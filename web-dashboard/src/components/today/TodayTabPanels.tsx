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

function TabPanel({ tab }: { tab: TodayTabKey }) {
  switch (tab) {
    case 'overview':
      return <TodayOverviewTab />
    case 'pitchers':
      return <TodayPitchersTab />
    case 'lineups':
      return <TodayLineupsTab />
    case 'splits':
      return <TodayTeamSplitsTab />
    case 'matchups':
      return <TodayMatchupsTab />
  }
}

export function TodayTabPanels() {
  const [tab, setTab] = useState<TodayTabKey>('overview')

  function handleKeyDown(event: React.KeyboardEvent<HTMLButtonElement>) {
    const tablist = event.currentTarget.closest('[role="tablist"]')
    if (!tablist) return

    const tabs = Array.from(tablist.querySelectorAll<HTMLButtonElement>('[role="tab"]'))
    const currentIndex = tabs.indexOf(event.currentTarget)
    if (currentIndex === -1) return

    let nextIndex: number | null = null
    if (event.key === 'ArrowRight') nextIndex = (currentIndex + 1) % tabs.length
    if (event.key === 'ArrowLeft') nextIndex = (currentIndex - 1 + tabs.length) % tabs.length
    if (event.key === 'Home') nextIndex = 0
    if (event.key === 'End') nextIndex = tabs.length - 1
    if (nextIndex == null) return

    event.preventDefault()
    const nextTab = tabs[nextIndex]
    nextTab.focus()
    nextTab.click()
  }

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
            id={`today-tab-${key}`}
            aria-selected={tab === key}
            aria-controls={`today-panel-${key}`}
            tabIndex={tab === key ? 0 : -1}
            onClick={() => setTab(key)}
            onKeyDown={handleKeyDown}
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

      {TABS.map(({ key }) => (
        <div
          key={key}
          role="tabpanel"
          id={`today-panel-${key}`}
          aria-labelledby={`today-tab-${key}`}
          tabIndex={0}
          hidden={tab !== key}
        >
          <TabPanel tab={key} />
        </div>
      ))}
    </div>
  )
}
