import { useFilters } from '../../context/ResearchContext'
import { TIMEFRAME_OPTIONS } from '../../types/research'

interface LeaderboardFilterNoteProps {
  pitchFilterApplied: boolean
}

/** Honest filter support notes for pre-computed leaderboard exports. */
export function LeaderboardFilterNote({
  pitchFilterApplied,
}: LeaderboardFilterNoteProps) {
  const { filters } = useFilters()
  const notes: string[] = []

  if (filters.timeframe !== 'season') {
    const label =
      TIMEFRAME_OPTIONS.find((o) => o.key === filters.timeframe)?.label ??
      filters.timeframe
    notes.push(
      `${label} timeframe does not apply to pre-computed leaderboard rows — metrics reflect the export Statcast window.`,
    )
  }

  if (filters.situation !== 'overall') {
    notes.push(
      'Situation splits are not applied to leaderboard rows — export values are season-window aggregates.',
    )
  }

  if (pitchFilterApplied) {
    notes.push(`Pitch filter active (${filters.pitchType}) — showing matching pitch rows only.`)
  }

  if (!notes.length) return null

  return (
    <p className="text-[10px] text-[#D29922]" role="status">
      {notes.join(' · ')}
    </p>
  )
}
