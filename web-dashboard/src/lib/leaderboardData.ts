import type { DailyExport, Game, HitterRow, PlayCategory, TopPlay } from '../types/slate'
import type { LeaderboardScope } from '../types/leaderboard'

/** Exclude duplicate placeholder slate entries (TBD starters sharing a game_pk). */
export function isValidSlateGame(game: Game): boolean {
  return game.away_sp !== 'TBD' && game.home_sp !== 'TBD'
}

/** Canonical game_pk set for today's slate — one entry per pk, placeholders excluded. */
export function getValidSlateGamePks(exportData: DailyExport): Set<number> {
  const pks = new Set<number>()
  for (const game of exportData.games ?? []) {
    if (game.game_pk != null && isValidSlateGame(game)) {
      pks.add(game.game_pk)
    }
  }
  return pks
}

/** Remove duplicate rows that share game_pk + hitter + team + pitch. */
export function dedupeLeaderboardRows<
  T extends { hitter: string; team: string; game_pk?: number | null; pitch?: string; game?: string },
>(rows: T[]): T[] {
  const seen = new Set<string>()
  const result: T[] = []
  for (const row of rows) {
    const key = `${row.game_pk ?? row.game ?? ''}|${row.hitter}|${row.team}|${row.pitch ?? ''}`
    if (seen.has(key)) continue
    seen.add(key)
    result.push(row)
  }
  return result
}

export function filterRowsByScope<T extends { game_pk?: number | null }>(
  rows: T[],
  scope: LeaderboardScope,
  gamePk: number | null,
  validSlatePks: Set<number>,
): T[] {
  if (scope === 'game') {
    if (gamePk == null) return []
    return rows.filter((r) => r.game_pk === gamePk)
  }
  if (scope === 'slate') {
    return rows.filter((r) => r.game_pk != null && validSlatePks.has(r.game_pk))
  }
  return rows
}

export function applyPitchFilter<T extends { pitch?: string }>(
  rows: T[],
  pitchType: string | null,
): T[] {
  if (!pitchType) return rows
  return rows.filter((r) => r.pitch === pitchType)
}

export function flattenTopPlays(
  exportData: DailyExport,
  category: PlayCategory | 'all',
): TopPlay[] {
  if (category !== 'all') {
    return exportData.top_plays[category] ?? []
  }
  const rows: TopPlay[] = []
  for (const key of Object.keys(exportData.top_plays) as PlayCategory[]) {
    rows.push(...(exportData.top_plays[key] ?? []))
  }
  return rows
}

export function getCategoryBoardRows(
  exportData: DailyExport,
  category: PlayCategory,
): HitterRow[] {
  return exportData.category_boards[category] ?? []
}

export function inferTeamSide(
  exportData: DailyExport,
  row: Pick<HitterRow, 'team' | 'game_pk' | 'game'>,
): 'away' | 'home' | undefined {
  const detail =
    row.game_pk != null
      ? exportData.game_details?.find((g) => g.game_pk === row.game_pk && g.away_sp !== 'TBD')
      : exportData.game_details?.find((g) => g.game_id === row.game)
  if (!detail) return undefined
  if (row.team === detail.away_team) return 'away'
  if (row.team === detail.home_team) return 'home'
  return undefined
}

export function exportDataWindowLabel(exportData: DailyExport): string | null {
  const meta = exportData.export_meta
  if (!meta?.statcast_start || !meta?.statcast_end) return null
  return `${meta.statcast_start} – ${meta.statcast_end}`
}
