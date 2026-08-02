import type { PitchMixEntry } from '../types/slate'

export interface PitchChipItem {
  pitch: string
  usage_pct?: number | null
}

export function normalizePitchMixItems(
  pitches: Array<PitchMixEntry | string> | undefined,
): PitchChipItem[] {
  if (!pitches?.length) return []
  return pitches.map((entry) =>
    typeof entry === 'string' ? { pitch: entry, usage_pct: null } : entry,
  )
}

interface PitchMixFilterChipsProps {
  /** Pitch codes to show — from SP mix or hitter's logged pitch types */
  pitches: PitchChipItem[]
  selected: string | null
  onSelect: (pitch: string | null) => void
  /** Show an explicit All reset chip (default true) */
  showAll?: boolean
}

export function PitchMixFilterChips({
  pitches,
  selected,
  onSelect,
  showAll = true,
}: PitchMixFilterChipsProps) {
  if (!pitches.length && !showAll) {
    return <span className="text-xs text-[#6E7681]">No pitch types</span>
  }

  return (
    <div className="mb-3 flex flex-wrap items-center gap-1.5">
      {showAll && (
        <button
          type="button"
          onClick={() => onSelect(null)}
          className={`rounded border px-2 py-0.5 text-[11px] font-medium transition-colors ${
            selected === null
              ? 'border-[#58A6FF] bg-[#1F6FEB33] text-[#58A6FF]'
              : 'border-[#30363D] bg-[#0D1117] text-[#8B949E] hover:bg-[#21262D] hover:text-[#F0F6FC]'
          }`}
        >
          All
        </button>
      )}
      {pitches.map(({ pitch, usage_pct }) => {
        const active = selected === pitch
        const pctLabel =
          usage_pct == null || Number.isNaN(usage_pct)
            ? null
            : `${((usage_pct <= 1 ? usage_pct * 100 : usage_pct)).toFixed(0)}%`
        return (
          <button
            key={pitch}
            type="button"
            onClick={() => onSelect(active ? null : pitch)}
            title={active ? 'Click to clear filter' : `Filter to ${pitch} only`}
            className={`rounded border px-2 py-0.5 font-mono text-xs transition-colors ${
              active
                ? 'border-[#58A6FF] bg-[#1F6FEB33] text-[#58A6FF]'
                : 'border-[#30363D] bg-[#0D1117] text-[#58A6FF] hover:bg-[#21262D]'
            }`}
          >
            {pitch}
            {pctLabel && (
              <span className={`ml-1 ${active ? 'text-[#58A6FF]' : 'text-[#8B949E]'}`}>
                {pctLabel}
              </span>
            )}
          </button>
        )
      })}
    </div>
  )
}
