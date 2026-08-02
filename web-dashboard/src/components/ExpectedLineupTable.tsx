import { useMemo } from 'react'
import { StatCell } from './ui/StatCell'
import { HitterLink } from './ui/HitterLink'
import { DataTable, type Column } from './ui/DataTable'
import { fmtInt, fmtPct, fmtRate } from '../design/format'
import { battingRateToHeat, powerRateToHeat, rateToHeat, type HeatLevel } from '../design/tokens'
import type { TeamSide } from '../types/research'
import type { LineupBatter } from '../types/slate'
import { batSpeedCell, batTrackingPctCell } from './batTrackingCells'

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

function buildColumns(teamSide?: TeamSide): Column<LineupBatter>[] {
  return [
  {
    key: 'order',
    label: '#',
    align: 'right',
    sortValue: (r) => r.order,
    render: (r) => <span className="font-mono text-[#8B949E]">{r.order}</span>,
  },
  {
    key: 'hitter',
    label: 'Hitter',
    sortValue: (r) => r.hitter,
    render: (r) => (
      <div className="flex items-center gap-2">
        <HitterLink name={r.hitter} className="font-medium" side={teamSide} />
        {r.hand && (
          <span className="rounded border border-[#30363D] px-1 py-0.5 font-mono text-[10px] text-[#8B949E]">
            {r.hand}
          </span>
        )}
      </div>
    ),
  },
  {
    key: 'status',
    label: 'Status',
    sortable: false,
    render: (r) => (
      <span className="text-[11px] text-[#8B949E]">{r.status ?? '—'}</span>
    ),
  },
  { key: 'ab', label: 'AB', align: 'right', sortValue: (r) => r.ab, render: (r) => fmtInt(r.ab) },
  { key: 'hits', label: 'H', align: 'right', sortValue: (r) => r.hits, render: (r) => fmtInt(r.hits) },
  { key: 'hr', label: 'HR', align: 'right', sortValue: (r) => r.hr, render: (r) => fmtInt(r.hr) },
  {
    key: 'avg',
    label: 'AVG',
    align: 'right',
    sortValue: (r) => r.avg,
    render: (r) => rateCell(r.avg, battingRateToHeat(r.avg), fmtRate),
  },
  {
    key: 'slg',
    label: 'SLG',
    align: 'right',
    sortValue: (r) => r.slg,
    render: (r) => rateCell(r.slg, powerRateToHeat(r.slg), fmtRate),
  },
  {
    key: 'k_pct',
    label: 'K%',
    align: 'right',
    sortValue: (r) => r.k_pct,
    render: (r) => rateCell(r.k_pct, heatPct(r.k_pct, true), fmtPct),
  },
  {
    key: 'barrel_pct',
    label: 'Barrel%',
    align: 'right',
    sortValue: (r) => r.barrel_pct,
    render: (r) => rateCell(r.barrel_pct, heatPct(r.barrel_pct), fmtPct),
  },
  {
    key: 'bat_speed',
    label: 'BatSpd',
    align: 'right',
    sortValue: (r) => r.bat_speed ?? null,
    render: (r) => batSpeedCell(r.bat_speed, r.bat_tracking_low_confidence),
  },
  {
    key: 'squared_up_pct',
    label: 'SqUp%',
    align: 'right',
    sortValue: (r) => r.squared_up_pct ?? null,
    render: (r) => batTrackingPctCell(r.squared_up_pct, r.bat_tracking_low_confidence),
  },
  {
    key: 'blast_pct',
    label: 'Blast%',
    align: 'right',
    sortValue: (r) => r.blast_pct ?? null,
    render: (r) => batTrackingPctCell(r.blast_pct, r.bat_tracking_low_confidence),
  },
]
}

interface ExpectedLineupTableProps {
  rows: LineupBatter[]
  sourceNote?: string
  teamSide?: TeamSide
}

export function ExpectedLineupTable({ rows, sourceNote, teamSide }: ExpectedLineupTableProps) {
  const columns = useMemo(() => buildColumns(teamSide), [teamSide])
  return (
    <div className="space-y-2">
      {sourceNote && <p className="text-[10px] text-[#6E7681]">{sourceNote}</p>}
      <DataTable columns={columns} rows={rows} emptyMessage="No lineup rows" />
    </div>
  )
}
