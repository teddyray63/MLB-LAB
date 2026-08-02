import { useMemo } from 'react'
import { useExport } from '../context/ExportContext'
import { useGameContext, useFilters } from '../context/ResearchContext'
import { useFilteredMatchupRows } from './useFilteredData'
import { lookupPlayerMap } from '../lib/playerExportLookup'
import { normalizePitchMixItems } from '../components/PitchMixFilterChips'
import type { SituationKey } from '../types/research'
import type {
  GameDetail,
  GameLogEntry,
  HitterDayNightProfile,
  HitterRow,
  PitchMixEntry,
  SplitHitter,
  SplitLine,
} from '../types/slate'

/** Weighted average of a rate stat across per-pitch matchup rows (PA-weighted). */
export function aggregateMatchupStat(
  rows: HitterRow[],
  field: keyof HitterRow,
): number | null {
  let paSum = 0
  let weighted = 0
  for (const row of rows) {
    const pa = row.pa ?? 0
    const val = row[field]
    if (pa <= 0 || val == null || typeof val !== 'number' || Number.isNaN(val)) continue
    weighted += val * pa
    paSum += pa
  }
  if (paSum <= 0) return null
  return weighted / paSum
}

function situationSplitLine(
  situation: SituationKey,
  dayNight: HitterDayNightProfile | undefined,
  teamSplit: SplitHitter | undefined,
): SplitLine | null {
  if (!dayNight && !teamSplit) return null
  switch (situation) {
    case 'day':
      return dayNight?.day_split ?? teamSplit?.day_split ?? null
    case 'night':
      return dayNight?.night_split ?? teamSplit?.night_split ?? null
    case 'vlhp':
      return teamSplit?.vs_lhp ?? null
    case 'vrhp':
      return teamSplit?.vs_rhp ?? null
    case 'overall':
    default:
      return dayNight?.overall ?? teamSplit?.overall ?? null
  }
}

function recentTrendLabel(log: GameLogEntry[] | undefined): string | null {
  if (!log?.length) return null
  const slice = log.slice(0, 5)
  const pa = slice.reduce((n, g) => n + (g.pa ?? 0), 0)
  const hits = slice.reduce((n, g) => n + (g.hits ?? 0), 0)
  const hr = slice.reduce((n, g) => n + (g.hr ?? 0), 0)
  const tb = slice.reduce((n, g) => n + (g.tb ?? 0), 0)
  if (pa <= 0) return `L${slice.length}: ${hits} H · ${hr} HR · ${tb} TB`
  return `L${slice.length}: ${(hits / pa).toFixed(3)} AVG · ${hr} HR · ${tb} TB`
}

export function useResearchPlayerData() {
  const exportData = useExport()
  const { selection } = useGameContext()
  const { filters } = useFilters()
  const matchupRows = useFilteredMatchupRows()

  const playerName = selection.player?.name ?? null

  const gameDetail = useMemo((): GameDetail | null => {
    if (selection.gamePk == null) return null
    return exportData.game_details?.find((g) => g.game_pk === selection.gamePk) ?? null
  }, [exportData.game_details, selection.gamePk])

  const opponentTeam = useMemo(() => {
    if (!gameDetail || !selection.teamSide) return null
    return selection.teamSide === 'home' ? gameDetail.away_team : gameDetail.home_team
  }, [gameDetail, selection.teamSide])

  const opposingPitchMix = useMemo((): PitchMixEntry[] => {
    if (!gameDetail || !selection.teamSide) return []
    const raw =
      selection.teamSide === 'home'
        ? gameDetail.away_pitch_mix
        : gameDetail.home_pitch_mix
    return normalizePitchMixItems(raw).map((p) => ({
      pitch: p.pitch,
      usage_pct: p.usage_pct ?? null,
    }))
  }, [gameDetail, selection.teamSide])

  const gameLog = useMemo(
    () => lookupPlayerMap(exportData.player_logs, playerName),
    [exportData.player_logs, playerName],
  )

  const dayNightProfile = useMemo(
    () => lookupPlayerMap(exportData.player_day_night_splits, playerName),
    [exportData.player_day_night_splits, playerName],
  )

  const zoneHeatmap = useMemo(
    () => lookupPlayerMap(exportData.player_zone_heatmaps, playerName),
    [exportData.player_zone_heatmaps, playerName],
  )

  const battedBalls = useMemo(
    () => lookupPlayerMap(exportData.batted_balls, playerName),
    [exportData.batted_balls, playerName],
  )

  const battedBallProfile = useMemo(
    () => lookupPlayerMap(exportData.batted_ball_profiles, playerName),
    [exportData.batted_ball_profiles, playerName],
  )

  const teamSplitHitter = useMemo((): SplitHitter | undefined => {
    if (!gameDetail || !playerName) return undefined
    const rows =
      selection.teamSide === 'home'
        ? gameDetail.home_splits
        : selection.teamSide === 'away'
          ? gameDetail.away_splits
          : [...(gameDetail.home_splits ?? []), ...(gameDetail.away_splits ?? [])]
    return rows?.find((r) => r.hitter.toLowerCase() === playerName.toLowerCase())
  }, [gameDetail, playerName, selection.teamSide])

  const activeSplitLine = useMemo(
    () => situationSplitLine(filters.situation, dayNightProfile, teamSplitHitter),
    [filters.situation, dayNightProfile, teamSplitHitter],
  )

  const pitcherMatchupRows = useMemo(() => {
    const pitcher = selection.pitcher?.name ?? selection.opposingPitcher?.name
    if (!pitcher) return matchupRows
    return matchupRows.filter(
      (r) => r.opp_sp.toLowerCase() === pitcher.toLowerCase(),
    )
  }, [matchupRows, selection.pitcher, selection.opposingPitcher])

  const aggregates = useMemo(
    () => ({
      xwoba: aggregateMatchupStat(matchupRows, 'xwoba'),
      woba: aggregateMatchupStat(matchupRows, 'woba'),
      barrelPct: aggregateMatchupStat(matchupRows, 'barrel_pct'),
      hardHitPct: aggregateMatchupStat(matchupRows, 'hard_hit_pct'),
      whiffPct: aggregateMatchupStat(matchupRows, 'whiff_pct'),
      batSpeed: aggregateMatchupStat(matchupRows, 'bat_speed'),
      squaredUpPct: aggregateMatchupStat(matchupRows, 'squared_up_pct'),
      blastPct: aggregateMatchupStat(matchupRows, 'blast_pct'),
      sweetSpotPct: aggregateMatchupStat(matchupRows, 'sweet_spot_pct'),
      iso: aggregateMatchupStat(matchupRows, 'iso'),
      avg: aggregateMatchupStat(matchupRows, 'avg'),
      slg: aggregateMatchupStat(matchupRows, 'slg'),
    }),
    [matchupRows],
  )

  const recentTrend = useMemo(() => recentTrendLabel(gameLog), [gameLog])

  const timeframeSupported = filters.support.timeframe[filters.timeframe].supported

  return {
    playerName,
    selection,
    filters,
    gameDetail,
    opponentTeam,
    opposingPitchMix,
    matchupRows,
    pitcherMatchupRows,
    gameLog,
    dayNightProfile,
    zoneHeatmap,
    battedBalls,
    battedBallProfile,
    teamSplitHitter,
    activeSplitLine,
    aggregates,
    recentTrend,
    timeframeSupported,
  }
}

export type ResearchPlayerData = ReturnType<typeof useResearchPlayerData>
