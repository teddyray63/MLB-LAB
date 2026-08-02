import { StatCell } from './ui/StatCell'
import { DataTable, type Column } from './ui/DataTable'
import { fmtInt, fmtPct, fmtRate } from '../design/format'
import { battingRateToHeat, powerRateToHeat, rateToHeat, type HeatLevel } from '../design/tokens'
import type { PitcherPlatoonLine } from '../types/slate'

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

const columns: Column<PitcherPlatoonLine>[] = [
  {
    key: 'split',
    label: 'Split',
    sortable: false,
    render: (r) => <span className="font-medium">{r.split}</span>,
  },
  { key: 'bf', label: 'BF', align: 'right', sortable: false, render: (r) => fmtInt(r.bf) },
  { key: 'hr', label: 'HR', align: 'right', sortable: false, render: (r) => fmtInt(r.hr) },
  { key: 'singles', label: '1B', align: 'right', sortable: false, render: (r) => fmtInt(r.singles) },
  { key: 'doubles', label: '2B', align: 'right', sortable: false, render: (r) => fmtInt(r.doubles) },
  { key: 'triples', label: '3B', align: 'right', sortable: false, render: (r) => fmtInt(r.triples) },
  { key: 'bb', label: 'BB', align: 'right', sortable: false, render: (r) => fmtInt(r.bb) },
  {
    key: 'oba',
    label: 'OBA',
    align: 'right',
    sortable: false,
    render: (r) => rateCell(r.oba, battingRateToHeat(r.oba), fmtRate),
  },
  {
    key: 'slg',
    label: 'SLG',
    align: 'right',
    sortable: false,
    render: (r) => rateCell(r.slg, powerRateToHeat(r.slg), fmtRate),
  },
  {
    key: 'iso',
    label: 'ISO',
    align: 'right',
    sortable: false,
    render: (r) => rateCell(r.iso, powerRateToHeat(r.iso), fmtRate),
  },
  {
    key: 'barrel_pct',
    label: 'Barrel%',
    align: 'right',
    sortable: false,
    render: (r) => rateCell(r.barrel_pct, heatPct(r.barrel_pct, true), fmtPct),
  },
  {
    key: 'hard_hit_pct',
    label: 'HardHit%',
    align: 'right',
    sortable: false,
    render: (r) => rateCell(r.hard_hit_pct, heatPct(r.hard_hit_pct, true), fmtPct),
  },
  {
    key: 'k_pct',
    label: 'K%',
    align: 'right',
    sortable: false,
    render: (r) => rateCell(r.k_pct, heatPct(r.k_pct, false), fmtPct),
  },
]

interface PitcherPlatoonTableProps {
  rows: PitcherPlatoonLine[]
  pitcherName: string
}

export function PitcherPlatoonTable({ rows, pitcherName }: PitcherPlatoonTableProps) {
  if (!rows.length) {
    return (
      <p className="text-xs text-[#6E7681]">
        No platoon sample for {pitcherName || 'this starter'}
      </p>
    )
  }
  return <DataTable columns={columns} rows={rows} emptyMessage="No platoon splits" />
}
