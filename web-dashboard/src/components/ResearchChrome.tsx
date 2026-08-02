import { useRef } from 'react'
import { useLocation } from 'react-router-dom'
import { useLayoutHeightVar } from '../hooks/useLayoutHeightVar'
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
  const chromeRef = useRef<HTMLDivElement>(null)
  // Measured for --research-chrome-height; only wire consumers if overlap is proven.
  useLayoutHeightVar(chromeRef, '--research-chrome-height', show)

  if (!show) return null

  return (
    <>
      <ResearchUrlBootstrap />
      <div
        ref={chromeRef}
        className="sticky z-10 -mx-4 mb-5 flex flex-col gap-4 border-b border-[#30363D] bg-[#0D1117]/95 px-4 backdrop-blur supports-[backdrop-filter]:bg-[#0D1117]/90"
        style={{ top: 'var(--app-header-height, 0px)' }}
      >
        <ResearchContextHeader />
        <FilterBar />
      </div>
    </>
  )
}
