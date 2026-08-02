import { DataTable, type Column } from './ui/DataTable'
import { fmtInt } from '../design/format'
import type { BullpenAppearance } from '../types/slate'

const columns: Column<BullpenAppearance>[] = [
  {
    key: 'reliever',
    label: 'Reliever',
    sortValue: (r) => r.reliever,
    render: (r) => (
      <span className="inline-flex items-center gap-2">
        {r.reliever}
        {r.flagged && (
          <span
            className="rounded border border-[#E67E22]/60 bg-[#3D2200] px-1.5 py-0.5 text-[10px] font-semibold uppercase tracking-wide text-[#FB8500]"
            title="3+ recent appearances or pitched yesterday"
          >
            Tired
          </span>
        )}
      </span>
    ),
  },
  {
    key: 'date',
    label: 'Date',
    sortValue: (r) => r.date,
    render: (r) => r.date || '—',
  },
  {
    key: 'ip',
    label: 'IP',
    align: 'right',
    sortValue: (r) => (r.ip == null ? null : String(r.ip)),
    render: (r) => (r.ip == null || r.ip === '' ? '—' : String(r.ip)),
  },
  {
    key: 'pitches',
    label: 'Pitches',
    align: 'right',
    sortValue: (r) => r.pitches,
    render: (r) => fmtInt(r.pitches),
  },
]

interface BullpenTableProps {
  rows: BullpenAppearance[]
}

export function BullpenTable({ rows }: BullpenTableProps) {
  // Error payload from export: { error: string }
  if (!Array.isArray(rows)) {
    const err = (rows as { error?: string })?.error
    return (
      <p className="text-sm text-[#F85149]">
        Bullpen unavailable{err ? `: ${err}` : ''}
      </p>
    )
  }

  return (
    <DataTable
      columns={columns}
      rows={rows}
      emptyMessage="No recent bullpen appearances"
      rowClassName={(row) =>
        row.flagged
          ? 'border-l-2 border-l-[#E67E22] bg-[#3D2200]/35'
          : undefined
      }
    />
  )
}
