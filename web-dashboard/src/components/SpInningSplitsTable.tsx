import { DataTable, type Column } from './ui/DataTable'
import { fmtInt } from '../design/format'
import type { SpInningStart } from '../types/slate'

const columns: Column<SpInningStart>[] = [
  { key: 'date', label: 'Date', sortValue: (r) => r.date, render: (r) => r.date },
  {
    key: 'f1',
    label: 'Thru 1',
    align: 'right',
    sortValue: (r) => r.f1,
    render: (r) => fmtInt(r.f1),
  },
  {
    key: 'f3',
    label: 'Thru 3',
    align: 'right',
    sortValue: (r) => r.f3,
    render: (r) => fmtInt(r.f3),
  },
  {
    key: 'f5',
    label: 'Thru 5',
    align: 'right',
    sortValue: (r) => r.f5,
    render: (r) => fmtInt(r.f5),
  },
  {
    key: 'f7',
    label: 'Thru 7',
    align: 'right',
    sortValue: (r) => r.f7,
    render: (r) => fmtInt(r.f7),
  },
]

export function SpInningSplitsTable({
  pitcher,
  rows,
}: {
  pitcher: string
  rows: SpInningStart[] | undefined
}) {
  if (!rows?.length) {
    return (
      <p className="text-xs text-[#8B949E]">
        No inning-checkpoint start log for {pitcher || 'this starter'}.
      </p>
    )
  }
  return (
    <div>
      <p className="mb-2 text-[10px] text-[#8B949E]">
        Cumulative runs allowed through innings 1 / 3 / 5 / 7 · last {rows.length} starts · pitching
        context only
      </p>
      <DataTable columns={columns} rows={rows} emptyMessage="No starts" />
    </div>
  )
}
