import type { DailyExport, SplitHitter } from '../types/slate'
import type {
  FilterSupportMatrix,
  ResolvedFilters,
  ResolvedResearchSelection,
  SituationKey,
  TimeframeKey,
} from '../types/research'
import {
  DEFAULT_SITUATION,
  DEFAULT_TIMEFRAME,
  RESEARCH_SCHEMA_VERSION,
} from '../types/research'

function supported(source: 'export' | 'client-slice' = 'export'): {
  supported: true
  source: typeof source
} {
  return { supported: true, source }
}

function unsupported(reason: string): { supported: false; reason: string; source: 'unsupported' } {
  return { supported: false, reason, source: 'unsupported' }
}

/** Whether the selected player has game-log data for client-side timeframe slicing. */
function playerHasGameLogs(exportData: DailyExport, playerName: string | null): boolean {
  if (!playerName) return false
  const logs = exportData.player_logs ?? {}
  if (logs[playerName]) return true
  const key = Object.keys(logs).find((k) => k.toLowerCase() === playerName.toLowerCase())
  return Boolean(key)
}

export function buildFilterSupportMatrix(
  exportData: DailyExport,
  selection: Pick<ResolvedResearchSelection, 'player' | 'gamePk'>,
): FilterSupportMatrix {
  const hasLogs = playerHasGameLogs(exportData, selection.player?.name ?? null)

  const timeframe: FilterSupportMatrix['timeframe'] = {
    season: supported('export'),
    l20: hasLogs
      ? supported('client-slice')
      : unsupported('Game logs available for top-board hitters only (Phase 0)'),
    l15: hasLogs
      ? supported('client-slice')
      : unsupported('Requires game log data for selected player'),
    l10: hasLogs
      ? supported('client-slice')
      : unsupported('Requires game log data for selected player'),
    l7: hasLogs
      ? supported('client-slice')
      : unsupported('Requires game log data for selected player'),
    l5: hasLogs
      ? supported('client-slice')
      : unsupported('Requires game log data for selected player'),
  }

  const situation: FilterSupportMatrix['situation'] = {
    overall: supported('export'),
    home: unsupported('Hitter home splits not in export — pitcher panels only'),
    away: unsupported('Hitter away splits not in export — pitcher panels only'),
    day: supported('export'),
    night: supported('export'),
    vlhp: supported('export'),
    vrhp: supported('export'),
    bvp: bvpSupported(exportData, selection)
      ? supported('export')
      : unsupported('No Statcast sample vs today’s starting pitcher'),
  }

  return {
    timeframe,
    situation,
    pitchType: supported('export'),
  }
}

export function resolveFilters(
  exportData: DailyExport,
  selection: Pick<ResolvedResearchSelection, 'player' | 'gamePk'>,
  raw: { timeframe?: string | null; situation?: string | null; pitchType?: string | null },
): ResolvedFilters {
  const support = buildFilterSupportMatrix(exportData, selection)

  let timeframe = parseTimeframe(raw.timeframe) ?? DEFAULT_TIMEFRAME
  if (!support.timeframe[timeframe].supported) {
    timeframe = DEFAULT_TIMEFRAME
  }

  let situation = parseSituation(raw.situation) ?? DEFAULT_SITUATION
  if (!support.situation[situation].supported) {
    situation = DEFAULT_SITUATION
  }

  const pitchType = raw.pitchType?.trim().toUpperCase() || null

  return {
    schemaVersion: RESEARCH_SCHEMA_VERSION,
    timeframe,
    situation,
    pitchType,
    support,
  }
}

const TIMEFRAME_KEYS: TimeframeKey[] = ['season', 'l20', 'l15', 'l10', 'l7', 'l5']

function splitHittersForSelection(
  exportData: DailyExport,
  selection: Pick<ResolvedResearchSelection, 'player' | 'gamePk'>,
): SplitHitter[] {
  const detail = exportData.game_details?.find((g) => g.game_pk === selection.gamePk)
  if (!detail) return []
  const rows = [...(detail.away_splits ?? []), ...(detail.home_splits ?? [])]
  const playerName = selection.player?.name
  if (!playerName) return rows
  return rows.filter((r) => r.hitter.toLowerCase() === playerName.toLowerCase())
}

function bvpSupported(
  exportData: DailyExport,
  selection: Pick<ResolvedResearchSelection, 'player' | 'gamePk'>,
): boolean {
  return splitHittersForSelection(exportData, selection).some((row) => row.bvp != null)
}

const SITUATION_KEYS: SituationKey[] = [
  'overall',
  'home',
  'away',
  'day',
  'night',
  'vlhp',
  'vrhp',
  'bvp',
]

export function parseTimeframe(value: string | null | undefined): TimeframeKey | null {
  if (!value) return null
  return TIMEFRAME_KEYS.includes(value as TimeframeKey) ? (value as TimeframeKey) : null
}

export function parseSituation(value: string | null | undefined): SituationKey | null {
  if (!value) return null
  return SITUATION_KEYS.includes(value as SituationKey) ? (value as SituationKey) : null
}
