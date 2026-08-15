import type { TimeframeKey } from '../types/research'
import type { GameLogEntry } from '../types/slate'

/** Max recent games for a timeframe filter, or null for season (full log). */
export function timeframeToGameLimit(timeframe: TimeframeKey): number | null {
  switch (timeframe) {
    case 'l5':
      return 5
    case 'l7':
      return 7
    case 'l10':
      return 10
    case 'l15':
      return 15
    case 'l20':
      return 20
    case 'season':
    default:
      return null
  }
}

/** Slice a most-recent-first game log for the active timeframe filter. */
export function sliceGameLogByTimeframe(
  log: GameLogEntry[] | undefined,
  timeframe: TimeframeKey,
): GameLogEntry[] {
  if (!log?.length) return []
  const limit = timeframeToGameLimit(timeframe)
  if (limit == null) return log
  return log.slice(0, limit)
}
