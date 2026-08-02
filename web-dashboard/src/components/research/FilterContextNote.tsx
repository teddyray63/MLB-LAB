import type { ReactNode } from 'react'
import { Card } from '../ui/Card'
import { useFilters } from '../../context/ResearchContext'
import { TIMEFRAME_OPTIONS } from '../../types/research'

/** Honest note when active filters are unsupported or export-limited. */
export function FilterContextNote() {
  const { filters } = useFilters()

  const tfSupport = filters.support.timeframe[filters.timeframe]
  const sitSupport = filters.support.situation[filters.situation]

  const notes: string[] = []

  if (!tfSupport.supported) {
    notes.push(tfSupport.reason ?? 'Timeframe filter not supported for this view.')
  } else if (filters.timeframe !== 'season') {
    notes.push(
      `Matchup tables reflect the export season window; ${TIMEFRAME_OPTIONS.find((o) => o.key === filters.timeframe)?.label ?? filters.timeframe} slicing applies where game logs exist.`,
    )
  }

  if (!sitSupport.supported && filters.situation !== 'overall') {
    notes.push(sitSupport.reason ?? 'Situation split unavailable.')
  }

  if (!notes.length) return null

  return (
    <p className="mb-3 text-[10px] text-[#D29922]">
      {notes.join(' · ')}
    </p>
  )
}

export function ResearchPanelShell({
  title,
  subtitle,
  children,
}: {
  title: string
  subtitle?: string
  children: ReactNode
}) {
  return (
    <Card title={title} subtitle={subtitle}>
      <FilterContextNote />
      {children}
    </Card>
  )
}
