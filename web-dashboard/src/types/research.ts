/** Shared research context schema — bump when URL/context shape changes. */
export const RESEARCH_SCHEMA_VERSION = 2 as const

export type ResearchSchemaVersion = typeof RESEARCH_SCHEMA_VERSION

export type TimeframeKey = 'season' | 'l20' | 'l15' | 'l10' | 'l7' | 'l5'

export type SituationKey =
  | 'overall'
  | 'home'
  | 'away'
  | 'day'
  | 'night'
  | 'vlhp'
  | 'vrhp'
  | 'bvp'

/** Shared situation → export SplitHitter field mapping (Today + Research). */
export type SituationSplitKey =
  | 'overall'
  | 'vs_lhp'
  | 'vs_rhp'
  | 'bvp'
  | 'day_split'
  | 'night_split'

export type TeamSide = 'away' | 'home'

export interface PitcherRef {
  name: string
  id: number | null
}

export interface PlayerRef {
  name: string
  team: string
  side: TeamSide
  lineupOrder?: number | null
  hand?: string | null
}

export interface FilterSupport {
  supported: boolean
  reason?: string
  source?: 'export' | 'client-slice' | 'unsupported'
}

export interface FilterSupportMatrix {
  timeframe: Record<TimeframeKey, FilterSupport>
  situation: Record<SituationKey, FilterSupport>
  pitchType: FilterSupport
}

/** Output of the centralized selection resolver — single source of truth. */
export interface ResolvedResearchSelection {
  schemaVersion: ResearchSchemaVersion
  date: string
  gamePk: number | null
  awayTeam: string | null
  homeTeam: string | null
  awaySp: PitcherRef | null
  homeSp: PitcherRef | null
  teamSide: TeamSide | null
  player: PlayerRef | null
  pitcher: PitcherRef | null
  opposingPitcher: PitcherRef | null
  leagueMode: boolean
  warnings: string[]
}

export interface ResolvedFilters {
  schemaVersion: ResearchSchemaVersion
  timeframe: TimeframeKey
  situation: SituationKey
  pitchType: string | null
  support: FilterSupportMatrix
}

/** Partial override layer for resolver precedence (URL → context → export → fallback). */
export interface SelectionOverride {
  date?: string
  gamePk?: number | null
  teamSide?: TeamSide | null
  playerName?: string | null
  pitcherName?: string | null
  leagueMode?: boolean
}

export interface FilterOverride {
  timeframe?: TimeframeKey
  situation?: SituationKey
  pitchType?: string | null
}

export const DEFAULT_TIMEFRAME: TimeframeKey = 'season'
export const DEFAULT_SITUATION: SituationKey = 'overall'

export const TIMEFRAME_OPTIONS: { key: TimeframeKey; label: string }[] = [
  { key: 'season', label: 'Season' },
  { key: 'l20', label: 'Last 20' },
  { key: 'l15', label: 'Last 15' },
  { key: 'l10', label: 'Last 10' },
  { key: 'l7', label: 'Last 7' },
  { key: 'l5', label: 'Last 5' },
]

export const SITUATION_OPTIONS: { key: SituationKey; label: string }[] = [
  { key: 'overall', label: 'Overall' },
  { key: 'home', label: 'Home' },
  { key: 'away', label: 'Away' },
  { key: 'day', label: 'Day' },
  { key: 'night', label: 'Night' },
  { key: 'vlhp', label: 'vs LHP' },
  { key: 'vrhp', label: 'vs RHP' },
  { key: 'bvp', label: 'vs Today’s SP' },
]

export function situationToSplitKey(situation: SituationKey): SituationSplitKey {
  switch (situation) {
    case 'vlhp':
      return 'vs_lhp'
    case 'vrhp':
      return 'vs_rhp'
    case 'day':
      return 'day_split'
    case 'night':
      return 'night_split'
    case 'bvp':
      return 'bvp'
    default:
      return 'overall'
  }
}
