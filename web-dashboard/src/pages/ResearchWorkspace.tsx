import { PlayerSummaryCard } from '../components/research/PlayerSummaryCard'
import { ResearchTabPanels } from '../components/research/ResearchTabPanels'
import { useGameContext } from '../context/ResearchContext'

/** Phase C — player investigation workspace at `/research`. */
export function ResearchWorkspace() {
  const { selection, matchupLabel } = useGameContext()

  return (
    <div className="space-y-5">
      <div>
        <p className="text-xs font-medium uppercase tracking-[0.12em] text-[#8B949E]">
          Research
        </p>
        <h2 className="text-2xl font-bold tracking-tight">
          {selection.player?.name ?? 'Player workspace'}
        </h2>
        {matchupLabel && (
          <p className="mt-1 text-sm text-[#58A6FF]">{matchupLabel}</p>
        )}
        <p className="mt-1 text-sm text-[#8B949E]">
          Continuous investigation session · context from Today travels with you
        </p>
      </div>

      <PlayerSummaryCard />
      <ResearchTabPanels />
    </div>
  )
}
