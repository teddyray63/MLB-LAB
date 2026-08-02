import type { PipelineStatus } from '../../lib/dataStatus'

const STATUS_STYLES: Record<
  PipelineStatus,
  { label: string; className: string }
> = {
  loaded: {
    label: 'Loaded',
    className: 'border-[#238636] bg-[#1A4D2E]/40 text-[#3FB950]',
  },
  partial: {
    label: 'Partial',
    className: 'border-[#9E6A03] bg-[#3D2E00]/40 text-[#D29922]',
  },
  missing: {
    label: 'Missing',
    className: 'border-[#DA3633] bg-[#4C1D1D]/40 text-[#F85149]',
  },
}

export function StatusBadge({ status }: { status: PipelineStatus }) {
  const { label, className } = STATUS_STYLES[status]
  return (
    <span
      className={`inline-flex rounded border px-2 py-0.5 text-[10px] font-semibold uppercase tracking-wide ${className}`}
    >
      {label}
    </span>
  )
}
