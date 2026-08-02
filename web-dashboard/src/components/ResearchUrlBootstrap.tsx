import { useEffect, useRef } from 'react'
import { useSearchParams } from 'react-router-dom'
import { useExport } from '../context/ExportContext'
import { buildSearchParamsPatch, searchParamsEqual } from '../lib/researchUrl'
import { firstValidGamePk } from '../lib/researchResolver'
import { RESEARCH_SCHEMA_VERSION, DEFAULT_SITUATION, DEFAULT_TIMEFRAME } from '../types/research'
import { useResearchChrome } from './ResearchChrome'

/** Writes default URL params once so refresh/copy-link preserves research context. */
export function ResearchUrlBootstrap() {
  const show = useResearchChrome()
  const exportData = useExport()
  const [searchParams, setSearchParams] = useSearchParams()
  const done = useRef(false)

  useEffect(() => {
    if (!show || done.current) return

    let next = new URLSearchParams(searchParams)
    let changed = false

    if (!next.get('v')) {
      next = buildSearchParamsPatch(next, {})
      changed = true
    }

    if (!next.get('date')) {
      next = buildSearchParamsPatch(next, { selection: { date: exportData.date } })
      changed = true
    }

    if (!next.get('game')) {
      const pk = firstValidGamePk(exportData)
      if (pk != null) {
        next = buildSearchParamsPatch(next, { selection: { gamePk: pk } })
        changed = true
      }
    }

    if (!next.get('tf')) {
      next = buildSearchParamsPatch(next, { filters: { timeframe: DEFAULT_TIMEFRAME } })
      changed = true
    }

    if (!next.get('sit')) {
      next = buildSearchParamsPatch(next, { filters: { situation: DEFAULT_SITUATION } })
      changed = true
    }

    const urlV = Number(next.get('v'))
    if (urlV !== RESEARCH_SCHEMA_VERSION) {
      next.set('v', String(RESEARCH_SCHEMA_VERSION))
      changed = true
    }

    if (changed && !searchParamsEqual(searchParams, next)) {
      setSearchParams(next, { replace: true })
    }

    done.current = true
  }, [show, exportData, searchParams, setSearchParams])

  return null
}
