import { Card } from '../ui/Card'
import type { PipelineItem } from '../../lib/dataStatus'
import { StatusBadge } from './StatusBadge'

export function PipelineStatusPanel({ items }: { items: PipelineItem[] }) {
  return (
    <Card title="Pipeline status" subtitle="Loaded / Partial / Missing by data layer">
      <ul className="space-y-3">
        {items.map((item) => (
          <li
            key={item.label}
            className="flex flex-wrap items-start justify-between gap-2 rounded border border-[#21262D] bg-[#0D1117] px-3 py-2"
          >
            <div>
              <p className="text-sm font-medium text-[#F0F6FC]">{item.label}</p>
              <p className="mt-0.5 text-[11px] text-[#8B949E]">{item.detail}</p>
            </div>
            <StatusBadge status={item.status} />
          </li>
        ))}
      </ul>
    </Card>
  )
}
