import type { Tier } from '../types/slate'

/** Design tokens — dark research dashboard palette */
export const colors = {
  bg: '#0D1117',
  bgElevated: '#161B22',
  bgBanner: '#0B1F3A',
  border: '#30363D',
  borderSubtle: '#21262D',
  text: '#F0F6FC',
  textMuted: '#8B949E',
  textDim: '#6E7681',
  accent: '#58A6FF',
  accentSoft: '#1F6FEB33',
} as const

/** Mirrors Excel / export_json tier_for() — T1 elite, T3 below */
export const tierColors: Record<
  Tier,
  { bg: string; text: string; border: string; label: string }
> = {
  T1: {
    bg: '#1A4D2E',
    text: '#3FB950',
    border: '#238636',
    label: 'T1',
  },
  T2: {
    bg: '#3D2E00',
    text: '#D29922',
    border: '#9E6A03',
    label: 'T2',
  },
  T3: {
    bg: '#3D2200',
    text: '#FB8500',
    border: '#E67E22',
    label: 'T3',
  },
}

export type HeatLevel = 'elite' | 'good' | 'avg' | 'below' | 'poor'

/** Percentile-style heat for rate stats (0–1 or 0–100) */
export function rateToHeat(value: number | null | undefined, invert = false): HeatLevel {
  if (value == null || Number.isNaN(value)) return 'avg'
  const normalized = value <= 1 ? value * 100 : value
  const v = invert ? 100 - normalized : normalized
  if (v >= 85) return 'elite'
  if (v >= 70) return 'good'
  if (v >= 50) return 'avg'
  if (v >= 35) return 'below'
  return 'poor'
}

/** Composite score heat for top_plays.score */
export function scoreToHeat(score: number): HeatLevel {
  if (score >= 0.35) return 'elite'
  if (score >= 0.28) return 'good'
  if (score >= 0.22) return 'avg'
  if (score >= 0.16) return 'below'
  return 'poor'
}

/** Batting rate stats (AVG, wOBA, xwOBA, etc.) — typical range ~0.200–0.450 */
export function battingRateToHeat(value: number | null | undefined): HeatLevel {
  if (value == null || Number.isNaN(value)) return 'avg'
  if (value >= 0.400) return 'elite'
  if (value >= 0.350) return 'good'
  if (value >= 0.300) return 'avg'
  if (value >= 0.250) return 'below'
  return 'poor'
}

/** ISO / SLG power-ish rates */
export function powerRateToHeat(value: number | null | undefined): HeatLevel {
  if (value == null || Number.isNaN(value)) return 'avg'
  if (value >= 0.250) return 'elite'
  if (value >= 0.200) return 'good'
  if (value >= 0.150) return 'avg'
  if (value >= 0.100) return 'below'
  return 'poor'
}

export const heatCellClasses: Record<HeatLevel, string> = {
  elite: 'bg-emerald-950/80 text-emerald-300',
  good: 'bg-green-950/50 text-green-300',
  avg: 'bg-amber-950/50 text-amber-200',
  below: 'bg-orange-950/50 text-orange-300',
  poor: 'bg-red-950/60 text-red-300',
}

export const heatBarClasses: Record<HeatLevel, string> = {
  elite: 'bg-emerald-500',
  good: 'bg-green-500',
  avg: 'bg-amber-400',
  below: 'bg-orange-500',
  poor: 'bg-red-500',
}
