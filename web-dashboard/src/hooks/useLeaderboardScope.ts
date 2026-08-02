import { useCallback, useEffect, useMemo } from 'react'
import { useSearchParams } from 'react-router-dom'
import { useGameContext } from '../context/ResearchContext'
import { buildSearchParamsPatch } from '../lib/researchUrl'
import type { LeaderboardScope } from '../types/leaderboard'

const SCOPES: LeaderboardScope[] = ['game', 'slate', 'league']

function parseScope(raw: string | null): LeaderboardScope | null {
  if (raw && SCOPES.includes(raw as LeaderboardScope)) {
    return raw as LeaderboardScope
  }
  return null
}

function defaultScope(hasValidGame: boolean): LeaderboardScope {
  return hasValidGame ? 'game' : 'slate'
}

/** Leaderboard scope — synced to URL `scope` param. */
export function useLeaderboardScope() {
  const { selection } = useGameContext()
  const [searchParams, setSearchParams] = useSearchParams()

  const hasValidGame = selection.gamePk != null

  const scope = useMemo(() => {
    const parsed = parseScope(searchParams.get('scope'))
    if (parsed) return parsed
    return defaultScope(hasValidGame)
  }, [searchParams, hasValidGame])

  useEffect(() => {
    const parsed = parseScope(searchParams.get('scope'))
    if (!parsed) {
      const next = buildSearchParamsPatch(searchParams, {
        scope: defaultScope(hasValidGame),
      })
      setSearchParams(next, { replace: true })
    }
  }, [searchParams, setSearchParams, hasValidGame])

  const setScope = useCallback(
    (next: LeaderboardScope) => {
      const params = buildSearchParamsPatch(searchParams, { scope: next })
      setSearchParams(params, { replace: true })
    },
    [searchParams, setSearchParams],
  )

  return { scope, setScope, hasValidGame }
}
