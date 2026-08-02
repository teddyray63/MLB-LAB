import type { HeatLevel } from '../../design/tokens'
import { heatCellClasses } from '../../design/tokens'

interface StatCellProps {
  value: string
  heat?: HeatLevel
  className?: string
}

export function StatCell({ value, heat, className = '' }: StatCellProps) {
  const heatClass = heat ? heatCellClasses[heat] : ''
  return (
    <span
      className={`inline-block whitespace-nowrap rounded px-1.5 py-0.5 text-xs tabular-nums ${heatClass} ${className}`}
    >
      {value}
    </span>
  )
}
