import { GameCardGrid } from '../components/today/GameCardGrid'
import { TodayTabPanels } from '../components/today/TodayTabPanels'
import { PageHeader } from '../components/ui/PageHeader'
import { SectionLabel } from '../components/ui/SectionLabel'
import { WorkspacePage } from '../components/ui/WorkspacePage'
import { useGameContext } from '../context/ResearchContext'

export function TodayPage() {
  const { selection, matchupLabel } = useGameContext()

  return (
    <WorkspacePage>
      <PageHeader
        kicker="Today"
        title={selection.date}
        accent={matchupLabel ?? undefined}
        description="Game-first workspace · use the header for date, game, and filters"
      />

      <section aria-labelledby="today-slate-label" className="space-y-3">
        <SectionLabel id="today-slate-label">Slate</SectionLabel>
        <GameCardGrid />
      </section>

      <TodayTabPanels />
    </WorkspacePage>
  )
}
