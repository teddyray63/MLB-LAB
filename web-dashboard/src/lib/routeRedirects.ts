import { RESEARCH_PATH } from './researchNavigation'
import { URL_KEYS } from './researchUrl'

/** Query keys preserved across IA route redirects (Phase E). */
export const PRESERVED_QUERY_KEYS = [
  URL_KEYS.schemaVersion,
  URL_KEYS.date,
  URL_KEYS.game,
  URL_KEYS.player,
  URL_KEYS.pitcher,
  URL_KEYS.side,
  URL_KEYS.tab,
  URL_KEYS.timeframe,
  URL_KEYS.situation,
  URL_KEYS.pitch,
  URL_KEYS.scope,
] as const

export interface ResearchRedirectPathContext {
  gameId?: string
  playerId?: string
}

/** Copy supported research query params from an incoming search string. */
export function preserveQueryParams(source: URLSearchParams): URLSearchParams {
  const next = new URLSearchParams()
  for (const key of PRESERVED_QUERY_KEYS) {
    const value = source.get(key)
    if (value != null) next.set(key, value)
  }
  return next
}

/**
 * Build the query string for `/research` redirects.
 * Translates legacy `name=` and path segments into canonical `player` / `game` params.
 */
export function buildResearchRedirectSearch(
  search: string,
  pathCtx: ResearchRedirectPathContext = {},
): string {
  const source = new URLSearchParams(search)
  const next = preserveQueryParams(source)

  const legacyName = source.get('name')
  if (legacyName && !next.get(URL_KEYS.player)) {
    next.set(URL_KEYS.player, legacyName)
  }

  if (pathCtx.playerId && !next.get(URL_KEYS.player)) {
    next.set(URL_KEYS.player, decodeURIComponent(pathCtx.playerId))
  }

  if (pathCtx.gameId && !next.get(URL_KEYS.game)) {
    const decoded = decodeURIComponent(pathCtx.gameId)
    if (/^\d+$/.test(decoded)) {
      next.set(URL_KEYS.game, decoded)
    }
  }

  const qs = next.toString()
  return qs ? `?${qs}` : ''
}

/** Full `/research` redirect target including preserved or translated query state. */
export function buildResearchRedirectPath(
  search: string,
  pathCtx: ResearchRedirectPathContext = {},
): string {
  return `${RESEARCH_PATH}${buildResearchRedirectSearch(search, pathCtx)}`
}
