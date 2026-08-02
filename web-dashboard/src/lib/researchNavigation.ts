import type { FilterOverride, ResolvedResearchSelection, TeamSide } from '../types/research'
import { buildSearchParamsPatch } from './researchUrl'

/** Canonical research workspace route (Phase C+). */
export const RESEARCH_PATH = '/research' as const

/** In-page research tabs — extend as Phase C panels ship. */
export type ResearchTabKey =
  | 'overview'
  | 'matchup'
  | 'recent-games'
  | 'splits'
  | 'pitch-matchup'
  | 'heatmaps'
  | 'batted-balls'
  | 'swing-metrics'
  | 'outcome-profile'
  | 'scouting-summary'

export interface OpenResearchOptions {
  /** Batter to investigate — required */
  player: string
  pitcher?: string | null
  /** gamePk — defaults to current selection when omitted */
  game?: number | null
  date?: string
  side?: TeamSide | null
  tab?: ResearchTabKey | string
  leagueMode?: boolean
  /** Filter overrides; omit to preserve active URL filters */
  filters?: FilterOverride
}

export interface ResearchNavigationContext {
  currentParams: URLSearchParams
  selection: Pick<ResolvedResearchSelection, 'date' | 'gamePk'>
}

export interface ResearchNavigationTarget {
  pathname: typeof RESEARCH_PATH
  search: string
}

/**
 * Single source of truth for `/research?v=2&…` URLs.
 * Preserves current filter params unless explicitly overridden.
 */
export function buildResearchNavigation(
  ctx: ResearchNavigationContext,
  opts: OpenResearchOptions,
): ResearchNavigationTarget {
  const next = buildSearchParamsPatch(ctx.currentParams, {
    selection: {
      date: opts.date ?? ctx.selection.date,
      gamePk: opts.game !== undefined ? opts.game : ctx.selection.gamePk,
      playerName: opts.player,
      teamSide: opts.side !== undefined ? opts.side : null,
      pitcherName: opts.pitcher !== undefined ? opts.pitcher : null,
      leagueMode: opts.leagueMode ?? false,
    },
    filters: opts.filters,
    tab: opts.tab ?? 'overview',
  })

  return {
    pathname: RESEARCH_PATH,
    search: next.toString(),
  }
}

/** Shareable href — for `<Link to={…}>` or clipboard copy. */
export function buildResearchHref(
  ctx: ResearchNavigationContext,
  opts: OpenResearchOptions,
): string {
  const { pathname, search } = buildResearchNavigation(ctx, opts)
  return search ? `${pathname}?${search}` : pathname
}
