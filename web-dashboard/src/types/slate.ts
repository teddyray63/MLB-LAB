/** Matches export_json() output — do not drift from Python schema */

export type PlayCategory =
  | 'hits'
  | 'singles'
  | 'total_bases'
  | 'hrr'
  | 'home_runs'

/** Tier thresholds from export_json tier_for() */
export type Tier = 'T1' | 'T2' | 'T3'

/** Phase 0 export metadata — Data Status workspace */
export interface ExportMeta {
  generated_at: string
  statcast_start: string
  statcast_end: string
  runner_version: string
  warnings: string[]
}

/** Park factor indices (100 = league average) */
export interface ParkFactors {
  run_factor: number | null
  hit_factor: number | null
  hr_factor: number | null
}

/** How a batting order was derived in the export pipeline */
export type LineupSource = 'override' | 'projected' | 'empty'

export interface Game {
  /** Canonical stable key — MLB gamePk (Phase 0+) */
  game_pk?: number | null
  game_id: string
  away_team: string
  home_team: string
  away_sp: string
  home_sp: string
  away_sp_id: number | null
  home_sp_id: number | null
  /** ISO 8601 UTC start time from MLB Stats API */
  start_time_utc?: string | null
  /** detailedState or abstractGameState from schedule */
  status?: string | null
  venue?: string | null
}

export interface TopPlay {
  rank: number
  hitter: string
  team: string
  game: string
  game_pk?: number | null
  opp_sp: string
  pitch: string
  score: number
  tier: Tier
  key_stat: string
  key_val: number | string | null
}

/** clean_row() shape — used for category_boards and matchups */
export interface HitterRow {
  hitter: string
  team: string
  game: string
  game_pk?: number | null
  opp_sp: string
  pitch: string
  pa: number | null
  hits: number | null
  singles: number | null
  tb: number | null
  avg: number | null
  slg: number | null
  iso: number | null
  woba: number | null
  xwoba: number | null
  xba: number | null
  xslg: number | null
  sweet_spot_pct: number | null
  barrel_pct: number | null
  hard_hit_pct: number | null
  whiff_pct: number | null
  /** Avg bat speed (mph) on tracked swings — 2024+ Statcast, partial coverage */
  bat_speed?: number | null
  /** Squared-up% on tracked swings (derived) */
  squared_up_pct?: number | null
  /** Blast% on tracked swings (derived) */
  blast_pct?: number | null
  /** True when tracked swing sample is thin */
  bat_tracking_low_confidence?: boolean
  /** Near-HR count: EV≥100, LA 20–35°, not a HR */
  near_hr?: number | null
}

/** Hitter pool row inside game_details (from team_hitter_pool) */
export interface GameHitter {
  hitter: string
  pa: number | null
  avg: number | null
  slg: number | null
  iso: number | null
  woba: number | null
  xwoba: number | null
  xba: number | null
  xslg: number | null
  sweet_spot_pct: number | null
  barrel_pct: number | null
  hard_hit_pct: number | null
  bat_speed?: number | null
  squared_up_pct?: number | null
  blast_pct?: number | null
  bat_tracking_low_confidence?: boolean
}

export interface BullpenAppearance {
  reliever: string
  date: string
  ip: string | number | null
  pitches: number | null
  flagged: boolean
}

export interface PitchMixEntry {
  pitch: string
  usage_pct: number | null
}

/** Team W-L from MLB Stats API leagueRecord */
export interface TeamRecord {
  wins: number | null
  losses: number | null
  pct: string | null
}

/** Weather from MLB Stats API schedule.weather */
export interface GameWeather {
  condition: string | null
  temp: string | null
  wind: string | null
}

/** One recent game in the context strip */
export interface RecentGame {
  date: string
  opponent: string
  result: 'W' | 'L' | 'T' | string
  score: string
  is_home: boolean
}

/** Game context strip — records, last 5, weather (MLB Stats API) */
export interface GameContext {
  park?: string | null
  park_factors?: ParkFactors | null
  away_record: TeamRecord | null
  home_record: TeamRecord | null
  weather: GameWeather | null
  away_last5: RecentGame[]
  home_last5: RecentGame[]
}

/** Pitcher situation split row (Season / Home / Away / Day / Night) */
export interface PitcherSituationLine {
  split: string
  ip: number | null
  /** Runs allowed per 9 IP — Statcast proxy, not official ERA */
  ra9: number | null
  whip: number | null
  /** Opponent batting average against */
  oba: number | null
  iso: number | null
  k_pct: number | null
  k9: number | null
  hr9: number | null
  barrel_pct: number | null
}

/** Pitcher platoon split row (vs RHB / vs LHB) */
export interface PitcherPlatoonLine {
  split: string
  bf: number | null
  hr: number | null
  singles: number | null
  doubles: number | null
  triples: number | null
  bb: number | null
  oba: number | null
  slg: number | null
  iso: number | null
  barrel_pct: number | null
  hard_hit_pct: number | null
  k_pct: number | null
}

/** Expected batting order slot (lineups_override or PA fallback) */
export interface LineupBatter {
  order: number
  hitter: string
  /** R, L, or S from Statcast stand */
  hand: string | null
  status: string | null
  ab: number | null
  hits: number | null
  hr: number | null
  avg: number | null
  slg: number | null
  k_pct: number | null
  barrel_pct: number | null
  bat_speed?: number | null
  squared_up_pct?: number | null
  blast_pct?: number | null
  bat_tracking_low_confidence?: boolean
}

/** One slash-line slice from _split_line() — overall / vs LHP / vs RHP / BVP / day / night */
export interface SplitLine {
  pa: number | null
  ab: number | null
  hits: number | null
  hr: number | null
  avg: number | null
  slg: number | null
  iso: number | null
  woba: number | null
  babip: number | null
  k_pct: number | null
  bb_pct: number | null
  hard_hit_pct: number | null
  barrel_pct: number | null
  /** True when PA below export threshold (default 20) */
  small_sample?: boolean
  bat_speed?: number | null
  squared_up_pct?: number | null
  blast_pct?: number | null
  bat_tracking_low_confidence?: boolean
}

/** Extended hitter split line with xStats — used in player_day_night_splits */
export interface HitterFullSplitLine extends SplitLine {
  xwoba?: number | null
  xba?: number | null
  xslg?: number | null
  sweet_spot_pct?: number | null
  whiff_pct?: number | null
}

/** Overall + day/night profile for one hitter */
export interface HitterDayNightProfile {
  overall: HitterFullSplitLine
  day_split: HitterFullSplitLine
  night_split: HitterFullSplitLine
}

/** Pitcher day/night split (RA/9 proxy, not official ERA) */
export interface PitcherDayNightSplit {
  ip: number | null
  ra9: number | null
  whip: number | null
  oba: number | null
  iso: number | null
  k_pct: number | null
  k9: number | null
  hr9: number | null
  barrel_pct: number | null
  bf?: number | null
  small_sample?: boolean
}

export interface PitcherDayNightProfile {
  day_split: PitcherDayNightSplit
  night_split: PitcherDayNightSplit
}

/** Per-hitter platoon + batter-vs-pitcher splits (from team_hitter_splits) */
export interface SplitHitter {
  hitter: string
  /** Opposing starter this hitter faces today (BVP target) */
  bvp_pitcher: string
  overall: SplitLine
  vs_lhp: SplitLine
  vs_rhp: SplitLine
  /** Null when no window sample vs today's starter */
  bvp: SplitLine | null
  /** Day-game split (MLB Stats API dayNight joined on game_pk) */
  day_split?: SplitLine
  /** Night-game split */
  night_split?: SplitLine
}

export interface GameDetail {
  game_pk?: number | null
  game_id: string
  away_team: string
  home_team: string
  away_sp: string
  home_sp: string
  start_time_utc?: string | null
  status?: string | null
  venue?: string | null
  away_hitters: GameHitter[]
  home_hitters: GameHitter[]
  /** Prefer {pitch, usage_pct}[]; older exports may be bare pitch-code strings */
  away_pitch_mix: Array<PitchMixEntry | string>
  home_pitch_mix: Array<PitchMixEntry | string>
  away_bullpen: BullpenAppearance[]
  home_bullpen: BullpenAppearance[]
  /** Platoon/BVP splits — additive, may be absent in older exports */
  away_splits?: SplitHitter[]
  home_splits?: SplitHitter[]
  /** Expected batting order (replaces pool display in Game Hub) */
  away_lineup?: LineupBatter[]
  home_lineup?: LineupBatter[]
  /** How away/home lineups were derived (Phase 0+) */
  away_lineup_source?: LineupSource
  home_lineup_source?: LineupSource
  /** Starter situation splits (Season/Home/Away/Day/Night) */
  away_sp_situation?: PitcherSituationLine[]
  home_sp_situation?: PitcherSituationLine[]
  /** Starter platoon splits (vs RHB/LHB) */
  away_sp_platoon?: PitcherPlatoonLine[]
  home_sp_platoon?: PitcherPlatoonLine[]
  /** Records, last 5, weather */
  context?: GameContext
  /** Starter day/night splits (explicit objects alongside situation table) */
  away_sp_day_night?: PitcherDayNightProfile
  home_sp_day_night?: PitcherDayNightProfile
  /** Cumulative runs allowed by inning checkpoint — last 5 starts */
  away_sp_inning_splits?: SpInningStart[]
  home_sp_inning_splits?: SpInningStart[]
}

/** Per-zone contact rate heatmap (Statcast zones 1–9 + 11–14) */
export interface ZoneHeatmapCell {
  zone: number
  contact_rate: number | null
  hard_hit_pct: number | null
  swings: number
  pitches: number
}

export interface ZoneHeatmapProfile {
  metric: 'contact_rate'
  zones: ZoneHeatmapCell[]
}

/** Aggregated batted-ball profile (spray + trajectory + distance) */
export interface BattedBallProfile {
  bbe: number
  pull_pct: number | null
  straight_pct: number | null
  oppo_pct: number | null
  gb_pct: number | null
  ld_pct: number | null
  fb_pct: number | null
  avg_dist: number | null
  dist_300_plus: number
  dist_350_plus: number
}

/** One SP start with cumulative runs allowed through F1/F3/F5/F7 */
export interface SpInningStart {
  date: string
  game_pk: number
  f1: number | null
  f3: number | null
  f5: number | null
  f7: number | null
}

export interface BattedBall {
  date: string
  /** Exit velocity (mph) */
  ev: number | null
  /** Launch angle (deg) */
  la: number | null
  /** Hit distance (ft) */
  dist: number | null
  /** Statcast events value: single, double, home_run, field_out, … */
  result: string
  barrel: boolean
  pitch: string | null
}

export interface GameLogEntry {
  date: string
  pa: number | null
  hits: number | null
  singles: number | null
  tb: number | null
  hr: number | null
  avg_ev: number | null
  barrels: number | null
}

export interface DailyExport {
  date: string
  /** Export pipeline metadata (Phase 0+) */
  export_meta?: ExportMeta
  games: Game[]
  top_plays: Record<PlayCategory, TopPlay[]>
  category_boards: Record<PlayCategory, HitterRow[]>
  matchups: HitterRow[]
  game_details: GameDetail[]
  /** Per-game logs for hitters in top_plays / category_boards */
  player_logs?: Record<string, GameLogEntry[]>
  /** Per-batted-ball rows for the same hitter set as player_logs */
  batted_balls?: Record<string, BattedBall[]>
  /** Spray/trajectory/distance profiles for batted_balls hitters */
  batted_ball_profiles?: Record<string, BattedBallProfile>
  /** Overall + day/night splits for matchups hitters */
  player_day_night_splits?: Record<string, HitterDayNightProfile>
  /** 13-zone contact-rate heatmaps for matchups hitters */
  player_zone_heatmaps?: Record<string, ZoneHeatmapProfile>
}

export const PLAY_CATEGORIES: PlayCategory[] = [
  'hits',
  'singles',
  'total_bases',
  'hrr',
  'home_runs',
]

export const CATEGORY_LABELS: Record<PlayCategory, string> = {
  hits: 'Hits',
  singles: 'Singles',
  total_bases: 'Total Bases',
  hrr: 'HRR',
  home_runs: 'Home Runs',
}
