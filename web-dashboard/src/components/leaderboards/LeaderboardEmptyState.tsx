import type { LeaderboardScope } from '../../types/leaderboard'
import { EmptyState } from '../ui/EmptyState'

interface LeaderboardEmptyStateProps {
  scope: LeaderboardScope
  categoryLabel: string
  hasValidGame: boolean
  pitchFilterApplied: boolean
}

export function LeaderboardEmptyState({
  scope,
  categoryLabel,
  hasValidGame,
  pitchFilterApplied,
}: LeaderboardEmptyStateProps) {
  let message = `No rows for ${categoryLabel} in the current scope.`

  if (scope === 'game' && !hasValidGame) {
    message = 'Select a game in the header to view game-scoped leaderboards.'
  } else if (pitchFilterApplied) {
    message = `No ${categoryLabel} rows match the active pitch filter in this scope.`
  }

  return <EmptyState>{message}</EmptyState>
}
