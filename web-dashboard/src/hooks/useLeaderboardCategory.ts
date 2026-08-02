import { useCallback, useEffect, useMemo } from 'react'
import { useSearchParams } from 'react-router-dom'
import { buildSearchParamsPatch } from '../lib/researchUrl'
import {
  LEADERBOARD_CATEGORIES,
  type LeaderboardCategory,
} from '../types/leaderboard'

function parseCategory(raw: string | null): LeaderboardCategory {
  if (raw && LEADERBOARD_CATEGORIES.includes(raw as LeaderboardCategory)) {
    return raw as LeaderboardCategory
  }
  return 'top-plays'
}

/** Leaderboard category/view — synced to URL `tab` param (page-local). */
export function useLeaderboardCategory() {
  const [searchParams, setSearchParams] = useSearchParams()

  const category = useMemo(
    () => parseCategory(searchParams.get('tab')),
    [searchParams],
  )

  useEffect(() => {
    const raw = searchParams.get('tab')
    if (!raw || !LEADERBOARD_CATEGORIES.includes(raw as LeaderboardCategory)) {
      const next = buildSearchParamsPatch(searchParams, { tab: 'top-plays' })
      setSearchParams(next, { replace: true })
    }
  }, [searchParams, setSearchParams])

  const setCategory = useCallback(
    (next: LeaderboardCategory) => {
      const params = buildSearchParamsPatch(searchParams, { tab: next })
      setSearchParams(params, { replace: true })
    },
    [searchParams, setSearchParams],
  )

  return { category, setCategory }
}
