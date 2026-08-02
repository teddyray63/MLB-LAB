import { useEffect, useMemo, useState } from 'react'
import { CategoryBoardTable } from '../components/CategoryBoardTable'
import { PitchMixFilterChips, normalizePitchMixItems } from '../components/PitchMixFilterChips'
import { TeamSplitsTable, type SplitKey } from '../components/TeamSplitsTable'
import { Card } from '../components/ui/Card'
import { SectionBanner } from '../components/ui/SectionBanner'
import { useExport } from '../context/ExportContext'
import type { GameDetail, HitterRow, SplitHitter } from '../types/slate'

const SPLITS: { key: SplitKey; label: string }[] = [
  { key: 'overall', label: 'Overall' },
  { key: 'vs_lhp', label: 'vs LHP' },
  { key: 'vs_rhp', label: 'vs RHP' },
  { key: 'day_split', label: 'Day' },
  { key: 'night_split', label: 'Night' },
  { key: 'bvp', label: 'vs Today’s SP' },
]

function TeamSplitCard({
  team,
  side,
  sp,
  rows,
  split,
  gameId,
  pitchMix,
  matchupRows,
}: {
  team: string
  side: 'Away' | 'Home'
  sp: string
  rows: SplitHitter[]
  split: SplitKey
  gameId: string
  pitchMix: GameDetail['away_pitch_mix']
  matchupRows: HitterRow[]
}) {
  const [pitchFilter, setPitchFilter] = useState<string | null>(null)

  useEffect(() => {
    setPitchFilter(null)
  }, [gameId, team])

  const visible = useMemo(
    () => (split === 'bvp' ? rows.filter((r) => r.bvp != null) : rows),
    [rows, split],
  )

  const pitchChips = normalizePitchMixItems(pitchMix)

  const filteredMatchups = useMemo(() => {
    if (!pitchFilter) return []
    return matchupRows.filter((r) => r.pitch === pitchFilter)
  }, [matchupRows, pitchFilter])

  const subtitle =
    pitchFilter
      ? `${pitchFilter} only · vs ${sp || 'opposing SP'} pitch mix`
      : split === 'bvp'
      ? `Batter vs pitcher · 120-day window vs ${sp || 'opposing SP'}`
      : split === 'vs_lhp'
        ? 'vs left-handed pitching'
        : split === 'vs_rhp'
          ? 'vs right-handed pitching'
          : split === 'day_split'
            ? 'Day games · MLB Stats API dayNight joined on game_pk'
            : split === 'night_split'
              ? 'Night games · MLB Stats API dayNight joined on game_pk'
              : '120-day season line'

  return (
    <Card title={`${team} · ${side}`} subtitle={subtitle}>
      {pitchChips.length > 0 && (
        <PitchMixFilterChips
          pitches={pitchChips}
          selected={pitchFilter}
          onSelect={setPitchFilter}
        />
      )}
      {pitchFilter ? (
        <>
          <p className="mb-2 text-[10px] text-[#58A6FF]">
            Per-pitch stats vs {sp} · {filteredMatchups.length} hitter
            {filteredMatchups.length === 1 ? '' : 's'}
          </p>
          <CategoryBoardTable rows={filteredMatchups} hideIdentity />
        </>
      ) : (
        <TeamSplitsTable rows={visible} split={split} />
      )}
    </Card>
  )
}

export function TeamSplitsPage() {
  const data = useExport()
  const games = data.game_details ?? []
  const [gameId, setGameId] = useState(games[0]?.game_id ?? '')
  const [split, setSplit] = useState<SplitKey>('overall')

  const selected = useMemo(
    () => games.find((g) => g.game_id === gameId) ?? games[0],
    [games, gameId],
  )

  const awayMatchups = useMemo(() => {
    if (!selected) return []
    return data.matchups.filter(
      (r) => r.game === selected.game_id && r.team === selected.away_team,
    )
  }, [data.matchups, selected])

  const homeMatchups = useMemo(() => {
    if (!selected) return []
    return data.matchups.filter(
      (r) => r.game === selected.game_id && r.team === selected.home_team,
    )
  }, [data.matchups, selected])

  const hasSplits = games.some(
    (g) => (g.away_splits?.length ?? 0) > 0 || (g.home_splits?.length ?? 0) > 0,
  )

  if (!games.length || !selected || !hasSplits) {
    return (
      <div className="space-y-5">
        <div>
          <p className="text-xs font-medium uppercase tracking-[0.12em] text-[#8B949E]">
            Team Splits
          </p>
          <h2 className="text-2xl font-bold tracking-tight">{data.date}</h2>
        </div>
        <Card title="No split data" subtitle="away_splits / home_splits missing in today's export">
          <p className="text-sm text-[#8B949E]">
            Re-run the Python export to populate platoon (vs LHP/RHP) and batter-vs-pitcher splits.
          </p>
        </Card>
      </div>
    )
  }

  return (
    <div className="space-y-5">
      <div className="flex flex-wrap items-end justify-between gap-4">
        <div>
          <p className="text-xs font-medium uppercase tracking-[0.12em] text-[#8B949E]">
            Team Splits
          </p>
          <h2 className="text-2xl font-bold tracking-tight">{data.date}</h2>
          <p className="mt-1 text-sm text-[#8B949E]">
            Platoon &amp; batter-vs-pitcher splits · ISO / BABIP / wOBA by player
          </p>
        </div>
        <label className="flex items-center gap-2 text-xs text-[#8B949E]">
          Game
          <select
            value={selected.game_id}
            onChange={(e) => setGameId(e.target.value)}
            className="min-w-[16rem] rounded-md border border-[#30363D] bg-[#161B22] px-2 py-1.5 text-xs text-[#F0F6FC]"
          >
            {games.map((g) => (
              <option key={g.game_id} value={g.game_id}>
                {g.away_team} @ {g.home_team}
              </option>
            ))}
          </select>
        </label>
      </div>

      <div className="flex flex-wrap items-center gap-1">
        {SPLITS.map(({ key, label }) => (
          <button
            key={key}
            type="button"
            onClick={() => setSplit(key)}
            className={`rounded-md border px-3 py-1.5 text-[11px] font-medium transition-colors ${
              split === key
                ? 'border-[#58A6FF] bg-[#1F6FEB33] text-[#58A6FF]'
                : 'border-[#30363D] text-[#8B949E] hover:bg-[#21262D] hover:text-[#F0F6FC]'
            }`}
          >
            {label}
          </button>
        ))}
      </div>

      <SectionBanner label={selected.game_id} />

      <div className="grid gap-5 xl:grid-cols-2">
        <TeamSplitCard
          side="Away"
          team={selected.away_team}
          sp={selected.home_sp}
          rows={selected.away_splits ?? []}
          split={split}
          gameId={selected.game_id}
          pitchMix={selected.home_pitch_mix}
          matchupRows={awayMatchups}
        />
        <TeamSplitCard
          side="Home"
          team={selected.home_team}
          sp={selected.away_sp}
          rows={selected.home_splits ?? []}
          split={split}
          gameId={selected.game_id}
          pitchMix={selected.away_pitch_mix}
          matchupRows={homeMatchups}
        />
      </div>
    </div>
  )
}
