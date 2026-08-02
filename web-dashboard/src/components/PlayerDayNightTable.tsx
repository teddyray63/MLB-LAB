import { StatCell } from './ui/StatCell'
import { DataTable, type Column } from './ui/DataTable'
import { fmtInt, fmtPct, fmtRate } from '../design/format'
import { battingRateToHeat, powerRateToHeat, rateToHeat, type HeatLevel } from '../design/tokens'
import type { HitterFullSplitLine } from '../types/slate'

export type PlayerSplitKey = 'overall' | 'day_split' | 'night_split'

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

interface DisplayRow extends HitterFullSplitLine {
  split: string
}

const columns: Column<DisplayRow>[] = [
  {
    key: 'split',
    label: 'Split',
    sortable: false,
    render: (r) => (
      <span className="font-medium">
        {r.split}
        {r.small_sample && (
          <span className="ml-1.5 text-[10px] font-normal text-[#D29922]">(small sample)</span>
        )}
      </span>
    ),
  },
  { key: 'pa', label: 'PA', align: 'right', sortable: false, render: (r) => fmtInt(r.pa) },
  { key: 'ab', label: 'AB', align: 'right', sortable: false, render: (r) => fmtInt(r.ab) },
  { key: 'hits', label: 'H', align: 'right', sortable: false, render: (r) => fmtInt(r.hits) },
  { key: 'hr', label: 'HR', align: 'right', sortable: false, render: (r) => fmtInt(r.hr) },
  {
    key: 'avg',
    label: 'AVG',
    align: 'right',
    sortable: false,
    render: (r) => rateCell(r.avg, battingRateToHeat(r.avg), fmtRate),
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
    key: 'woba',
    label: 'wOBA',
    align: 'right',
    sortable: false,
    render: (r) => rateCell(r.woba, battingRateToHeat(r.woba), fmtRate),
  },
  {
    key: 'xwoba',
    label: 'xwOBA',
    align: 'right',
    sortable: false,
    render: (r) => rateCell(r.xwoba, battingRateToHeat(r.xwoba), fmtRate),
  },
  {
    key: 'xba',
    label: 'xBA',
    align: 'right',
    sortable: false,
    render: (r) => rateCell(r.xba, battingRateToHeat(r.xba), fmtRate),
  },
  {
    key: 'xslg',
    label: 'xSLG',
    align: 'right',
    sortable: false,
    render: (r) => rateCell(r.xslg, powerRateToHeat(r.xslg), fmtRate),
  },
  {
    key: 'sweet_spot_pct',
    label: 'SweetSpot%',
    align: 'right',
    sortable: false,
    render: (r) => rateCell(r.sweet_spot_pct, heatPct(r.sweet_spot_pct), fmtPct),
  },
  {
    key: 'barrel_pct',
    label: 'Barrel%',
    align: 'right',
    sortable: false,
    render: (r) => rateCell(r.barrel_pct, heatPct(r.barrel_pct), fmtPct),
  },
  {
    key: 'hard_hit_pct',
    label: 'HardHit%',
    align: 'right',
    sortable: false,
    render: (r) => rateCell(r.hard_hit_pct, heatPct(r.hard_hit_pct), fmtPct),
  },
  {
    key: 'whiff_pct',
    label: 'Whiff%',
    align: 'right',
    sortable: false,
    render: (r) => rateCell(r.whiff_pct, heatPct(r.whiff_pct, true), fmtPct),
  },
]

const SPLIT_LABELS: Record<PlayerSplitKey, string> = {
  overall: 'Overall',
  day_split: 'Day',
  night_split: 'Night',
}

interface PlayerDayNightTableProps {
  profile: import('../types/slate').HitterDayNightProfile | undefined
  activeSplit: PlayerSplitKey
}

export function PlayerDayNightTable({ profile, activeSplit }: PlayerDayNightTableProps) {
  if (!profile) {
    return <p className="text-sm text-[#8B949E]">No day/night split data for this hitter</p>
  }

  const line = profile[activeSplit]
  const row: DisplayRow = { ...line, split: SPLIT_LABELS[activeSplit] }

  return (
    <div className="space-y-2">
      <p className="text-[10px] text-[#6E7681]">
        120-day Statcast · day/night from MLB Stats API schedule (unmapped games excluded)
      </p>
      <DataTable columns={columns} rows={[row]} emptyMessage="No split data" />
    </div>
  )
}

export const PLAYER_SPLITS: { key: PlayerSplitKey; label: string }[] = [
  { key: 'overall', label: 'Overall' },
  { key: 'day_split', label: 'Day' },
  { key: 'night_split', label: 'Night' },
]
