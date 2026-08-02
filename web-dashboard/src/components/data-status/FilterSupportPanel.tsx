import { Card } from '../ui/Card'
import type { FilterSupportMatrix } from '../../types/research'
import {
  SITUATION_OPTIONS,
  TIMEFRAME_OPTIONS,
} from '../../types/research'

function SupportCell({
  label,
  supported,
  reason,
  source,
}: {
  label: string
  supported: boolean
  reason?: string
  source?: string
}) {
  return (
    <div
      className={`rounded border px-2.5 py-2 ${
        supported
          ? 'border-[#238636]/50 bg-[#1A4D2E]/20'
          : 'border-[#30363D] bg-[#0D1117]'
      }`}
      title={reason}
    >
      <p className="text-[11px] font-medium text-[#F0F6FC]">{label}</p>
      <p
        className={`mt-0.5 text-[10px] ${
          supported ? 'text-[#3FB950]' : 'text-[#F85149]'
        }`}
      >
        {supported ? `Supported${source ? ` (${source})` : ''}` : 'Unsupported'}
      </p>
      {!supported && reason && (
        <p className="mt-1 text-[10px] leading-snug text-[#8B949E]">{reason}</p>
      )}
    </div>
  )
}

export function FilterSupportPanel({
  support,
  contextNote,
}: {
  support: FilterSupportMatrix
  contextNote: string
}) {
  return (
    <Card
      title="Filter support matrix"
      subtitle="Honest capability for the current shared context selection"
    >
      <p className="mb-4 text-xs text-[#8B949E]">{contextNote}</p>

      <div className="space-y-4">
        <div>
          <h4 className="mb-2 text-[10px] font-semibold uppercase tracking-[0.12em] text-[#8B949E]">
            Timeframe
          </h4>
          <div className="grid gap-2 sm:grid-cols-2 lg:grid-cols-3">
            {TIMEFRAME_OPTIONS.map(({ key, label }) => {
              const entry = support.timeframe[key]
              return (
                <SupportCell
                  key={key}
                  label={label}
                  supported={entry.supported}
                  reason={entry.reason}
                  source={entry.source}
                />
              )
            })}
          </div>
        </div>

        <div>
          <h4 className="mb-2 text-[10px] font-semibold uppercase tracking-[0.12em] text-[#8B949E]">
            Situation
          </h4>
          <div className="grid gap-2 sm:grid-cols-2 lg:grid-cols-3">
            {SITUATION_OPTIONS.map(({ key, label }) => {
              const entry = support.situation[key]
              return (
                <SupportCell
                  key={key}
                  label={label}
                  supported={entry.supported}
                  reason={entry.reason}
                  source={entry.source}
                />
              )
            })}
          </div>
        </div>

        <div>
          <h4 className="mb-2 text-[10px] font-semibold uppercase tracking-[0.12em] text-[#8B949E]">
            Pitch type
          </h4>
          <SupportCell
            label="Pitch Type"
            supported={support.pitchType.supported}
            reason={support.pitchType.reason}
            source={support.pitchType.source}
          />
        </div>
      </div>
    </Card>
  )
}
