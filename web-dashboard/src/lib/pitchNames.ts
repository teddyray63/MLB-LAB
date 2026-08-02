/** Statcast pitch_type code → full display name (shared across app). */

const PITCH_NAMES: Record<string, string> = {
  FF: 'Four-Seam Fastball',
  SI: 'Sinker',
  FC: 'Cutter',
  SL: 'Slider',
  ST: 'Sweeper',
  CU: 'Curveball',
  KC: 'Knuckle Curve',
  CH: 'Changeup',
  FS: 'Splitter',
  SV: 'Slurve',
  KN: 'Knuckleball',
  EP: 'Eephus',
  FO: 'Forkball',
  SC: 'Screwball',
  PO: 'Pitchout',
  AB: 'Auto Ball',
  UN: 'Unknown',
}

export interface FormatPitchOptions {
  /** Include abbreviation in parentheses, e.g. "Four-Seam Fastball (FF)" */
  compact?: boolean
}

export function getPitchDisplayName(code: string | null | undefined): string {
  if (!code) return 'All Pitches'
  const upper = code.toUpperCase()
  return PITCH_NAMES[upper] ?? `Unknown Pitch (${upper})`
}

export function formatPitchName(
  code: string | null | undefined,
  options: FormatPitchOptions = {},
): string {
  if (!code) return 'All Pitches'
  const upper = code.toUpperCase()
  const name = PITCH_NAMES[upper] ?? `Unknown Pitch (${upper})`
  if (options.compact) {
    return `${name} (${upper})`
  }
  return name
}

/** All known pitch codes for filter dropdowns (sorted by name). */
export function allPitchCodes(): string[] {
  return Object.keys(PITCH_NAMES).sort((a, b) =>
    getPitchDisplayName(a).localeCompare(getPitchDisplayName(b)),
  )
}

export function pitchCodesFromMix(codes: string[]): string[] {
  const unique = [...new Set(codes.filter(Boolean).map((c) => c.toUpperCase()))]
  return unique.sort((a, b) => getPitchDisplayName(a).localeCompare(getPitchDisplayName(b)))
}
