import { PlayerSummaryCard } from '../components/research/PlayerSummaryCard'
import { ResearchTabPanels } from '../components/research/ResearchTabPanels'
import { PageHeader } from '../components/ui/PageHeader'
import { WorkspacePage } from '../components/ui/WorkspacePage'
import { useGameContext } from '../context/ResearchContext'

/** Phase C — player investigation workspace at `/research`. */
export function ResearchWorkspace() {
  const { selection, matchupLabel } = useGameContext()

  return (
    <WorkspacePage>
      <PageHeader
        kicker="Research"
        title={selection.player?.name ?? 'Player workspace'}
        accent={matchupLabel ?? undefined}
        description="Continuous investigation session · context from Today travels with you"
      />

      <PlayerSummaryCard />
      <ResearchTabPanels />
    </WorkspacePage>
  )
}
