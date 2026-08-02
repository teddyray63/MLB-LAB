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
            aria-selected={tab === key}
            onClick={() => setTab(key)}
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
      <div role="tabpanel">
        <TabPanel tab={tab} />
      </div>
    </div>
  )
}
