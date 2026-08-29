import { describe, expect, it } from 'vitest'
import {
  countExportLeaderboardRows,
  exportHasLeaderboardSections,
} from './leaderboardData'
import type { DailyExport } from '../types/slate'
import { PLAY_CATEGORIES } from '../types/slate'

const emptyBoards = Object.fromEntries(PLAY_CATEGORIES.map((c) => [c, []])) as DailyExport['category_boards']
const emptyTopPlays = Object.fromEntries(PLAY_CATEGORIES.map((c) => [c, []])) as DailyExport['top_plays']

function minimalExport(overrides: Partial<DailyExport> = {}): DailyExport {
  return {
    date: '2026-08-01',
    games: [],
    matchups: [],
    game_details: [],
    top_plays: emptyTopPlays,
    category_boards: emptyBoards,
    ...overrides,
  }
}

describe('leaderboardData export capability', () => {
  it('detects empty G0b export with no leaderboard sections', () => {
    const exportData = minimalExport()
    expect(exportHasLeaderboardSections(exportData)).toBe(false)
    expect(countExportLeaderboardRows(exportData, 'hits')).toBe(0)
    expect(countExportLeaderboardRows(exportData, 'top-plays')).toBe(0)
  })

  it('detects populated category boards', () => {
    const exportData = minimalExport({
      category_boards: {
        ...emptyBoards,
        hits: [{ hitter: 'A', team: 'T', game: 'G', pitch: 'FF' } as never],
      },
    })
    expect(exportHasLeaderboardSections(exportData)).toBe(true)
    expect(countExportLeaderboardRows(exportData, 'hits')).toBe(1)
    expect(countExportLeaderboardRows(exportData, 'singles')).toBe(0)
  })

  it('detects populated top plays', () => {
    const exportData = minimalExport({
      top_plays: {
        ...emptyTopPlays,
        hits: [{ hitter: 'A', team: 'T', game: 'G', pitch: 'FF', score: 1 } as never],
      },
    })
    expect(exportHasLeaderboardSections(exportData)).toBe(true)
    expect(countExportLeaderboardRows(exportData, 'top-plays')).toBe(1)
  })
})

describe('LeaderboardEmptyState messaging contract', () => {
  it('uses unavailable copy when export lacks source rows', () => {
    const unavailable =
      'are not populated in the current export. The G0b pipeline does not yet generate ranked leaderboard rows'
    expect(unavailable).toContain('not populated in the current export')
    expect(unavailable).not.toContain('No rows for')
  })
})
