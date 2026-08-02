import { useCallback, useMemo } from 'react'
import { useSearchParams } from 'react-router-dom'
import { buildSearchParamsPatch } from '../lib/researchUrl'
import type { ResearchTabKey } from '../lib/researchNavigation'

const TAB_KEYS: ResearchTabKey[] = [
  'overview',
  'matchup',
  'recent-games',
  'splits',
  'pitch-matchup',
  'heatmaps',
  'batted-balls',
  'swing-metrics',
  'outcome-profile',
  'scouting-summary',
]

function parseTab(raw: string | null): ResearchTabKey {
  if (raw && TAB_KEYS.includes(raw as ResearchTabKey)) {
    return raw as ResearchTabKey
  }
  return 'overview'
}

/** Research workspace tab — synced to URL `tab` param (page-local, no context changes). */
export function useResearchTab() {
  const [searchParams, setSearchParams] = useSearchParams()

  const tab = useMemo(
    () => parseTab(searchParams.get('tab')),
    [searchParams],
  )

  const setTab = useCallback(
    (next: ResearchTabKey) => {
      const params = buildSearchParamsPatch(searchParams, { tab: next })
      setSearchParams(params, { replace: true })
    },
    [searchParams, setSearchParams],
  )

  return { tab, setTab }
}

export const RESEARCH_TABS: { key: ResearchTabKey; label: string }[] = [
  { key: 'overview', label: 'Overview' },
  { key: 'matchup', label: 'Matchup' },
  { key: 'recent-games', label: 'Recent Games' },
  { key: 'splits', label: 'Splits' },
  { key: 'pitch-matchup', label: 'Pitch Matchup' },
  { key: 'heatmaps', label: 'Heatmaps' },
  { key: 'batted-balls', label: 'Batted Balls' },
  { key: 'swing-metrics', label: 'Swing Metrics' },
  { key: 'outcome-profile', label: 'Outcome Profile' },
  { key: 'scouting-summary', label: 'Scouting Summary' },
]
