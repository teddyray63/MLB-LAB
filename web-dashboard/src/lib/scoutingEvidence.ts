import { fmtMph, fmtPct, fmtRate } from '../design/format'
import { formatPitchName } from './pitchNames'
import { battingRateToHeat, rateToHeat } from '../design/tokens'
import type { HitterRow } from '../types/slate'
import type { ResearchPlayerData } from '../hooks/useResearchPlayerData'

export interface ScoutingSummary {
  strengths: string[]
  weaknesses: string[]
  pitcherProfile: { label: string; pct: string }[]
  evidence: { label: string; value: string }[]
}

const MIN_PITCH_PA = 8

function pitchRowsWithSample(rows: HitterRow[]): HitterRow[] {
  return rows.filter((r) => (r.pa ?? 0) >= MIN_PITCH_PA)
}

/**
 * Derive scouting bullets from export metrics only — no inference beyond thresholds.
 */
export function buildScoutingSummary(data: ResearchPlayerData): ScoutingSummary {
  const strengths: string[] = []
  const weaknesses: string[] = []
  const evidence: { label: string; value: string }[] = []

  const { aggregates, battedBallProfile, opposingPitchMix, pitcherMatchupRows, selection } = data

  const sampled = pitchRowsWithSample(pitcherMatchupRows.length ? pitcherMatchupRows : data.matchupRows)

  for (const row of sampled) {
    const pitchLabel = formatPitchName(row.pitch, { compact: true })
    const xwoba = row.xwoba
    const whiff = row.whiff_pct
    if (xwoba != null && battingRateToHeat(xwoba) === 'elite') {
      strengths.push(`Elite vs ${pitchLabel} (xwOBA ${fmtRate(xwoba)}, ${row.pa ?? 0} PA)`)
    }
    if (whiff != null) {
      const whiffPct = whiff <= 1 ? whiff * 100 : whiff
      if (rateToHeat(whiffPct, true) === 'poor' || whiffPct >= 40) {
        weaknesses.push(`Elevated whiff vs ${pitchLabel} (${fmtPct(whiff)}, ${row.pa ?? 0} PA)`)
      }
    }
    if (xwoba != null && battingRateToHeat(xwoba) === 'poor') {
      weaknesses.push(`Below-average vs ${pitchLabel} (xwOBA ${fmtRate(xwoba)}, ${row.pa ?? 0} PA)`)
    }
  }

  if (battedBallProfile?.pull_pct != null) {
    const pull = battedBallProfile.pull_pct <= 1 ? battedBallProfile.pull_pct : battedBallProfile.pull_pct / 100
    if (pull >= 0.4) {
      strengths.push(`Pull-side contact ${fmtPct(battedBallProfile.pull_pct)} of BBE`)
    }
  }

  const pitcherProfile = opposingPitchMix.map(({ pitch, usage_pct }) => {
    const pct =
      usage_pct == null || Number.isNaN(usage_pct)
        ? '—'
        : `${((usage_pct <= 1 ? usage_pct * 100 : usage_pct)).toFixed(0)}%`
    return {
      label: formatPitchName(pitch, { compact: true }),
      pct,
    }
  })

  const evidenceFields: { key: keyof typeof aggregates; label: string; format: (v: number) => string }[] = [
    { key: 'xwoba', label: 'xwOBA', format: fmtRate },
    { key: 'barrelPct', label: 'Barrel%', format: fmtPct },
    { key: 'batSpeed', label: 'Bat Speed', format: fmtMph },
    { key: 'whiffPct', label: 'Whiff%', format: fmtPct },
    { key: 'hardHitPct', label: 'Hard Hit%', format: fmtPct },
  ]

  for (const { key, label, format } of evidenceFields) {
    const val = aggregates[key]
    if (val != null && !Number.isNaN(val)) {
      evidence.push({ label, value: format(val) })
    }
  }

  const split = data.activeSplitLine
  if (split && 'xwoba' in split && split.xwoba != null) {
    evidence.push({ label: 'Split xwOBA', value: fmtRate(split.xwoba as number) })
  }

  const pitcherName = selection.pitcher?.name ?? selection.opposingPitcher?.name
  if (pitcherName && !pitcherProfile.length) {
    pitcherProfile.push({ label: pitcherName, pct: 'mix unavailable' })
  }

  return {
    strengths: strengths.slice(0, 4),
    weaknesses: weaknesses.slice(0, 4),
    pitcherProfile: pitcherProfile.slice(0, 6),
    evidence,
  }
}
