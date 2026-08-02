import { StatCell } from './ui/StatCell'
import { HitterLink } from './ui/HitterLink'
import { DataTable, type Column } from './ui/DataTable'
import { fmtInt, fmtPct, fmtRate } from '../design/format'
import { battingRateToHeat, powerRateToHeat, rateToHeat, type HeatLevel } from '../design/tokens'
import type { TeamSide } from '../types/research'
import type { SplitHitter, SplitLine } from '../types/slate'
import { batSpeedCell, batTrackingPctCell } from './batTrackingCells'

export type SplitKey = 'overall' | 'vs_lhp' | 'vs_rhp' | 'bvp' | 'day_split' | 'night_split'

function lineOf(h: SplitHitter, key: SplitKey): SplitLine | null {
  return h[key] ?? null
}

function SmallSampleTag({ line }: { line: SplitLine | null }) {
  if (!line?.small_sample) return null
  return <span className="ml-1.5 text-[10px] font-normal text-[#D29922]">(small sample)</span>
}

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

function buildColumns(split: SplitKey, teamSide?: TeamSide): Column<SplitHitter>[] {
  const L = (r: SplitHitter) => lineOf(r, split)
  return [
    {
      key: 'hitter',
      label: 'Hitter',
      sortValue: (r) => r.hitter,
      render: (r) => (
        <span>
          <HitterLink name={r.hitter} className="font-medium" side={teamSide} />
          <SmallSampleTag line={L(r)} />
        </span>
      ),
    },
    { key: 'pa', label: 'PA', align: 'right', sortValue: (r) => L(r)?.pa ?? null, render: (r) => fmtInt(L(r)?.pa) },
    { key: 'ab', label: 'AB', align: 'right', sortValue: (r) => L(r)?.ab ?? null, render: (r) => fmtInt(L(r)?.ab) },
    { key: 'hits', label: 'H', align: 'right', sortValue: (r) => L(r)?.hits ?? null, render: (r) => fmtInt(L(r)?.hits) },
    { key: 'hr', label: 'HR', align: 'right', sortValue: (r) => L(r)?.hr ?? null, render: (r) => fmtInt(L(r)?.hr) },
    {
      key: 'avg',
      label: 'AVG',
      align: 'right',
      sortValue: (r) => L(r)?.avg ?? null,
      render: (r) => rateCell(L(r)?.avg, battingRateToHeat(L(r)?.avg), fmtRate),
    },
    {
      key: 'slg',
      label: 'SLG',
      align: 'right',
      sortValue: (r) => L(r)?.slg ?? null,
      render: (r) => rateCell(L(r)?.slg, powerRateToHeat(L(r)?.slg), fmtRate),
    },
    {
      key: 'iso',
      label: 'ISO',
      align: 'right',
      sortValue: (r) => L(r)?.iso ?? null,
      render: (r) => rateCell(L(r)?.iso, powerRateToHeat(L(r)?.iso), fmtRate),
    },
    {
      key: 'woba',
      label: 'wOBA',
      align: 'right',
      sortValue: (r) => L(r)?.woba ?? null,
      render: (r) => rateCell(L(r)?.woba, battingRateToHeat(L(r)?.woba), fmtRate),
    },
    {
      key: 'babip',
      label: 'BABIP',
      align: 'right',
      sortValue: (r) => L(r)?.babip ?? null,
      render: (r) => rateCell(L(r)?.babip, battingRateToHeat(L(r)?.babip), fmtRate),
    },
    {
      key: 'k_pct',
      label: 'K%',
      align: 'right',
      sortValue: (r) => L(r)?.k_pct ?? null,
      render: (r) => rateCell(L(r)?.k_pct, heatPct(L(r)?.k_pct, true), fmtPct),
    },
    {
      key: 'bb_pct',
      label: 'BB%',
      align: 'right',
      sortValue: (r) => L(r)?.bb_pct ?? null,
      render: (r) => rateCell(L(r)?.bb_pct, heatPct(L(r)?.bb_pct), fmtPct),
    },
    {
      key: 'hard_hit_pct',
      label: 'HardHit%',
      align: 'right',
      sortValue: (r) => L(r)?.hard_hit_pct ?? null,
      render: (r) => rateCell(L(r)?.hard_hit_pct, heatPct(L(r)?.hard_hit_pct), fmtPct),
    },
    {
      key: 'barrel_pct',
      label: 'Barrel%',
      align: 'right',
      sortValue: (r) => L(r)?.barrel_pct ?? null,
      render: (r) => rateCell(L(r)?.barrel_pct, heatPct(L(r)?.barrel_pct), fmtPct),
    },
    {
      key: 'bat_speed',
      label: 'BatSpd',
      align: 'right',
      sortValue: (r) => L(r)?.bat_speed ?? null,
      render: (r) => batSpeedCell(L(r)?.bat_speed, L(r)?.bat_tracking_low_confidence),
    },
    {
      key: 'squared_up_pct',
      label: 'SqUp%',
      align: 'right',
      sortValue: (r) => L(r)?.squared_up_pct ?? null,
      render: (r) => batTrackingPctCell(L(r)?.squared_up_pct, L(r)?.bat_tracking_low_confidence),
    },
    {
      key: 'blast_pct',
      label: 'Blast%',
      align: 'right',
      sortValue: (r) => L(r)?.blast_pct ?? null,
      render: (r) => batTrackingPctCell(L(r)?.blast_pct, L(r)?.bat_tracking_low_confidence),
    },
  ]
}

interface TeamSplitsTableProps {
  rows: SplitHitter[]
  split: SplitKey
  teamSide?: TeamSide
}

export function TeamSplitsTable({ rows, split, teamSide }: TeamSplitsTableProps) {
  const columns = buildColumns(split, teamSide)
  const emptyMessage =
    split === 'bvp' ? 'No batter-vs-pitcher sample for these hitters' : 'No split rows'
  return <DataTable columns={columns} rows={rows} emptyMessage={emptyMessage} />
}
