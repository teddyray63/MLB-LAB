import type { Tier } from '../../types/slate'
import { tierColors } from '../../design/tokens'

interface TierBadgeProps {
  tier: Tier
}

export function TierBadge({ tier }: TierBadgeProps) {
  const style = tierColors[tier]
  return (
    <span
      className="inline-flex min-w-[2rem] items-center justify-center rounded px-2 py-0.5 text-[11px] font-bold"
      style={{
        backgroundColor: style.bg,
        color: style.text,
        border: `1px solid ${style.border}`,
      }}
    >
      {style.label}
    </span>
  )
}
