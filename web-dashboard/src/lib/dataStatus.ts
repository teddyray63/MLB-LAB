import type { DailyExport, Game, GameDetail } from '../types/slate'
import { isValidSlateGame } from './leaderboardData'

export type PipelineStatus = 'loaded' | 'partial' | 'missing'

export interface CoverageMetric {
  label: string
  present: number
  total: number
  detail?: string
}

export interface DuplicateGamePk {
  gamePk: number
  count: number
  entries: Pick<Game, 'game_id' | 'away_team' | 'home_team' | 'away_sp' | 'home_sp'>[]
}

export interface PipelineItem {
  label: string
  status: PipelineStatus
  detail: string
}

export interface DataStatusSnapshot {
  slateDate: string
  generatedAt: string | null
  runnerVersion: string | null
  exportSchemaVersion: string | null
  appSchemaVersion: number
  statcastWindow: string | null
  exportAgeDays: number | null
  exportAgeLabel: string
  isStale: boolean
  coverage: CoverageMetric[]
  pipeline: PipelineItem[]
  duplicateGamePks: DuplicateGamePk[]
  exportWarnings: string[]
  derivedWarnings: string[]
  allWarnings: string[]
  batTrackingLowConfidence: { count: number; total: number }
  filterContextNote: string
}

function hasParkFactors(detail: GameDetail): boolean {
  const pf = detail.context?.park_factors
  if (!pf) return false
  return pf.run_factor != null || pf.hit_factor != null || pf.hr_factor != null
}

function hasLineup(detail: GameDetail): boolean {
  return Boolean(detail.away_lineup?.length && detail.home_lineup?.length)
}

function hasPitchMix(detail: GameDetail): boolean {
  return Boolean(detail.away_pitch_mix?.length && detail.home_pitch_mix?.length)
}

function ratioStatus(present: number, total: number): PipelineStatus {
  if (total <= 0) return 'missing'
  if (present >= total) return 'loaded'
  if (present > 0) return 'partial'
  return 'missing'
}

function parseExportDate(iso: string | undefined | null): Date | null {
  if (!iso) return null
  const d = new Date(iso)
  return Number.isNaN(d.getTime()) ? null : d
}

function formatAge(days: number | null): string {
  if (days == null) return 'Unknown'
  if (days <= 0) return 'Today'
  if (days === 1) return '1 day old'
  return `${days} days old`
}

/** Derive duplicate game_pk groups from the games[] slate array. */
export function findDuplicateGamePks(games: Game[]): DuplicateGamePk[] {
  const byPk = new Map<number, Game[]>()
  for (const game of games) {
    const pk = game.game_pk
    if (pk == null) continue
    const list = byPk.get(pk) ?? []
    list.push(game)
    byPk.set(pk, list)
  }

  const duplicates: DuplicateGamePk[] = []
  for (const [gamePk, entries] of byPk) {
    if (entries.length <= 1) continue
    duplicates.push({
      gamePk,
      count: entries.length,
      entries: entries.map((g) => ({
        game_id: g.game_id,
        away_team: g.away_team,
        home_team: g.home_team,
        away_sp: g.away_sp,
        home_sp: g.home_sp,
      })),
    })
  }
  return duplicates.sort((a, b) => a.gamePk - b.gamePk)
}

export function buildDataStatusSnapshot(
  exportData: DailyExport,
  appSchemaVersion: number,
  selectedPlayerName: string | null,
): DataStatusSnapshot {
  const meta = exportData.export_meta
  const games = exportData.games ?? []
  const details = exportData.game_details ?? []
  const matchups = exportData.matchups ?? []
  const totalGames = Math.max(games.length, details.length)

  const gamePkPresent = games.filter((g) => g.game_pk != null).length
  const validSlateCount = games.filter((g) => g.game_pk != null && isValidSlateGame(g)).length
  const lineupCount = details.filter(hasLineup).length
  const spCount = games.filter(
    (g) => g.away_sp && g.home_sp && g.away_sp !== 'TBD' && g.home_sp !== 'TBD',
  ).length
  const parkFactorCount = details.filter(hasParkFactors).length
  const pitchMixCount = details.filter(hasPitchMix).length
  const zoneHeatmapCount = Object.keys(exportData.player_zone_heatmaps ?? {}).length
  const playerLogCount = Object.keys(exportData.player_logs ?? {}).length
  const battedBallProfileCount = Object.keys(exportData.batted_ball_profiles ?? {}).length
  const batSpeedCount = matchups.filter((r) => r.bat_speed != null).length
  const lowConfCount = matchups.filter((r) => r.bat_tracking_low_confidence).length

  const generatedAt = meta?.generated_at ?? null
  const generatedDate = parseExportDate(generatedAt)
  const now = new Date()
  let exportAgeDays: number | null = null
  if (generatedDate) {
    exportAgeDays = Math.floor(
      (now.getTime() - generatedDate.getTime()) / (1000 * 60 * 60 * 24),
    )
  }

  const statcastWindow =
    meta?.statcast_start && meta?.statcast_end
      ? `${meta.statcast_start} – ${meta.statcast_end}`
      : null

  const duplicateGamePks = findDuplicateGamePks(games)
  const exportWarnings = [...(meta?.warnings ?? [])]

  const derivedWarnings: string[] = []
  if (duplicateGamePks.length) {
    for (const dup of duplicateGamePks) {
      derivedWarnings.push(
        `Duplicate game_pk ${dup.gamePk} appears ${dup.count} times in games[]`,
      )
    }
  }
  if (parkFactorCount < totalGames && totalGames > 0) {
    derivedWarnings.push(
      `Park factors missing for ${totalGames - parkFactorCount}/${totalGames} games`,
    )
  }
  if (exportAgeDays != null && exportAgeDays > 1) {
    derivedWarnings.push(
      `Export is ${formatAge(exportAgeDays)} (slate date ${exportData.date})`,
    )
  }
  if (lowConfCount > 0) {
    derivedWarnings.push(
      `${lowConfCount}/${matchups.length} matchup rows flagged bat_tracking_low_confidence`,
    )
  }

  const uniqueHitterCount = new Set(matchups.map((r) => r.hitter)).size

  const coverage: CoverageMetric[] = [
    {
      label: 'Games (game_pk)',
      present: gamePkPresent,
      total: games.length,
      detail: `${validSlateCount} valid slate entries (non-TBD SPs)`,
    },
    {
      label: 'Lineups',
      present: lineupCount,
      total: details.length || totalGames,
      detail: 'From game_details away_lineup + home_lineup',
    },
    {
      label: 'Probable SPs',
      present: spCount,
      total: games.length,
    },
    {
      label: 'Park factors',
      present: parkFactorCount,
      total: details.length || totalGames,
      detail: 'Non-null run/hit/hr in context.park_factors',
    },
    {
      label: 'Zone heatmaps',
      present: zoneHeatmapCount,
      total: uniqueHitterCount,
      detail: 'player_zone_heatmaps vs unique matchup hitters',
    },
    {
      label: 'Bat tracking',
      present: batSpeedCount,
      total: matchups.length,
      detail: `${lowConfCount} low-confidence rows`,
    },
    {
      label: 'Player logs',
      present: playerLogCount,
      total: uniqueHitterCount,
      detail: 'Top-board hitters with game logs',
    },
    {
      label: 'Batted-ball profiles',
      present: battedBallProfileCount,
      total: uniqueHitterCount,
    },
    {
      label: 'Pitch mix',
      present: pitchMixCount,
      total: details.length || totalGames,
      detail: 'Both away and home SP mix present',
    },
    {
      label: 'Matchup rows',
      present: matchups.length,
      total: matchups.length,
    },
  ]

  const pipeline: PipelineItem[] = [
    {
      label: 'Games',
      status: ratioStatus(gamePkPresent, games.length),
      detail: `${gamePkPresent}/${games.length} with game_pk`,
    },
    {
      label: 'Lineups',
      status: ratioStatus(lineupCount, details.length),
      detail: `${lineupCount}/${details.length} games with both lineups`,
    },
    {
      label: 'Statcast',
      status:
        matchups.length > 0 && statcastWindow ? 'loaded' : matchups.length > 0 ? 'partial' : 'missing',
      detail: statcastWindow
        ? `${matchups.length} matchup rows · ${statcastWindow}`
        : `${matchups.length} matchup rows`,
    },
    {
      label: 'Pitch tracking',
      status: ratioStatus(pitchMixCount, details.length),
      detail: `${pitchMixCount}/${details.length} games with SP pitch mix`,
    },
    {
      label: 'Park factors',
      status: ratioStatus(parkFactorCount, details.length),
      detail: `${parkFactorCount}/${details.length} games with mapped park factors`,
    },
    {
      label: 'Zone data',
      status: ratioStatus(zoneHeatmapCount, uniqueHitterCount),
      detail: `${zoneHeatmapCount}/${uniqueHitterCount} hitters with zone heatmaps`,
    },
    {
      label: 'Bat tracking',
      status: ratioStatus(batSpeedCount, matchups.length),
      detail: `${batSpeedCount}/${matchups.length} rows with bat_speed · ${lowConfCount} low-confidence`,
    },
  ]

  const exportSchemaRaw = (exportData as DailyExport & { schema_version?: unknown })
    .schema_version
  const exportSchemaVersion =
    exportSchemaRaw != null ? String(exportSchemaRaw) : null

  const filterContextNote = selectedPlayerName
    ? `Filter matrix reflects selected player: ${selectedPlayerName}`
    : 'Filter matrix reflects no player selected — Last N timeframes require a player with game logs'

  return {
    slateDate: exportData.date,
    generatedAt,
    runnerVersion: meta?.runner_version ?? null,
    exportSchemaVersion,
    appSchemaVersion,
    statcastWindow,
    exportAgeDays,
    exportAgeLabel: formatAge(exportAgeDays),
    isStale: exportAgeDays != null && exportAgeDays > 1,
    coverage,
    pipeline,
    duplicateGamePks,
    exportWarnings,
    derivedWarnings,
    allWarnings: [...exportWarnings, ...derivedWarnings],
    batTrackingLowConfidence: { count: lowConfCount, total: matchups.length },
    filterContextNote,
  }
}
