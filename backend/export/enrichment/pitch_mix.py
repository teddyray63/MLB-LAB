"""Build pitcher pitch-mix summaries from pitch-level Statcast events."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from backend.export.daily_export_models import PitchMixEntry as ExportPitchMixEntry
from backend.export.enrichment.enrichment_models import PitchMixEntry, PitchMixSummary
from backend.export.enrichment.statcast_formulas import pitch_display_name
from backend.export.enrichment.statcast_source import StatcastEvents

MAJOR_PITCH_THRESHOLD = 0.08
USAGE_TOLERANCE = 0.02
SMALL_SAMPLE_PITCHES = 100


@dataclass
class PitchMixBuildResult:
    summaries: list[PitchMixSummary] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def build_pitch_mix_summaries(
    *,
    pitcher_ids: list[tuple[int, int]],
    events: StatcastEvents,
    window_start: str | None = None,
    window_end: str | None = None,
) -> PitchMixBuildResult:
    summaries: list[PitchMixSummary] = []
    warnings: list[str] = []

    for game_pk, pitcher_id in pitcher_ids:
        pitcher_rows = [row for row in events if row.get("pitcher") == pitcher_id]
        if not pitcher_rows:
            warnings.append(f"Missing pitch mix for pitcher {pitcher_id} game_pk {game_pk}")
            summaries.append(
                PitchMixSummary(
                    pitcher_id=pitcher_id,
                    game_pk=game_pk,
                    window_start=window_start,
                    window_end=window_end,
                    warnings=["missing pitch mix"],
                )
            )
            continue

        total = len(pitcher_rows)
        by_pitch: dict[str, list[dict[str, Any]]] = {}
        for row in pitcher_rows:
            code = str(row.get("pitch_type") or "UN")
            by_pitch.setdefault(code, []).append(row)

        entries: list[PitchMixEntry] = []
        usage_total = 0.0
        for code, rows in sorted(by_pitch.items(), key=lambda item: len(item[1]), reverse=True):
            count = len(rows)
            usage = count / total if total else 0.0
            usage_total += usage
            velocities = [float(row["release_speed"]) for row in rows if row.get("release_speed") is not None]
            entries.append(
                PitchMixEntry(
                    pitcher_id=pitcher_id,
                    pitch_code=code,
                    pitch_name=pitch_display_name(code),
                    pitch_count=count,
                    usage_pct=usage,
                    avg_velocity=(sum(velocities) / len(velocities)) if velocities else None,
                    max_velocity=max(velocities) if velocities else None,
                )
            )

        if abs(usage_total - 1.0) > USAGE_TOLERANCE and total > 0:
            warnings.append(
                f"Pitch usage for pitcher {pitcher_id} reconciles to {usage_total:.3f} "
                f"(tolerance {USAGE_TOLERANCE})"
            )

        summary_warnings: list[str] = []
        if total < SMALL_SAMPLE_PITCHES:
            summary_warnings.append(f"small sample ({total} pitches)")

        summaries.append(
            PitchMixSummary(
                pitcher_id=pitcher_id,
                game_pk=game_pk,
                window_start=window_start,
                window_end=window_end,
                entries=entries,
                small_sample=total < SMALL_SAMPLE_PITCHES,
                warnings=summary_warnings,
            )
        )

    return PitchMixBuildResult(summaries=summaries, warnings=_dedupe(warnings))


def major_pitch_codes(summary: PitchMixSummary) -> list[str]:
    return [
        entry.pitch_code
        for entry in summary.entries
        if entry.usage_pct >= MAJOR_PITCH_THRESHOLD
    ]


def to_export_pitch_mix(summary: PitchMixSummary) -> list[ExportPitchMixEntry]:
    return [
        ExportPitchMixEntry(pitch=entry.pitch_code, usage_pct=entry.usage_pct)
        for entry in summary.entries
        if entry.usage_pct >= MAJOR_PITCH_THRESHOLD
    ]


def _dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result
