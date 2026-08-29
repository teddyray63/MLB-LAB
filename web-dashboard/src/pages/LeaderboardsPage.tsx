import { useGameContext } from '../context/ResearchContext'
import { RESEARCH_SCHEMA_VERSION } from '../types/research'
import { LeaderboardCategoryNav } from '../components/leaderboards/LeaderboardCategoryNav'
import { LeaderboardEmptyState } from '../components/leaderboards/LeaderboardEmptyState'
import { LeaderboardFilterNote } from '../components/leaderboards/LeaderboardFilterNote'
import { LeaderboardResults } from '../components/leaderboards/LeaderboardTable'
import { LeaderboardScopeControl } from '../components/leaderboards/LeaderboardScopeControl'
import { PageHeader } from '../components/ui/PageHeader'
import { WorkspacePage } from '../components/ui/WorkspacePage'
import { useLeaderboardCategory } from '../hooks/useLeaderboardCategory'
import { useLeaderboardData } from '../hooks/useLeaderboardData'
import { useLeaderboardScope } from '../hooks/useLeaderboardScope'

export function LeaderboardsPage() {
  const { selection } = useGameContext()
  const { scope, setScope, hasValidGame } = useLeaderboardScope()
  const { category, setCategory } = useLeaderboardCategory()
  const data = useLeaderboardData(scope, category)

  const schemaWarning = selection.warnings.find((w) => w.includes('schema v'))

  return (
    <WorkspacePage>
      <PageHeader
        kicker="Leaderboards"
        title={selection.date}
        description={
          data.exportHasLeaderboardSections
            ? 'Top Plays and Category Boards · use the header for date, game, and filters'
            : 'Top Plays and Category Boards · not populated in the current export'
        }
        warning={
          schemaWarning
            ? `${schemaWarning} — app expects v${RESEARCH_SCHEMA_VERSION}.`
            : undefined
        }
      />

      <div className="space-y-4">
        <LeaderboardScopeControl
          scope={scope}
          onScopeChange={setScope}
          hasValidGame={hasValidGame}
          dataWindow={data.dataWindow}
        />

        <LeaderboardCategoryNav category={category} onCategoryChange={setCategory} />

        <LeaderboardFilterNote pitchFilterApplied={data.pitchFilterApplied} />
      </div>

      {data.rowCount === 0 ? (
        <LeaderboardEmptyState
          scope={scope}
          categoryLabel={data.categoryLabel}
          hasValidGame={hasValidGame}
          pitchFilterApplied={data.pitchFilterApplied}
          exportHasSourceRows={data.exportHasSourceRows}
        />
      ) : (
        <LeaderboardResults
          isTopPlaysView={data.isTopPlaysView}
          topPlays={data.topPlays}
          boardRows={data.boardRows}
          categoryLabel={data.categoryLabel}
        />
      )}
    </WorkspacePage>
  )
}
