import type { FilterOverride, SelectionOverride, SituationKey, TimeframeKey } from '../types/research'
import { RESEARCH_SCHEMA_VERSION } from '../types/research'

/** URL query keys for research context (Phase A+). */
export const URL_KEYS = {
  schemaVersion: 'v',
  date: 'date',
  game: 'game',
  side: 'side',
  player: 'player',
  pitcher: 'pitcher',
  league: 'league',
  timeframe: 'tf',
  situation: 'sit',
  pitch: 'pitch',
  tab: 'tab',
  scope: 'scope',
} as const

export function parseSearchParams(search: string): URLSearchParams {
  return new URLSearchParams(search)
}

export function readSelectionFromUrl(params: URLSearchParams): {
  date: string | null
  gamePk: number | null
  teamSide: 'away' | 'home' | null
  playerName: string | null
  pitcherName: string | null
  leagueMode: boolean
  schemaVersion: number | null
} {
  const v = params.get(URL_KEYS.schemaVersion)
  const gameRaw = params.get(URL_KEYS.game)
  const side = params.get(URL_KEYS.side)
  return {
    schemaVersion: v ? Number(v) : null,
    date: params.get(URL_KEYS.date),
    gamePk: gameRaw ? Number(gameRaw) : null,
    teamSide: side === 'away' || side === 'home' ? side : null,
    playerName: params.get(URL_KEYS.player),
    pitcherName: params.get(URL_KEYS.pitcher),
    leagueMode: params.get(URL_KEYS.league) === '1',
  }
}

export function readFiltersFromUrl(params: URLSearchParams): {
  timeframe: string | null
  situation: string | null
  pitchType: string | null
} {
  return {
    timeframe: params.get(URL_KEYS.timeframe),
    situation: params.get(URL_KEYS.situation),
    pitchType: params.get(URL_KEYS.pitch),
  }
}

export function buildSearchParamsPatch(
  current: URLSearchParams,
  patch: {
    selection?: SelectionOverride
    filters?: FilterOverride
    tab?: string | null
    scope?: string | null
  },
): URLSearchParams {
  const next = new URLSearchParams(current)
  next.set(URL_KEYS.schemaVersion, String(RESEARCH_SCHEMA_VERSION))

  if (patch.selection) {
    const s = patch.selection
    if (s.date !== undefined) {
      if (s.date) next.set(URL_KEYS.date, s.date)
      else next.delete(URL_KEYS.date)
    }
    if (s.gamePk !== undefined) {
      if (s.gamePk != null) next.set(URL_KEYS.game, String(s.gamePk))
      else next.delete(URL_KEYS.game)
    }
    if (s.teamSide !== undefined) {
      if (s.teamSide) next.set(URL_KEYS.side, s.teamSide)
      else next.delete(URL_KEYS.side)
    }
    if (s.playerName !== undefined) {
      if (s.playerName) next.set(URL_KEYS.player, s.playerName)
      else next.delete(URL_KEYS.player)
    }
    if (s.pitcherName !== undefined) {
      if (s.pitcherName) next.set(URL_KEYS.pitcher, s.pitcherName)
      else next.delete(URL_KEYS.pitcher)
    }
    if (s.leagueMode !== undefined) {
      if (s.leagueMode) next.set(URL_KEYS.league, '1')
      else next.delete(URL_KEYS.league)
    }
  }

  if (patch.filters) {
    const f = patch.filters
    if (f.timeframe !== undefined) {
      if (f.timeframe) next.set(URL_KEYS.timeframe, f.timeframe)
      else next.delete(URL_KEYS.timeframe)
    }
    if (f.situation !== undefined) {
      if (f.situation) next.set(URL_KEYS.situation, f.situation)
      else next.delete(URL_KEYS.situation)
    }
    if (f.pitchType !== undefined) {
      if (f.pitchType) next.set(URL_KEYS.pitch, f.pitchType)
      else next.delete(URL_KEYS.pitch)
    }
  }

  if (patch.tab !== undefined) {
    if (patch.tab) next.set(URL_KEYS.tab, patch.tab)
    else next.delete(URL_KEYS.tab)
  }

  if (patch.scope !== undefined) {
    if (patch.scope) next.set(URL_KEYS.scope, patch.scope)
    else next.delete(URL_KEYS.scope)
  }

  return next
}

export function searchParamsEqual(a: URLSearchParams, b: URLSearchParams): boolean {
  return a.toString() === b.toString()
}

export function selectionToUrlValues(selection: {
  date: string
  gamePk: number | null
  teamSide: 'away' | 'home' | null
  playerName: string | null
  pitcherName: string | null
  leagueMode: boolean
}): SelectionOverride {
  return {
    date: selection.date,
    gamePk: selection.gamePk,
    teamSide: selection.teamSide,
    playerName: selection.playerName,
    pitcherName: selection.pitcherName,
    leagueMode: selection.leagueMode,
  }
}

export function filtersToUrlValues(filters: {
  timeframe: TimeframeKey
  situation: SituationKey
  pitchType: string | null
}): FilterOverride {
  return {
    timeframe: filters.timeframe,
    situation: filters.situation,
    pitchType: filters.pitchType,
  }
}
