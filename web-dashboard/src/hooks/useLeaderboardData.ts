import { useMemo } from 'react'
import { useExport } from '../context/ExportContext'
import { useGameContext } from '../context/ResearchContext'
import { useFilters } from '../context/ResearchContext'
import {
  applyPitchFilter,
  countExportLeaderboardRows,
  dedupeLeaderboardRows,
  exportDataWindowLabel,
  exportHasLeaderboardSections,
  filterRowsByScope,
  flattenTopPlays,
  getCategoryBoardRows,
  getValidSlateGamePks,
} from '../lib/leaderboardData'
import { CATEGORY_LABELS } from '../types/slate'
import type { LeaderboardCategory, LeaderboardScope } from '../types/leaderboard'
import type { HitterRow, TopPlay } from '../types/slate'

export interface LeaderboardDataResult {
  topPlays: TopPlay[]
  boardRows: HitterRow[]
  rowCount: number
  dataWindow: string | null
  pitchFilterApplied: boolean
  isTopPlaysView: boolean
  categoryLabel: string
  exportHasSourceRows: boolean
  exportHasLeaderboardSections: boolean
}

/**
 * Scoped and filtered leaderboard data — central slice for the workspace.
 * Pages must not re-implement scope or pitch filtering on export rows.
 */
export function useLeaderboardData(
  scope: LeaderboardScope,
  category: LeaderboardCategory,
): LeaderboardDataResult {
  const exportData = useExport()
  const { selection } = useGameContext()
  const { filters } = useFilters()

  return useMemo(() => {
    const validSlatePks = getValidSlateGamePks(exportData)
    const pitchFilterApplied = Boolean(filters.pitchType)
    const isTopPlaysView = category === 'top-plays'

    let topPlays: TopPlay[] = []
    let boardRows: HitterRow[] = []

    if (isTopPlaysView) {
      topPlays = flattenTopPlays(exportData, 'all')
      topPlays = filterRowsByScope(topPlays, scope, selection.gamePk, validSlatePks)
      topPlays = applyPitchFilter(topPlays, filters.pitchType)
      topPlays = dedupeLeaderboardRows(topPlays)
    } else {
      boardRows = getCategoryBoardRows(exportData, category)
      boardRows = filterRowsByScope(boardRows, scope, selection.gamePk, validSlatePks)
      boardRows = applyPitchFilter(boardRows, filters.pitchType)
      boardRows = dedupeLeaderboardRows(boardRows)
    }

    const rowCount = isTopPlaysView ? topPlays.length : boardRows.length
    const categoryLabel = isTopPlaysView ? 'Top Plays' : CATEGORY_LABELS[category]
    const exportHasSourceRows = countExportLeaderboardRows(exportData, category) > 0

    return {
      topPlays,
      boardRows,
      rowCount,
      dataWindow: exportDataWindowLabel(exportData),
      pitchFilterApplied,
      isTopPlaysView,
      categoryLabel,
      exportHasSourceRows,
      exportHasLeaderboardSections: exportHasLeaderboardSections(exportData),
    }
  }, [exportData, scope, category, selection.gamePk, filters.pitchType])
}
