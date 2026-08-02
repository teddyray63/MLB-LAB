import { StatCell } from './ui/StatCell'
import { HitterLink } from './ui/HitterLink'
import { DataTable, type Column } from './ui/DataTable'
import { fmtInt, fmtPct, fmtRate } from '../design/format'
import { battingRateToHeat, powerRateToHeat, rateToHeat, type HeatLevel } from '../design/tokens'
import type { GameHitter } from '../types/slate'

function heatPct(value: number | null | undefined): HeatLevel | undefined {
  if (value == null || Number.isNaN(value)) return undefined
  return rateToHeat(value <= 1 ? value * 100 : value, false)
}

function rateCell(
  value: number | null | undefined,
  heat: HeatLevel | undefined,
  format: (v: number | null | undefined) => string,
) {
  if (value == null || Number.isNaN(value)) {
    return <span className="text-[#6E7681]">—</span>
  }
  return <StatCell value={format(value)} heat={heat} />
}

const columns: Column<GameHitter>[] = [
  {
    key: 'hitter',
    label: 'Hitter',
    sortValue: (r) => r.hitter,
    render: (r) => <HitterLink name={r.hitter} className="font-medium" />,
  },
  {
    key: 'pa',
    label: 'PA',
    align: 'right',
    sortValue: (r) => r.pa,
    render: (r) => fmtInt(r.pa),
  },
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
    key: 'iso',
    label: 'ISO',
    align: 'right',
    sortValue: (r) => r.iso,
    render: (r) => rateCell(r.iso, powerRateToHeat(r.iso), fmtRate),
  },
  {
    key: 'woba',
    label: 'wOBA',
    align: 'right',
    sortValue: (r) => r.woba,
    render: (r) => rateCell(r.woba, battingRateToHeat(r.woba), fmtRate),
  },
  {
    key: 'xwoba',
    label: 'xwOBA',
    align: 'right',
    sortValue: (r) => r.xwoba,
    render: (r) => rateCell(r.xwoba, battingRateToHeat(r.xwoba), fmtRate),
  },
  {
    key: 'xba',
    label: 'xBA',
    align: 'right',
    sortValue: (r) => r.xba,
    render: (r) => rateCell(r.xba, battingRateToHeat(r.xba), fmtRate),
  },
  {
    key: 'xslg',
    label: 'xSLG',
    align: 'right',
    sortValue: (r) => r.xslg,
    render: (r) => rateCell(r.xslg, powerRateToHeat(r.xslg), fmtRate),
  },
  {
    key: 'sweet_spot_pct',
    label: 'SweetSpot%',
    align: 'right',
    sortValue: (r) => r.sweet_spot_pct,
    render: (r) => rateCell(r.sweet_spot_pct, heatPct(r.sweet_spot_pct), fmtPct),
  },
  {
    key: 'barrel_pct',
    label: 'Barrel%',
    align: 'right',
    sortValue: (r) => r.barrel_pct,
    render: (r) => rateCell(r.barrel_pct, heatPct(r.barrel_pct), fmtPct),
  },
  {
    key: 'hard_hit_pct',
    label: 'HardHit%',
    align: 'right',
    sortValue: (r) => r.hard_hit_pct,
    render: (r) => rateCell(r.hard_hit_pct, heatPct(r.hard_hit_pct), fmtPct),
  },
]

interface GameHitterPoolTableProps {
  hitters: GameHitter[]
}

export function GameHitterPoolTable({ hitters }: GameHitterPoolTableProps) {
  return (
    <DataTable columns={columns} rows={hitters} emptyMessage="No hitter pool rows" />
  )
}
