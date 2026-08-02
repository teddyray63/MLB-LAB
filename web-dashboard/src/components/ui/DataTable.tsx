import { useMemo, useState, type ReactNode } from 'react'

export interface Column<T> {
  key: string
  label: string
  align?: 'left' | 'right'
  sortable?: boolean
  sortValue?: (row: T) => string | number | null
  render: (row: T) => ReactNode
}

interface DataTableProps<T> {
  columns: Column<T>[]
  rows: T[]
  stickyHeader?: boolean
  compact?: boolean
  emptyMessage?: string
  rowClassName?: (row: T) => string | undefined
}

export function DataTable<T>({
  columns,
  rows,
  stickyHeader = true,
  compact = true,
  emptyMessage = 'No rows',
  rowClassName,
}: DataTableProps<T>) {
  const [sortKey, setSortKey] = useState<string | null>(null)
  const [sortDir, setSortDir] = useState<'asc' | 'desc'>('desc')

  const sortedRows = useMemo(() => {
    if (!sortKey) return rows
    const col = columns.find((c) => c.key === sortKey)
    if (!col?.sortValue) return rows
    const copy = [...rows]
    copy.sort((a, b) => {
      const av = col.sortValue!(a)
      const bv = col.sortValue!(b)
      if (av == null && bv == null) return 0
      if (av == null) return 1
      if (bv == null) return -1
      if (typeof av === 'number' && typeof bv === 'number') {
        return sortDir === 'asc' ? av - bv : bv - av
      }
      return sortDir === 'asc'
        ? String(av).localeCompare(String(bv))
        : String(bv).localeCompare(String(av))
    })
    return copy
  }, [rows, columns, sortKey, sortDir])

  function toggleSort(key: string) {
    if (sortKey === key) {
      setSortDir((d) => (d === 'asc' ? 'desc' : 'asc'))
    } else {
      setSortKey(key)
      setSortDir('desc')
    }
  }

  const cellPad = compact ? 'px-2 py-1.5' : 'px-3 py-2'

  return (
    <div className="overflow-auto rounded-md border border-[#21262D]">
      <table className="w-full min-w-max border-collapse text-left">
        <thead className={stickyHeader ? 'sticky top-0 z-10 bg-[#161B22]' : ''}>
          <tr className="border-b border-[#30363D]">
            {columns.map((col) => {
              const sortable = col.sortable !== false
              const ariaSort =
                !sortable
                  ? undefined
                  : sortKey === col.key
                    ? sortDir === 'asc'
                      ? 'ascending'
                      : 'descending'
                    : 'none'

              return (
                <th
                  key={col.key}
                  aria-sort={ariaSort}
                  className={`${cellPad} text-[10px] font-semibold uppercase tracking-wider text-[#8B949E] ${
                    col.align === 'right' ? 'text-right' : 'text-left'
                  }`}
                >
                  {sortable ? (
                    <button
                      type="button"
                      onClick={() => toggleSort(col.key)}
                      className={`inline-flex w-full cursor-pointer select-none items-center gap-0.5 hover:text-[#F0F6FC] ${
                        col.align === 'right' ? 'justify-end' : 'justify-start'
                      }`}
                    >
                      {col.label}
                      {sortKey === col.key && (sortDir === 'asc' ? ' ↑' : ' ↓')}
                    </button>
                  ) : (
                    col.label
                  )}
                </th>
              )
            })}
          </tr>
        </thead>
        <tbody>
          {sortedRows.length === 0 ? (
            <tr>
              <td
                colSpan={columns.length}
                className={`${cellPad} text-center text-xs text-[#6E7681]`}
              >
                {emptyMessage}
              </td>
            </tr>
          ) : (
            sortedRows.map((row, i) => (
              <tr
                key={i}
                className={`border-b border-[#21262D] transition-colors hover:bg-[#1C2128] ${
                  rowClassName?.(row) ?? ''
                }`}
              >
                {columns.map((col) => (
                  <td
                    key={col.key}
                    className={`${cellPad} text-xs text-[#F0F6FC] ${
                      col.align === 'right' ? 'text-right tabular-nums' : ''
                    }`}
                  >
                    {col.render(row)}
                  </td>
                ))}
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  )
}
