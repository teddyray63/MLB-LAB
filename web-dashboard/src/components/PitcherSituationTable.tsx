import { StatCell } from './ui/StatCell'
import { DataTable, type Column } from './ui/DataTable'
import { fmtPct, fmtRate } from '../design/format'
import { battingRateToHeat, powerRateToHeat, rateToHeat, type HeatLevel } from '../design/tokens'
import type { PitcherSituationLine } from '../types/slate'

function heatPct(value: number | null | undefined, invert = false): HeatLevel | undefined {
  if (value == null || Number.isNaN(value)) return undefined
  return rateToHeat(value <= 1 ? value * 100 : value, invert)
}

function rateCell(
  value: number | null | undefined,
  heat: HeatLevel | undefined,
  format: (v: number | null | undefined) => string,
) {
  if (value == null || Number.isNaN(value)) return <span className="text-[#6E7681]">—</span>
  return <StatCell value={format(value)} heat={heat} />
}

const columns: Column<PitcherSituationLine>[] = [
  {
    key: 'split',
    label: 'Split',
    sortable: false,
    render: (r) => <span className="font-medium">{r.split}</span>,
  },
  {
    key: 'ip',
    label: 'IP',
    align: 'right',
    sortable: false,
    render: (r) => (r.ip != null ? r.ip.toFixed(1) : '—'),
  },
  {
    key: 'ra9',
    label: 'RA/9',
    align: 'right',
    sortable: false,
    render: (r) => rateCell(r.ra9, heatPct(r.ra9, true), fmtRate),
  },
  {
    key: 'whip',
    label: 'WHIP',
    align: 'right',
    sortable: false,
    render: (r) => rateCell(r.whip, heatPct(r.whip, true), fmtRate),
  },
  {
    key: 'oba',
    label: 'OBA',
    align: 'right',
    sortable: false,
    render: (r) => rateCell(r.oba, battingRateToHeat(r.oba), fmtRate),
  },
  {
    key: 'iso',
    label: 'ISO',
    align: 'right',
    sortable: false,
    render: (r) => rateCell(r.iso, powerRateToHeat(r.iso), fmtRate),
  },
  {
    key: 'k_pct',
    label: 'K%',
    align: 'right',
    sortable: false,
    render: (r) => rateCell(r.k_pct, heatPct(r.k_pct, false), fmtPct),
  },
  {
    key: 'k9',
    label: 'K/9',
    align: 'right',
    sortable: false,
    render: (r) => (r.k9 != null ? r.k9.toFixed(2) : '—'),
  },
  {
    key: 'hr9',
    label: 'HR/9',
    align: 'right',
    sortable: false,
    render: (r) => (r.hr9 != null ? r.hr9.toFixed(2) : '—'),
  },
  {
    key: 'barrel_pct',
    label: 'Barrel%',
    align: 'right',
    sortable: false,
    render: (r) => rateCell(r.barrel_pct, heatPct(r.barrel_pct, true), fmtPct),
  },
]

interface PitcherSituationTableProps {
  rows: PitcherSituationLine[]
  pitcherName: string
}

export function PitcherSituationTable({ rows, pitcherName }: PitcherSituationTableProps) {
  if (!rows.length) {
    return (
      <p className="text-xs text-[#6E7681]">
        No Statcast sample for {pitcherName || 'this starter'}
      </p>
    )
  }
  return (
    <div className="space-y-2">
      <p className="text-[10px] text-[#6E7681]">
        120-day Statcast window · RA/9 = runs allowed per 9 IP (not official ERA) · OBA = opponent AVG
      </p>
      <DataTable columns={columns} rows={rows} emptyMessage="No splits" />
    </div>
  )
}
