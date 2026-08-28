import { useMemo } from 'react'
import { CategoryBoardTable } from '../CategoryBoardTable'
import { Card } from '../ui/Card'
import { useExport } from '../../context/ExportContext'
import { useGameContext, useFilters } from '../../context/ResearchContext'
import { useFilteredMatchupRows } from '../../hooks/useFilteredData'
import { formatPitchName } from '../../lib/pitchNames'
import {
  pitchMatchupScopeNote,
  pitchMatchupTeamCardSubtitle,
} from '../../lib/pitchTypeCopy'
import type { GameDetail, HitterRow } from '../../types/slate'

function MatchupTeamCard({
  team,
  side,
  oppSp,
  rows,
}: {
  team: string
  side: 'Away' | 'Home'
  oppSp: string
  rows: HitterRow[]
}) {
  return (
    <Card
      title={`${team} · ${side}`}
      subtitle={pitchMatchupTeamCardSubtitle(oppSp, rows.length)}
    >
      <CategoryBoardTable rows={rows} hideIdentity />
    </Card>
  )
}

function useSelectedGameDetail(): GameDetail | null {
  const data = useExport()
  const { selection } = useGameContext()
  if (selection.gamePk == null) return null
  return data.game_details?.find((g) => g.game_pk === selection.gamePk) ?? null
}

export function TodayMatchupsTab() {
  const { filters } = useFilters()
  const detail = useSelectedGameDetail()
  const allRows = useFilteredMatchupRows()

  const { awayRows, homeRows } = useMemo(() => {
    if (!detail) return { awayRows: [] as HitterRow[], homeRows: [] as HitterRow[] }
    return {
      awayRows: allRows.filter((r) => r.team === detail.away_team),
      homeRows: allRows.filter((r) => r.team === detail.home_team),
    }
  }, [allRows, detail])

  const pitchNote = filters.pitchType
    ? formatPitchName(filters.pitchType, { compact: true })
    : 'All pitches'

  if (!detail) {
    return (
      <Card title="Matchups" subtitle="Select a game">
        <p className="text-sm text-[#8B949E]">No matchup rows until a game is selected.</p>
      </Card>
    )
  }

  if (!allRows.length) {
    return (
      <Card title="Matchups" subtitle={`${pitchNote} · no rows for current filters`}>
        <p className="text-sm text-[#8B949E]">
          Try clearing the pitch filter or pick a different game.
        </p>
      </Card>
    )
  }

  return (
    <div className="space-y-4">
      <p className="text-xs text-[#8B949E]">
        {pitchMatchupScopeNote("today's SP", pitchNote)}
      </p>
      <div className="grid gap-5 xl:grid-cols-2">
        <MatchupTeamCard
          side="Away"
          team={detail.away_team}
          oppSp={detail.home_sp}
          rows={awayRows}
        />
        <MatchupTeamCard
          side="Home"
          team={detail.home_team}
          oppSp={detail.away_sp}
          rows={homeRows}
        />
      </div>
    </div>
  )
}
