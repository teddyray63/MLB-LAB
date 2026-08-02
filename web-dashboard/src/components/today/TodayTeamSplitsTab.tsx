import { useMemo } from 'react'
import { CategoryBoardTable } from '../CategoryBoardTable'
import { TeamSplitsTable, type SplitKey } from '../TeamSplitsTable'
import { Card } from '../ui/Card'
import { useExport } from '../../context/ExportContext'
import { useGameContext, useFilters } from '../../context/ResearchContext'
import { formatPitchName } from '../../lib/pitchNames'
import type { SituationKey } from '../../types/research'
import type { GameDetail, HitterRow, SplitHitter } from '../../types/slate'

function situationToSplit(situation: SituationKey): SplitKey {
  switch (situation) {
    case 'vlhp':
      return 'vs_lhp'
    case 'vrhp':
      return 'vs_rhp'
    case 'day':
      return 'day_split'
    case 'night':
      return 'night_split'
    default:
      return 'overall'
  }
}

function splitSubtitle(split: SplitKey, sp: string, pitchFilter: string | null): string {
  if (pitchFilter) {
    return `${formatPitchName(pitchFilter, { compact: true })} only · vs ${sp || 'opposing SP'} pitch mix`
  }
  if (split === 'vs_lhp') return 'vs left-handed pitching'
  if (split === 'vs_rhp') return 'vs right-handed pitching'
  if (split === 'day_split') return 'Day games · MLB Stats API dayNight joined on game_pk'
  if (split === 'night_split') return 'Night games · MLB Stats API dayNight joined on game_pk'
  return '120-day season line · driven by shared situation filter'
}

function TeamSplitPanel({
  team,
  side,
  sp,
  rows,
  split,
  pitchFilter,
  matchupRows,
}: {
  team: string
  side: 'Away' | 'Home'
  sp: string
  rows: SplitHitter[]
  split: SplitKey
  pitchFilter: string | null
  matchupRows: HitterRow[]
}) {
  const visible = useMemo(
    () => (split === 'bvp' ? rows.filter((r) => r.bvp != null) : rows),
    [rows, split],
  )

  const filteredMatchups = useMemo(() => {
    if (!pitchFilter) return []
    return matchupRows.filter((r) => r.pitch === pitchFilter)
  }, [matchupRows, pitchFilter])

  const teamSide = side === 'Away' ? 'away' : 'home'

  return (
    <Card title={`${team} · ${side}`} subtitle={splitSubtitle(split, sp, pitchFilter)}>
      {pitchFilter ? (
        <>
          <p className="mb-2 text-[10px] text-[#58A6FF]">
            Per-pitch stats vs {sp} · {filteredMatchups.length} hitter
            {filteredMatchups.length === 1 ? '' : 's'}
          </p>
          <CategoryBoardTable rows={filteredMatchups} hideIdentity />
        </>
      ) : (
        <TeamSplitsTable rows={visible} split={split} teamSide={teamSide} />
      )}
    </Card>
  )
}

function useSelectedGameDetail(): GameDetail | null {
  const data = useExport()
  const { selection } = useGameContext()
  if (selection.gamePk == null) return null
  return data.game_details?.find((g) => g.game_pk === selection.gamePk) ?? null
}

export function TodayTeamSplitsTab() {
  const data = useExport()
  const { filters } = useFilters()
  const detail = useSelectedGameDetail()

  const split = situationToSplit(filters.situation)
  const pitchFilter = filters.pitchType

  const awayMatchups = useMemo(() => {
    if (!detail) return []
    return data.matchups.filter(
      (r) => r.game_pk === detail.game_pk && r.team === detail.away_team,
    )
  }, [data.matchups, detail])

  const homeMatchups = useMemo(() => {
    if (!detail) return []
    return data.matchups.filter(
      (r) => r.game_pk === detail.game_pk && r.team === detail.home_team,
    )
  }, [data.matchups, detail])

  if (!detail) {
    return (
      <Card title="Team splits" subtitle="Select a game">
        <p className="text-sm text-[#8B949E]">No split data until a game is selected.</p>
      </Card>
    )
  }

  const hasSplits =
    (detail.away_splits?.length ?? 0) > 0 || (detail.home_splits?.length ?? 0) > 0

  if (!hasSplits) {
    return (
      <Card title="No split data" subtitle="away_splits / home_splits missing in today's export">
        <p className="text-sm text-[#8B949E]">
          Re-run the Python export to populate platoon and batter-vs-pitcher splits.
        </p>
      </Card>
    )
  }

  return (
    <div className="grid gap-5 xl:grid-cols-2">
      <TeamSplitPanel
        side="Away"
        team={detail.away_team}
        sp={detail.home_sp}
        rows={detail.away_splits ?? []}
        split={split}
        pitchFilter={pitchFilter}
        matchupRows={awayMatchups}
      />
      <TeamSplitPanel
        side="Home"
        team={detail.home_team}
        sp={detail.away_sp}
        rows={detail.home_splits ?? []}
        split={split}
        pitchFilter={pitchFilter}
        matchupRows={homeMatchups}
      />
    </div>
  )
}
