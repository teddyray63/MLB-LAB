import { useGameContext } from '../context/ResearchContext'
import { RESEARCH_SCHEMA_VERSION } from '../types/research'
import { LeaderboardCategoryNav } from '../components/leaderboards/LeaderboardCategoryNav'
import { LeaderboardEmptyState } from '../components/leaderboards/LeaderboardEmptyState'
import { LeaderboardFilterNote } from '../components/leaderboards/LeaderboardFilterNote'
import { LeaderboardResults } from '../components/leaderboards/LeaderboardTable'
import { LeaderboardScopeControl } from '../components/leaderboards/LeaderboardScopeControl'
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
    <div className="space-y-5">
      <div>
        <p className="text-xs font-medium uppercase tracking-[0.12em] text-[#8B949E]">
          Leaderboards
        </p>
        <h2 className="text-2xl font-bold tracking-tight">{selection.date}</h2>
        <p className="mt-1 text-sm text-[#8B949E]">
          Top Plays and Category Boards · use the header for date, game, and filters
        </p>
        {schemaWarning && (
          <p className="mt-2 text-[10px] text-[#D29922]">
            {schemaWarning} — app expects v{RESEARCH_SCHEMA_VERSION}.
          </p>
        )}
      </div>

      <LeaderboardScopeControl
        scope={scope}
        onScopeChange={setScope}
        hasValidGame={hasValidGame}
        dataWindow={data.dataWindow}
      />

      <LeaderboardCategoryNav category={category} onCategoryChange={setCategory} />

      <LeaderboardFilterNote
        category={category}
        pitchFilterApplied={data.pitchFilterApplied}
      />

      {data.rowCount === 0 ? (
        <LeaderboardEmptyState
          scope={scope}
          categoryLabel={data.categoryLabel}
          hasValidGame={hasValidGame}
          pitchFilterApplied={data.pitchFilterApplied}
        />
      ) : (
        <LeaderboardResults
          isTopPlaysView={data.isTopPlaysView}
          topPlays={data.topPlays}
          boardRows={data.boardRows}
          categoryLabel={data.categoryLabel}
        />
      )}
    </div>
  )
}
