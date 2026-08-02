import type { DailyExport } from '../types/slate'
import { PLAY_CATEGORIES } from '../types/slate'

export const EXPORT_URL = '/data/daily_export.json'

function isTopPlay(row: unknown): boolean {
  if (!row || typeof row !== 'object') return false
  const p = row as Record<string, unknown>
  return (
    typeof p.rank === 'number' &&
    typeof p.hitter === 'string' &&
    typeof p.tier === 'string'
  )
}

export function parseDailyExport(raw: unknown): DailyExport {
  if (!raw || typeof raw !== 'object') {
    throw new Error('Invalid export: expected JSON object')
  }
  const data = raw as Record<string, unknown>
  if (typeof data.date !== 'string') {
    throw new Error('Invalid export: missing date')
  }
  if (!data.top_plays || typeof data.top_plays !== 'object') {
    throw new Error('Invalid export: missing top_plays')
  }
  const topPlays = data.top_plays as Record<string, unknown>
  for (const category of PLAY_CATEGORIES) {
    const rows = topPlays[category]
    if (!Array.isArray(rows)) {
      throw new Error(`Invalid export: top_plays.${category} must be an array`)
    }
    if (!rows.every(isTopPlay)) {
      throw new Error(`Invalid export: malformed rows in top_plays.${category}`)
    }
  }
  return raw as DailyExport
}

export async function loadDailyExport(url = EXPORT_URL): Promise<DailyExport> {
  const res = await fetch(url, { cache: 'no-store' })
  if (!res.ok) {
    throw new Error(`Failed to load ${url} (${res.status})`)
  }
  return parseDailyExport(await res.json())
}
