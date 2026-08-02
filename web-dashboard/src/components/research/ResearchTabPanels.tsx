import { RESEARCH_TABS, useResearchTab } from '../../hooks/useResearchTab'
import type { ResearchTabKey } from '../../lib/researchNavigation'
import {
  ResearchOverviewTab,
  ResearchMatchupTab,
  ResearchRecentGamesTab,
  ResearchSplitsTab,
  ResearchPitchMatchupTab,
  ResearchHeatmapsTab,
  ResearchBattedBallsTab,
  ResearchSwingMetricsTab,
  ResearchOutcomeProfileTab,
  ResearchScoutingSummaryTab,
} from './ResearchTabContent'

function TabPanel({ tab }: { tab: ResearchTabKey }) {
  switch (tab) {
    case 'overview':
      return <ResearchOverviewTab />
    case 'matchup':
      return <ResearchMatchupTab />
    case 'recent-games':
      return <ResearchRecentGamesTab />
    case 'splits':
      return <ResearchSplitsTab />
    case 'pitch-matchup':
      return <ResearchPitchMatchupTab />
    case 'heatmaps':
      return <ResearchHeatmapsTab />
    case 'batted-balls':
      return <ResearchBattedBallsTab />
    case 'swing-metrics':
      return <ResearchSwingMetricsTab />
    case 'outcome-profile':
      return <ResearchOutcomeProfileTab />
    case 'scouting-summary':
      return <ResearchScoutingSummaryTab />
    default:
      return <ResearchOverviewTab />
  }
}

export function ResearchTabPanels() {
  const { tab, setTab } = useResearchTab()

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
        aria-label="Research workspace"
      >
        {RESEARCH_TABS.map(({ key, label }) => (
          <button
            key={key}
            type="button"
            role="tab"
            id={`research-tab-${key}`}
            aria-selected={tab === key}
            aria-controls={`research-panel-${key}`}
            tabIndex={tab === key ? 0 : -1}
            onClick={() => setTab(key)}
            onKeyDown={handleKeyDown}
            className={`rounded-md px-2.5 py-1.5 text-[11px] font-medium transition-colors ${
              tab === key
                ? 'bg-[#1F6FEB33] text-[#58A6FF]'
                : 'text-[#8B949E] hover:bg-[#21262D] hover:text-[#F0F6FC]'
            }`}
          >
            {label}
          </button>
        ))}
      </div>
      {RESEARCH_TABS.map(({ key }) => (
        <div
          key={key}
          role="tabpanel"
          id={`research-panel-${key}`}
          aria-labelledby={`research-tab-${key}`}
          tabIndex={0}
          hidden={tab !== key}
        >
          <TabPanel tab={key} />
        </div>
      ))}
    </div>
  )
}
