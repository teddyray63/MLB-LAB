import { Card } from '../ui/Card'
import type { DataStatusSnapshot } from '../../lib/dataStatus'

function InfoRow({ label, value }: { label: string; value: string }) {
  return (
    <div className="flex flex-col gap-0.5 sm:flex-row sm:items-baseline sm:justify-between sm:gap-4">
      <dt className="text-[10px] font-semibold uppercase tracking-[0.12em] text-[#8B949E]">
        {label}
      </dt>
      <dd className="font-mono text-sm text-[#F0F6FC]">{value}</dd>
    </div>
  )
}

export function ExportInfoPanel({ snapshot }: { snapshot: DataStatusSnapshot }) {
  return (
    <Card title="Export information" subtitle="Current daily_export.json metadata">
      <dl className="space-y-3">
        <InfoRow label="Slate date" value={snapshot.slateDate} />
        <InfoRow
          label="Generated at"
          value={snapshot.generatedAt ?? '—'}
        />
        <InfoRow label="Export age" value={snapshot.exportAgeLabel} />
        <InfoRow
          label="Runner version"
          value={snapshot.runnerVersion ?? '—'}
        />
        <InfoRow
          label="Export schema"
          value={snapshot.exportSchemaVersion ?? 'Not present in export'}
        />
        <InfoRow
          label="App URL schema"
          value={`v${snapshot.appSchemaVersion}`}
        />
        <InfoRow
          label="Statcast window"
          value={snapshot.statcastWindow ?? '—'}
        />
      </dl>
      {snapshot.isStale && (
        <p className="mt-4 text-xs text-[#D29922]">
          Export may be stale — slate date differs from today or generated more than 1 day ago.
        </p>
      )}
    </Card>
  )
}
