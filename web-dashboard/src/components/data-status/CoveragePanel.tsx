import { Card } from '../ui/Card'
import type { CoverageMetric } from '../../lib/dataStatus'

function pct(present: number, total: number): string {
  if (total <= 0) return '—'
  return `${Math.round((present / total) * 100)}%`
}

export function CoveragePanel({ metrics }: { metrics: CoverageMetric[] }) {
  return (
    <Card title="Coverage" subtitle="Field presence across the current export">
      <div className="overflow-x-auto">
        <table className="w-full min-w-[28rem] text-left text-xs">
          <thead>
            <tr className="border-b border-[#30363D] text-[10px] uppercase tracking-[0.12em] text-[#8B949E]">
              <th className="pb-2 pr-4 font-semibold">Dataset</th>
              <th className="pb-2 pr-4 font-semibold">Count</th>
              <th className="pb-2 font-semibold">Notes</th>
            </tr>
          </thead>
          <tbody>
            {metrics.map((m) => (
              <tr key={m.label} className="border-b border-[#21262D] last:border-0">
                <td className="py-2 pr-4 font-medium text-[#F0F6FC]">{m.label}</td>
                <td className="py-2 pr-4 font-mono text-[#58A6FF]">
                  {m.present}/{m.total}
                  <span className="ml-1.5 text-[#6E7681]">({pct(m.present, m.total)})</span>
                </td>
                <td className="py-2 text-[#8B949E]">{m.detail ?? '—'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </Card>
  )
}
