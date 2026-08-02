import { useLocation } from 'react-router-dom'
import { ResearchContextHeader } from './ResearchContextHeader'
import { FilterBar } from './FilterBar'
import { ResearchUrlBootstrap } from './ResearchUrlBootstrap'

const RESEARCH_CHROME_PREFIXES = ['/today', '/research', '/leaderboards']

const RESEARCH_CHROME_EXCLUDED = ['/settings', '/data-status', '/history']

export function useResearchChrome(): boolean {
  const { pathname } = useLocation()
  if (pathname.startsWith('/legacy')) return false
  if (RESEARCH_CHROME_EXCLUDED.some((p) => pathname === p || pathname.startsWith(`${p}/`))) {
    return false
  }
  return RESEARCH_CHROME_PREFIXES.some(
    (p) => pathname === p || pathname.startsWith(`${p}/`),
  )
}

/** Persistent research chrome — context header + shared filters (Phase A). */
export function ResearchChrome() {
  const show = useResearchChrome()
  if (!show) return null

  return (
    <>
      <ResearchUrlBootstrap />
      <ResearchContextHeader />
      <FilterBar />
    </>
  )
}
