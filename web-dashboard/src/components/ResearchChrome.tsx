import { useLocation } from 'react-router-dom'
import { ResearchContextHeader } from './ResearchContextHeader'
import { FilterBar } from './FilterBar'
import { ResearchUrlBootstrap } from './ResearchUrlBootstrap'

const RESEARCH_PATH_PREFIXES = [
  '/today',
  '/research',
  '/leaderboards',
  '/game',
  '/player',
  '/matchup',
]

export function useResearchChrome(): boolean {
  const { pathname } = useLocation()
  if (pathname.startsWith('/legacy')) return false
  if (pathname === '/settings' || pathname === '/history') return false
  return RESEARCH_PATH_PREFIXES.some(
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
