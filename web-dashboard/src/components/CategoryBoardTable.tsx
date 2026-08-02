import { useMemo, type ReactNode } from 'react'
import { StatCell } from './ui/StatCell'
import { HitterLink } from './ui/HitterLink'
import { DataTable, type Column } from './ui/DataTable'
import { fmtInt, fmtPct, fmtRate } from '../design/format'
import { battingRateToHeat, powerRateToHeat, rateToHeat } from '../design/tokens'
import type { HitterRow } from '../types/slate'
import { batSpeedCell, batTrackingPctCell } from './batTrackingCells'

function heatPct(value: number | null | undefined) {
  return rateToHeat(value == null ? null : value <= 1 ? value * 100 : value, false)
}

function heatWhiff(value: number | null | undefined) {
  return rateToHeat(value == null ? null : value <= 1 ? value * 100 : value, true)
}

const columns: Column<HitterRow>[] = [
  {
    key: 'hitter',
    label: 'Hitter',
    sortValue: (r) => r.hitter,
    render: (r) => <HitterLink name={r.hitter} className="font-medium" team={r.team} />,
  },
  { key: 'team', label: 'Team', sortValue: (r) => r.team, render: (r) => r.team },
  {
    key: 'game',
    label: 'Game',
    sortValue: (r) => r.game,
    render: (r) => <span className="max-w-[160px] truncate" title={r.game}>{r.game}</span>,
  },
  { key: 'opp_sp', label: 'Opp SP', sortValue: (r) => r.opp_sp, render: (r) => r.opp_sp },
  { key: 'pitch', label: 'Pitch', sortValue: (r) => r.pitch, render: (r) => <span className="font-mono text-[#58A6FF]">{r.pitch}</span> },
  { key: 'pa', label: 'PA', align: 'right', sortValue: (r) => r.pa, render: (r) => fmtInt(r.pa) },
  { key: 'hits', label: 'Hits', align: 'right', sortValue: (r) => r.hits, render: (r) => fmtInt(r.hits) },
  { key: 'singles', label: '1B', align: 'right', sortValue: (r) => r.singles, render: (r) => fmtInt(r.singles) },
  { key: 'tb', label: 'TB', align: 'right', sortValue: (r) => r.tb, render: (r) => fmtInt(r.tb) },
  {
    key: 'avg',
    label: 'AVG',
    align: 'right',
    sortValue: (r) => r.avg,
    render: (r) => <StatCell value={fmtRate(r.avg)} heat={battingRateToHeat(r.avg)} />,
  },
  {
    key: 'slg',
    label: 'SLG',
    align: 'right',
    sortValue: (r) => r.slg,
    render: (r) => <StatCell value={fmtRate(r.slg)} heat={powerRateToHeat(r.slg)} />,
  },
  {
    key: 'iso',
    label: 'ISO',
    align: 'right',
    sortValue: (r) => r.iso,
    render: (r) => <StatCell value={fmtRate(r.iso)} heat={powerRateToHeat(r.iso)} />,
  },
  {
    key: 'woba',
    label: 'wOBA',
    align: 'right',
    sortValue: (r) => r.woba,
    render: (r) => <StatCell value={fmtRate(r.woba)} heat={battingRateToHeat(r.woba)} />,
  },
  {
    key: 'xwoba',
    label: 'xwOBA',
    align: 'right',
    sortValue: (r) => r.xwoba,
    render: (r) => <StatCell value={fmtRate(r.xwoba)} heat={battingRateToHeat(r.xwoba)} />,
  },
  {
    key: 'xba',
    label: 'xBA',
    align: 'right',
    sortValue: (r) => r.xba,
    render: (r) => <StatCell value={fmtRate(r.xba)} heat={battingRateToHeat(r.xba)} />,
  },
  {
    key: 'xslg',
    label: 'xSLG',
    align: 'right',
    sortValue: (r) => r.xslg,
    render: (r) => <StatCell value={fmtRate(r.xslg)} heat={powerRateToHeat(r.xslg)} />,
  },
  {
    key: 'sweet_spot_pct',
    label: 'SweetSpot%',
    align: 'right',
    sortValue: (r) => r.sweet_spot_pct,
    render: (r) => <StatCell value={fmtPct(r.sweet_spot_pct)} heat={heatPct(r.sweet_spot_pct)} />,
  },
  {
    key: 'barrel_pct',
    label: 'Barrel%',
    align: 'right',
    sortValue: (r) => r.barrel_pct,
    render: (r) => <StatCell value={fmtPct(r.barrel_pct)} heat={heatPct(r.barrel_pct)} />,
  },
  {
    key: 'hard_hit_pct',
    label: 'HardHit%',
    align: 'right',
    sortValue: (r) => r.hard_hit_pct,
    render: (r) => <StatCell value={fmtPct(r.hard_hit_pct)} heat={heatPct(r.hard_hit_pct)} />,
  },
  {
    key: 'whiff_pct',
    label: 'Whiff%',
    align: 'right',
    sortValue: (r) => r.whiff_pct,
    render: (r) => <StatCell value={fmtPct(r.whiff_pct)} heat={heatWhiff(r.whiff_pct)} />,
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
  {
    key: 'near_hr',
    label: 'Near HR',
    align: 'right',
    sortValue: (r) => r.near_hr ?? null,
    render: (r) => fmtInt(r.near_hr),
  },
]

const IDENTITY_KEYS = new Set(['hitter', 'team', 'game', 'opp_sp'])

interface CategoryBoardTableProps {
  rows: HitterRow[]
  teamFilter?: string
  /** Hide hitter/team/game/opp SP — useful when those are shown in page chrome */
  hideIdentity?: boolean
  emptyMessage?: string
  /** Custom hitter cell — used by leaderboards for row-scoped research navigation */
  renderHitter?: (row: HitterRow) => ReactNode
}

export function CategoryBoardTable({
  rows,
  teamFilter = '',
  hideIdentity = false,
  emptyMessage = 'No rows for this filter',
  renderHitter,
}: CategoryBoardTableProps) {
  const filtered = useMemo(() => {
    if (!teamFilter) return rows
    return rows.filter((row) => row.team === teamFilter)
  }, [rows, teamFilter])

  const visibleColumns = useMemo(() => {
    const cols = hideIdentity ? columns.filter((col) => !IDENTITY_KEYS.has(col.key)) : columns
    if (!renderHitter) return cols
    return cols.map((col) =>
      col.key === 'hitter'
        ? {
            ...col,
            render: (r: HitterRow) => renderHitter(r),
          }
        : col,
    )
  }, [hideIdentity, renderHitter])

  return (
    <DataTable columns={visibleColumns} rows={filtered} emptyMessage={emptyMessage} />
  )
}

export function boardTeams(rows: HitterRow[]): string[] {
  return [...new Set(rows.map((r) => r.team).filter(Boolean))].sort()
}
