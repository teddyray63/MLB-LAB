import type { LeaderboardScope } from '../../types/leaderboard'
import { EmptyState } from '../ui/EmptyState'

interface LeaderboardEmptyStateProps {
  scope: LeaderboardScope
  categoryLabel: string
  hasValidGame: boolean
  pitchFilterApplied: boolean
  /** Export contains rows for this view before scope/pitch filtering. */
  exportHasSourceRows: boolean
}

export function LeaderboardEmptyState({
  scope,
  categoryLabel,
  hasValidGame,
  pitchFilterApplied,
  exportHasSourceRows,
}: LeaderboardEmptyStateProps) {
  if (!exportHasSourceRows) {
    return (
      <EmptyState>
        {categoryLabel} are not populated in the current export. The G0b pipeline does not
        yet generate ranked leaderboard rows — re-run export when ranking formulas are
        available.
      </EmptyState>
    )
  }

  let message = `No rows for ${categoryLabel} in the current scope.`

  if (scope === 'game' && !hasValidGame) {
    message = 'Select a game in the header to view game-scoped leaderboards.'
  } else if (pitchFilterApplied) {
    message = `No ${categoryLabel} rows match the active pitch filter in this scope.`
  }

  return <EmptyState>{message}</EmptyState>
}
