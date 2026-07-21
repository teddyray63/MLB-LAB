import {
  createContext,
  useCallback,
  useContext,
  useMemo,
  type ReactNode,
} from 'react'
import { useNavigate, useSearchParams } from 'react-router-dom'
import { useExport } from './ExportContext'
import {
  buildResearchNavigation,
  type OpenResearchOptions,
} from '../lib/researchNavigation'
import {
  buildSearchParamsPatch,
  readFiltersFromUrl,
  readSelectionFromUrl,
  searchParamsEqual,
} from '../lib/researchUrl'
import { resolveFilters } from '../lib/filterSupport'
import {
  listGamePlayers,
  listSlateGames,
  resolveResearchSelection,
  gameLabel,
  matchupLabel,
} from '../lib/researchResolver'
import type { Game } from '../types/slate'
import type {
  FilterOverride,
  PlayerRef,
  ResolvedFilters,
  ResolvedResearchSelection,
  SelectionOverride,
  SituationKey,
  TeamSide,
  TimeframeKey,
} from '../types/research'
import { RESEARCH_SCHEMA_VERSION } from '../types/research'

export interface GameContextValue {
  schemaVersion: typeof RESEARCH_SCHEMA_VERSION
  selection: ResolvedResearchSelection
  slateGames: Game[]
  gamePlayers: PlayerRef[]
  gameLabel: (game: Game) => string
  matchupLabel: string | null
  setDate: (date: string) => void
  setGame: (gamePk: number) => void
  setTeamSide: (side: TeamSide) => void
  setPlayer: (name: string, side?: TeamSide) => void
  setPitcher: (name: string) => void
  setLeagueMode: (enabled: boolean) => void
  openResearch: (opts: OpenResearchOptions) => void
}

const GameContext = createContext<GameContextValue | null>(null)

export function GameContextProvider({ children }: { children: ReactNode }) {
  const exportData = useExport()
  const [searchParams, setSearchParams] = useSearchParams()
  const navigate = useNavigate()

  const paramString = searchParams.toString()
  const urlSelection = useMemo(() => readSelectionFromUrl(searchParams), [paramString])

  const selection = useMemo(() => {
    const resolved = resolveResearchSelection(exportData, {
      date: urlSelection.date,
      gamePk: Number.isFinite(urlSelection.gamePk) ? urlSelection.gamePk : null,
      teamSide: urlSelection.teamSide,
      playerName: urlSelection.playerName,
      pitcherName: urlSelection.pitcherName,
      leagueMode: urlSelection.leagueMode,
    })
    if (
      urlSelection.schemaVersion != null &&
      urlSelection.schemaVersion !== RESEARCH_SCHEMA_VERSION
    ) {
      return {
        ...resolved,
        warnings: [
          ...resolved.warnings,
          `URL schema v${urlSelection.schemaVersion} differs from app v${RESEARCH_SCHEMA_VERSION}`,
        ],
      }
    }
    return resolved
  }, [exportData, urlSelection])

  const slateGames = useMemo(() => listSlateGames(exportData), [exportData])
  const gamePlayers = useMemo(
    () => listGamePlayers(exportData, selection.gamePk),
    [exportData, selection.gamePk],
  )

  const applySelection = useCallback(
    (patch: SelectionOverride, replace = false) => {
      const next = buildSearchParamsPatch(searchParams, { selection: patch })
      if (!searchParamsEqual(searchParams, next)) {
        setSearchParams(next, { replace })
      }
    },
    [searchParams, setSearchParams],
  )

  const setDate = useCallback(
    (date: string) => applySelection({ date }),
    [applySelection],
  )

  const setGame = useCallback(
    (gamePk: number) => {
      applySelection({
        gamePk,
        playerName: null,
        teamSide: null,
        pitcherName: null,
      })
    },
    [applySelection],
  )

  const setTeamSide = useCallback(
    (side: TeamSide) => applySelection({ teamSide: side }),
    [applySelection],
  )

  const setPlayer = useCallback(
    (name: string, side?: TeamSide) => {
      applySelection({
        playerName: name,
        teamSide: side ?? null,
        leagueMode: false,
      })
    },
    [applySelection],
  )

  const setPitcher = useCallback(
    (name: string) => applySelection({ pitcherName: name }),
    [applySelection],
  )

  const setLeagueMode = useCallback(
    (enabled: boolean) => {
      applySelection({
        leagueMode: enabled,
        ...(enabled ? {} : { playerName: null }),
      })
    },
    [applySelection],
  )

  const openResearch = useCallback(
    (opts: OpenResearchOptions) => {
      const target = buildResearchNavigation(
        { currentParams: searchParams, selection },
        opts,
      )
      navigate(target)
    },
    [navigate, searchParams, selection],
  )

  const value = useMemo<GameContextValue>(
    () => ({
      schemaVersion: RESEARCH_SCHEMA_VERSION,
      selection,
      slateGames,
      gamePlayers,
      gameLabel,
      matchupLabel: matchupLabel(selection),
      setDate,
      setGame,
      setTeamSide,
      setPlayer,
      setPitcher,
      setLeagueMode,
      openResearch,
    }),
    [
      selection,
      slateGames,
      gamePlayers,
      setDate,
      setGame,
      setTeamSide,
      setPlayer,
      setPitcher,
      setLeagueMode,
      openResearch,
    ],
  )

  return <GameContext.Provider value={value}>{children}</GameContext.Provider>
}

export function useGameContext(): GameContextValue {
  const ctx = useContext(GameContext)
  if (!ctx) {
    throw new Error('useGameContext must be used within GameContextProvider')
  }
  return ctx
}

/** Safe hook for legacy-adjacent code — returns null outside provider (should not happen after Phase A). */
export function useOptionalGameContext(): GameContextValue | null {
  return useContext(GameContext)
}

export interface FilterContextValue {
  schemaVersion: typeof RESEARCH_SCHEMA_VERSION
  filters: ResolvedFilters
  setTimeframe: (tf: TimeframeKey) => void
  setSituation: (sit: SituationKey) => void
  setPitchType: (code: string | null) => void
}

const FilterContext = createContext<FilterContextValue | null>(null)

export function FilterContextProvider({ children }: { children: ReactNode }) {
  const exportData = useExport()
  const { selection } = useGameContext()
  const [searchParams, setSearchParams] = useSearchParams()

  const paramString = searchParams.toString()
  const urlFilters = useMemo(() => readFiltersFromUrl(searchParams), [paramString])

  const filters = useMemo(
    () =>
      resolveFilters(exportData, selection, {
        timeframe: urlFilters.timeframe,
        situation: urlFilters.situation,
        pitchType: urlFilters.pitchType,
      }),
    [exportData, selection, urlFilters],
  )

  const applyFilters = useCallback(
    (patch: FilterOverride) => {
      const next = buildSearchParamsPatch(searchParams, { filters: patch })
      if (!searchParamsEqual(searchParams, next)) {
        setSearchParams(next, { replace: true })
      }
    },
    [searchParams, setSearchParams],
  )

  const setTimeframe = useCallback(
    (tf: TimeframeKey) => applyFilters({ timeframe: tf }),
    [applyFilters],
  )

  const setSituation = useCallback(
    (sit: SituationKey) => applyFilters({ situation: sit }),
    [applyFilters],
  )

  const setPitchType = useCallback(
    (code: string | null) => applyFilters({ pitchType: code }),
    [applyFilters],
  )

  const value = useMemo<FilterContextValue>(
    () => ({
      schemaVersion: RESEARCH_SCHEMA_VERSION,
      filters,
      setTimeframe,
      setSituation,
      setPitchType,
    }),
    [filters, setTimeframe, setSituation, setPitchType],
  )

  return <FilterContext.Provider value={value}>{children}</FilterContext.Provider>
}

export function useFilters(): FilterContextValue {
  const ctx = useContext(FilterContext)
  if (!ctx) {
    throw new Error('useFilters must be used within FilterContextProvider')
  }
  return ctx
}

/** Nests game + filter providers (must be inside BrowserRouter + ExportProvider). */
export function ResearchProviders({ children }: { children: ReactNode }) {
  return (
    <GameContextProvider>
      <FilterContextProvider>{children}</FilterContextProvider>
    </GameContextProvider>
  )
}
