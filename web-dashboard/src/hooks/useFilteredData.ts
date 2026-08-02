import { useMemo } from 'react'
import { useExport } from '../context/ExportContext'
import { useGameContext } from '../context/ResearchContext'
import { useFilters } from '../context/ResearchContext'
import type { HitterRow } from '../types/slate'

/**
 * Returns matchup rows for the current research selection + filters.
 * Central slice helper — pages must not re-implement this filtering.
 */
export function useFilteredMatchupRows(): HitterRow[] {
  const exportData = useExport()
  const { selection } = useGameContext()
  const { filters } = useFilters()

  return useMemo(() => {
    let rows = exportData.matchups ?? []

    if (selection.gamePk != null) {
      rows = rows.filter((r) => r.game_pk === selection.gamePk)
    }

    if (selection.player && !selection.leagueMode) {
      const key = selection.player.name.toLowerCase()
      rows = rows.filter((r) => r.hitter.toLowerCase() === key)
    }

    if (filters.pitchType) {
      rows = rows.filter((r) => r.pitch === filters.pitchType)
    }

    return rows
  }, [exportData.matchups, selection.gamePk, selection.player, selection.leagueMode, filters.pitchType])
}
