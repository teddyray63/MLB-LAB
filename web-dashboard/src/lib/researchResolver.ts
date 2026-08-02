import type { DailyExport, Game, GameDetail, LineupBatter } from '../types/slate'
import type {
  PitcherRef,
  PlayerRef,
  ResolvedResearchSelection,
  SelectionOverride,
  TeamSide,
} from '../types/research'
import { RESEARCH_SCHEMA_VERSION } from '../types/research'

export interface RawSelectionInput {
  date?: string | null
  gamePk?: number | null
  teamSide?: TeamSide | null
  playerName?: string | null
  pitcherName?: string | null
  leagueMode?: boolean
}

function pitcherRef(name: string | null | undefined, id: number | null | undefined): PitcherRef | null {
  if (!name || name === 'TBD') return null
  return { name, id: id ?? null }
}

function findGameDetail(exportData: DailyExport, gamePk: number): GameDetail | null {
  return exportData.game_details?.find((g) => g.game_pk === gamePk) ?? null
}

function findGameSummary(exportData: DailyExport, gamePk: number): Game | null {
  return exportData.games?.find((g) => g.game_pk === gamePk) ?? null
}

export function firstValidGamePk(exportData: DailyExport): number | null {
  for (const g of exportData.games ?? []) {
    if (g.game_pk != null) return g.game_pk
  }
  for (const g of exportData.game_details ?? []) {
    if (g.game_pk != null) return g.game_pk
  }
  return null
}

function lineupPlayers(detail: GameDetail, side: TeamSide): PlayerRef[] {
  const lineup: LineupBatter[] =
    side === 'away' ? (detail.away_lineup ?? []) : (detail.home_lineup ?? [])
  const team = side === 'away' ? detail.away_team : detail.home_team

  if (lineup.length) {
    return lineup.map((slot) => ({
      name: slot.hitter,
      team,
      side,
      lineupOrder: slot.order,
      hand: slot.hand,
    }))
  }

  const pool = side === 'away' ? detail.away_hitters : detail.home_hitters
  return (pool ?? []).map((h, i) => ({
    name: h.hitter,
    team,
    side,
    lineupOrder: i + 1,
    hand: null,
  }))
}

function gamePlayerList(detail: GameDetail): PlayerRef[] {
  return [...lineupPlayers(detail, 'away'), ...lineupPlayers(detail, 'home')]
}

function normalizeName(name: string): string {
  return name.trim().toLowerCase()
}

function findPlayerInGame(
  detail: GameDetail,
  playerName: string,
): PlayerRef | null {
  const key = normalizeName(playerName)
  return gamePlayerList(detail).find((p) => normalizeName(p.name) === key) ?? null
}

function inferSideFromMatchups(
  exportData: DailyExport,
  playerName: string,
  gamePk: number | null,
): TeamSide | null {
  const key = normalizeName(playerName)
  for (const row of exportData.matchups ?? []) {
    if (normalizeName(row.hitter) !== key) continue
    if (gamePk != null && row.game_pk != null && row.game_pk !== gamePk) continue
    const detail =
      gamePk != null
        ? findGameDetail(exportData, gamePk)
        : exportData.game_details?.find((g) => g.game_id === row.game)
    if (!detail) continue
    if (row.team === detail.home_team) return 'home'
    if (row.team === detail.away_team) return 'away'
  }
  return null
}

function opposingPitcherForSide(detail: GameDetail, side: TeamSide): PitcherRef | null {
  if (side === 'home') {
    return pitcherRef(detail.away_sp, null)
  }
  return pitcherRef(detail.home_sp, null)
}

function resolvePitcherWithIds(
  summary: Game | null,
  detail: GameDetail,
  side: TeamSide,
): PitcherRef | null {
  if (side === 'home') {
    return pitcherRef(
      detail.home_sp,
      summary?.home_sp_id ?? null,
    )
  }
  return pitcherRef(detail.away_sp, summary?.away_sp_id ?? null)
}

/**
 * Central selection resolver.
 * Precedence: URL/raw input → context override → export defaults → safe fallback.
 */
export function resolveResearchSelection(
  exportData: DailyExport,
  raw: RawSelectionInput,
  override: SelectionOverride = {},
): ResolvedResearchSelection {
  const warnings: string[] = []

  // 1–3: Date
  const date = raw.date ?? override.date ?? exportData.date

  // Schema version check (URL may carry stale v= param — warn only)
  // game pk resolution
  let gamePk =
    raw.gamePk ??
    override.gamePk ??
    (exportData.games?.[0]?.game_pk ?? null)

  if (gamePk == null) {
    gamePk = firstValidGamePk(exportData)
    if (gamePk != null) {
      warnings.push('No game in URL — defaulted to first slate game')
    }
  }

  let detail = gamePk != null ? findGameDetail(exportData, gamePk) : null
  let summary = gamePk != null ? findGameSummary(exportData, gamePk) : null

  if (gamePk != null && !detail) {
    warnings.push(`game_pk ${gamePk} not found in export — using fallback`)
    gamePk = firstValidGamePk(exportData)
    detail = gamePk != null ? findGameDetail(exportData, gamePk) : null
    summary = gamePk != null ? findGameSummary(exportData, gamePk) : null
  }

  const awayTeam = detail?.away_team ?? summary?.away_team ?? null
  const homeTeam = detail?.home_team ?? summary?.home_team ?? null

  const awaySp = detail
    ? pitcherRef(detail.away_sp, summary?.away_sp_id ?? null)
    : summary
      ? pitcherRef(summary.away_sp, summary.away_sp_id)
      : null
  const homeSp = detail
    ? pitcherRef(detail.home_sp, summary?.home_sp_id ?? null)
    : summary
      ? pitcherRef(summary.home_sp, summary.home_sp_id)
      : null

  const leagueMode = raw.leagueMode ?? override.leagueMode ?? false

  // Player resolution
  const playerName = raw.playerName ?? override.playerName ?? null
  let teamSide: TeamSide | null = raw.teamSide ?? override.teamSide ?? null
  let player: PlayerRef | null = null

  if (playerName && detail && !leagueMode) {
    player = findPlayerInGame(detail, playerName)
    if (!player) {
      const inferred = inferSideFromMatchups(exportData, playerName, gamePk)
      if (inferred) {
        teamSide = inferred
        const team = inferred === 'home' ? detail.home_team : detail.away_team
        player = { name: playerName, team, side: inferred }
        warnings.push(`Player not in lineup — matched via matchups (${team})`)
      } else {
        warnings.push(`Player "${playerName}" not found in selected game`)
      }
    } else {
      teamSide = player.side
    }
  } else if (playerName && leagueMode) {
    const row = exportData.matchups?.find(
      (r) => normalizeName(r.hitter) === normalizeName(playerName),
    )
    if (row) {
      teamSide =
        teamSide ??
        (row.team === homeTeam ? 'home' : row.team === awayTeam ? 'away' : null) ??
        'home'
      player = {
        name: row.hitter,
        team: row.team,
        side: teamSide ?? 'home',
      }
    } else {
      warnings.push(`Player "${playerName}" not found in export matchups`)
    }
  }

  // Pitcher resolution
  const pitcherName = raw.pitcherName ?? override.pitcherName ?? null
  let pitcher: PitcherRef | null = null
  let opposingPitcher: PitcherRef | null = null

  if (detail && teamSide) {
    opposingPitcher = opposingPitcherForSide(detail, teamSide)
    if (summary) {
      opposingPitcher = resolvePitcherWithIds(
        summary,
        detail,
        teamSide === 'home' ? 'away' : 'home',
      )
    }
  }

  if (pitcherName) {
    pitcher = pitcherRef(pitcherName, null)
  } else if (opposingPitcher) {
    pitcher = opposingPitcher
  }

  return {
    schemaVersion: RESEARCH_SCHEMA_VERSION,
    date,
    gamePk,
    awayTeam,
    homeTeam,
    awaySp,
    homeSp,
    teamSide,
    player,
    pitcher,
    opposingPitcher,
    leagueMode,
    warnings,
  }
}

/** Players available for the selected game (lineup-first). */
export function listGamePlayers(exportData: DailyExport, gamePk: number | null): PlayerRef[] {
  if (gamePk == null) return []
  const detail = findGameDetail(exportData, gamePk)
  if (!detail) return []
  return gamePlayerList(detail)
}

/** All games on the export slate keyed by game_pk. */
export function listSlateGames(exportData: DailyExport): Game[] {
  return exportData.games ?? []
}

export function gameLabel(game: Game): string {
  return game.game_id || `${game.away_team} @ ${game.home_team}`
}

export function matchupLabel(
  selection: Pick<
    ResolvedResearchSelection,
    'awaySp' | 'homeSp' | 'pitcher' | 'player' | 'awayTeam' | 'homeTeam'
  >,
): string | null {
  if (selection.player && selection.pitcher) {
    return `${selection.pitcher.name} vs ${selection.player.name}`
  }
  if (selection.awaySp && selection.homeSp) {
    return `${selection.awaySp.name} vs ${selection.homeSp.name}`
  }
  if (selection.awayTeam && selection.homeTeam) {
    return `${selection.awayTeam} @ ${selection.homeTeam}`
  }
  return null
}
