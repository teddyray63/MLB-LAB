import { GameCardGrid } from '../components/today/GameCardGrid'
import { TodayTabPanels } from '../components/today/TodayTabPanels'
import { useGameContext } from '../context/ResearchContext'

export function TodayPage() {
  const { selection, matchupLabel } = useGameContext()

  return (
    <div className="space-y-5">
      <div>
        <p className="text-xs font-medium uppercase tracking-[0.12em] text-[#8B949E]">Today</p>
        <h2 className="text-2xl font-bold tracking-tight">{selection.date}</h2>
        {matchupLabel && (
          <p className="mt-1 text-sm text-[#58A6FF]">{matchupLabel}</p>
        )}
        <p className="mt-1 text-sm text-[#8B949E]">
          Game-first workspace · use the header for date, game, and filters
        </p>
      </div>

      <section aria-label="Slate games">
        <h3 className="mb-3 text-[10px] font-semibold uppercase tracking-[0.14em] text-[#8B949E]">
          Slate
        </h3>
        <GameCardGrid />
      </section>

      <TodayTabPanels />
    </div>
  )
}
