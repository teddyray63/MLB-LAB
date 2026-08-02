import { Card } from '../ui/Card'
import { CategoryBoardTable } from '../CategoryBoardTable'
import { TopPlaysTable, type TopPlayRow } from '../TopPlaysTable'
import { LeaderboardPlayerLink } from './LeaderboardRow'
import type { HitterRow, TopPlay } from '../../types/slate'

interface LeaderboardTableProps {
  isTopPlaysView: boolean
  topPlays: TopPlay[]
  boardRows: HitterRow[]
  categoryLabel: string
}

/** Ranked results — reuses TopPlaysTable and CategoryBoardTable with row-scoped player links. */
export function LeaderboardTable({
  isTopPlaysView,
  topPlays,
  boardRows,
  categoryLabel,
}: LeaderboardTableProps) {
  if (isTopPlaysView) {
    const plays: TopPlayRow[] = topPlays.map((play) => ({
      ...play,
      category: categoryLabel,
    }))
    return (
      <TopPlaysTable
        plays={plays}
        showCategory={false}
        emptyMessage={`No top plays for ${categoryLabel}`}
        renderHitter={(play) => <LeaderboardPlayerLink row={play} />}
      />
    )
  }

  return (
    <CategoryBoardTable
      rows={boardRows}
      renderHitter={(row) => <LeaderboardPlayerLink row={row} />}
      emptyMessage={`No rows for ${categoryLabel}`}
    />
  )
}

export function LeaderboardResults({
  isTopPlaysView,
  topPlays,
  boardRows,
  categoryLabel,
}: LeaderboardTableProps) {
  return (
    <Card
      title={categoryLabel}
      subtitle={
        isTopPlaysView
          ? 'Curated top 5 per category · tier and composite score'
          : 'Top 20 · export ranking order · sortable columns'
      }
    >
      <LeaderboardTable
        isTopPlaysView={isTopPlaysView}
        topPlays={topPlays}
        boardRows={boardRows}
        categoryLabel={categoryLabel}
      />
    </Card>
  )
}
