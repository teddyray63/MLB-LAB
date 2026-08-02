import type { ReactNode } from 'react'
import { StatCell } from './ui/StatCell'
import { fmtMph, fmtPct } from '../design/format'
import { rateToHeat, type HeatLevel } from '../design/tokens'

function heatPct(value: number | null | undefined): HeatLevel | undefined {
  if (value == null || Number.isNaN(value)) return undefined
  return rateToHeat(value <= 1 ? value * 100 : value, false)
}

function lowConfWrap(node: ReactNode, lowConf: boolean | undefined) {
  if (!lowConf) return node
  return (
    <span className="text-[#D29922]" title="Limited bat-tracking sample in window">
      {node}
    </span>
  )
}

export function batSpeedCell(value: number | null | undefined, lowConf?: boolean) {
  if (value == null || Number.isNaN(value)) {
    return <span className="text-[#6E7681]">—</span>
  }
  return lowConfWrap(
    <span className="font-mono tabular-nums text-[#F0F6FC]">{fmtMph(value)}</span>,
    lowConf,
  )
}

export function batTrackingPctCell(
  value: number | null | undefined,
  lowConf?: boolean,
) {
  if (value == null || Number.isNaN(value)) {
    return <span className="text-[#6E7681]">—</span>
  }
  return lowConfWrap(<StatCell value={fmtPct(value)} heat={heatPct(value)} />, lowConf)
}
