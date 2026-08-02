import { getPitchDisplayName } from '../../lib/pitchNames'

/** Full pitch name with abbreviation as secondary text — leaderboards and context-aware tables. */
export function PitchTypeCell({ code }: { code: string | null | undefined }) {
  if (!code) return <span className="text-[#6E7681]">—</span>

  const abbr = code.toUpperCase()
  const name = getPitchDisplayName(abbr)

  return (
    <span className="inline-flex flex-col gap-0.5 leading-tight">
      <span className="text-xs text-[#C9D1D9]">{name}</span>
      <span className="font-mono text-[10px] text-[#6E7681]">{abbr}</span>
    </span>
  )
}
