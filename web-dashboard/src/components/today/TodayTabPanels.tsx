import { useState } from 'react'
import { TodayOverviewTab } from './TodayOverviewTab'
import { TodayPitchersTab } from './TodayPitchersTab'
import { TodayLineupsTab } from './TodayLineupsTab'
import { TodayTeamSplitsTab } from './TodayTeamSplitsTab'
import { TodayMatchupsTab } from './TodayMatchupsTab'

const TABS = [
  { key: 'overview', label: 'Overview' },
  { key: 'pitchers', label: 'Pitchers' },
  { key: 'lineups', label: 'Lineups' },
  { key: 'splits', label: 'Team Splits' },
  { key: 'matchups', label: 'Matchups' },
] as const

export type TodayTabKey = (typeof TABS)[number]['key']

export function TodayTabPanels() {
  const [tab, setTab] = useState<TodayTabKey>('overview')

  return (
    <div className="space-y-4">
      <div
        className="flex flex-wrap gap-1 border-b border-[#30363D] pb-2"
        role="tablist"
        aria-label="Today workspace"
      >
        {TABS.map(({ key, label }) => (
          <button
            key={key}
            type="button"
            role="tab"
            aria-selected={tab === key}
            onClick={() => setTab(key)}
            className={`rounded-md px-3 py-1.5 text-[11px] font-medium transition-colors ${
              tab === key
                ? 'bg-[#1F6FEB33] text-[#58A6FF]'
                : 'text-[#8B949E] hover:bg-[#21262D] hover:text-[#F0F6FC]'
            }`}
          >
            {label}
          </button>
        ))}
      </div>

      <div role="tabpanel">
        {tab === 'overview' && <TodayOverviewTab />}
        {tab === 'pitchers' && <TodayPitchersTab />}
        {tab === 'lineups' && <TodayLineupsTab />}
        {tab === 'splits' && <TodayTeamSplitsTab />}
        {tab === 'matchups' && <TodayMatchupsTab />}
      </div>
    </div>
  )
}
