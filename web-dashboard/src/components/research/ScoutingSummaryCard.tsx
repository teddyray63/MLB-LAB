import { useMemo } from 'react'
import { buildScoutingSummary } from '../../lib/scoutingEvidence'
import { useResearchPlayerData } from '../../hooks/useResearchPlayerData'
import { Card } from '../ui/Card'

function BulletList({ title, items }: { title: string; items: string[] }) {
  if (!items.length) {
    return (
      <div>
        <h4 className="mb-2 text-[10px] font-semibold uppercase tracking-[0.14em] text-[#8B949E]">
          {title}
        </h4>
        <p className="text-xs text-[#6E7681]">No metric-backed signals in current sample.</p>
      </div>
    )
  }
  return (
    <div>
      <h4 className="mb-2 text-[10px] font-semibold uppercase tracking-[0.14em] text-[#8B949E]">
        {title}
      </h4>
      <ul className="space-y-1.5 text-sm text-[#F0F6FC]">
        {items.map((item) => (
          <li key={item} className="flex gap-2">
            <span className="text-[#58A6FF]" aria-hidden>
              •
            </span>
            <span>{item}</span>
          </li>
        ))}
      </ul>
    </div>
  )
}

/** Metric-backed synthesis — no AI, no speculation. */
export function ScoutingSummaryCard() {
  const data = useResearchPlayerData()
  const summary = useMemo(() => buildScoutingSummary(data), [data])

  if (!data.playerName) {
    return (
      <Card title="Scouting summary" subtitle="Select a player">
        <p className="text-sm text-[#8B949E]">No evidence until a player is selected.</p>
      </Card>
    )
  }

  const pitcherLabel =
    data.selection.pitcher?.name ?? data.selection.opposingPitcher?.name ?? "Today's pitcher"

  return (
    <Card
      title="Scouting summary"
      subtitle="Evidence from export metrics · 120-day Statcast window unless noted"
    >
      <div className="grid gap-6 lg:grid-cols-2">
        <BulletList title="Strengths" items={summary.strengths} />
        <BulletList title="Weaknesses" items={summary.weaknesses} />
      </div>

      <div className="mt-6 border-t border-[#30363D] pt-4">
        <h4 className="mb-2 text-[10px] font-semibold uppercase tracking-[0.14em] text-[#8B949E]">
          {pitcherLabel}
        </h4>
        {summary.pitcherProfile.length ? (
          <ul className="flex flex-wrap gap-2">
            {summary.pitcherProfile.map(({ label, pct }) => (
              <li
                key={label}
                className="rounded border border-[#30363D] bg-[#0D1117] px-2 py-1 font-mono text-xs text-[#58A6FF]"
              >
                {label}
                <span className="ml-1.5 text-[#8B949E]">{pct}</span>
              </li>
            ))}
          </ul>
        ) : (
          <p className="text-xs text-[#6E7681]">Pitch mix unavailable for opposing starter.</p>
        )}
      </div>

      {summary.evidence.length > 0 && (
        <div className="mt-6 border-t border-[#30363D] pt-4">
          <h4 className="mb-3 text-[10px] font-semibold uppercase tracking-[0.14em] text-[#8B949E]">
            Supporting evidence
          </h4>
          <dl className="grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-5">
            {summary.evidence.map(({ label, value }) => (
              <div
                key={label}
                className="rounded border border-[#30363D] bg-[#0D1117] px-3 py-2 text-center"
              >
                <dt className="text-[10px] text-[#8B949E]">{label}</dt>
                <dd className="mt-1 font-mono text-sm font-medium text-[#F0F6FC]">{value}</dd>
              </div>
            ))}
          </dl>
        </div>
      )}
    </Card>
  )
}
