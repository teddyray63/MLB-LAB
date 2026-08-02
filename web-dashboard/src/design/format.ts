/** Format stat values for display — no invented metrics */

export function fmtRate(value: number | null | undefined, decimals = 3): string {
  if (value == null || Number.isNaN(value)) return '—'
  return value.toFixed(decimals)
}

export function fmtPct(value: number | null | undefined): string {
  if (value == null || Number.isNaN(value)) return '—'
  const pct = value <= 1 ? value * 100 : value
  return `${pct.toFixed(1)}%`
}

export function fmtInt(value: number | null | undefined): string {
  if (value == null || Number.isNaN(value)) return '—'
  return String(Math.round(value))
}

export function fmtMph(value: number | null | undefined): string {
  if (value == null || Number.isNaN(value)) return '—'
  return value.toFixed(1)
}

export function fmtScore(value: number | null | undefined): string {
  if (value == null || Number.isNaN(value)) return '—'
  return value.toFixed(3)
}

const RATE_STATS = new Set([
  'wOBA',
  'xwOBA',
  'ISO',
  'AVG',
  'xBA',
  'xSLG',
  'Barrel%',
  'HardHit%',
  'SweetSpot%',
  'Whiff%',
])

const COUNT_STATS = new Set(['Hits', '1B', 'TB'])

/** Format top_plays key_val based on key_stat from export_json */
export function fmtKeyVal(keyStat: string, value: number | string | null | undefined): string {
  if (value == null || value === '') return '—'
  if (typeof value === 'string') return value
  if (COUNT_STATS.has(keyStat)) return fmtInt(value)
  if (keyStat.includes('%')) return fmtPct(value)
  if (RATE_STATS.has(keyStat)) return fmtRate(value)
  return Number.isInteger(value) ? fmtInt(value) : fmtRate(value)
}
