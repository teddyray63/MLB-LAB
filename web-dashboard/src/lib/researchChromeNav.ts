/** Primary nav routes that share URL-synced research context. */
export const RESEARCH_CONTEXT_NAV_PATHS = ['/today', '/research', '/leaderboards'] as const

export type ResearchContextNavPath = (typeof RESEARCH_CONTEXT_NAV_PATHS)[number]

export function isResearchContextNavPath(path: string): path is ResearchContextNavPath {
  return (RESEARCH_CONTEXT_NAV_PATHS as readonly string[]).includes(path)
}

/**
 * React Router `to` value for primary nav items.
 * Preserves query string when moving among research-context routes.
 */
export function primaryNavLinkTo(
  itemTo: string,
  currentSearch: string,
): string | { pathname: string; search: string } {
  if (isResearchContextNavPath(itemTo)) {
    return { pathname: itemTo, search: currentSearch }
  }
  return itemTo
}
