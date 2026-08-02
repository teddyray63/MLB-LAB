import { useMemo } from 'react'
import { useExport } from '../context/ExportContext'
import { useGameContext, useFilters } from '../context/ResearchContext'
import { buildFilterSupportMatrix } from '../lib/filterSupport'
import { buildDataStatusSnapshot } from '../lib/dataStatus'
import { RESEARCH_SCHEMA_VERSION } from '../types/research'

/** Export health snapshot for the Data Status workspace. */
export function useDataStatus() {
  const exportData = useExport()
  const { selection } = useGameContext()
  const { filters } = useFilters()

  const snapshot = useMemo(
    () =>
      buildDataStatusSnapshot(
        exportData,
        RESEARCH_SCHEMA_VERSION,
        selection.player?.name ?? null,
      ),
    [exportData, selection.player?.name],
  )

  const filterSupport = useMemo(
    () => buildFilterSupportMatrix(exportData, selection),
    [exportData, selection],
  )

  return {
    snapshot,
    filterSupport,
    activeFilters: filters,
    selection,
  }
}
