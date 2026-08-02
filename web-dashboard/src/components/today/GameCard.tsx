import { gameLabel } from '../../lib/researchResolver'
import type { Game } from '../../types/slate'

interface GameCardProps {
  game: Game
  selected: boolean
  onSelect: () => void
}

function formatStartTime(iso: string | null | undefined): string | null {
  if (!iso) return null
  try {
    const d = new Date(iso)
    return d.toLocaleTimeString(undefined, { hour: 'numeric', minute: '2-digit' })
  } catch {
    return null
  }
}

/** Compact slate card — selects game via shared GameContext (no local game state). */
export function GameCard({ game, selected, onSelect }: GameCardProps) {
  const start = formatStartTime(game.start_time_utc)
  const spLine =
    game.away_sp && game.home_sp ? `${game.away_sp} vs ${game.home_sp}` : null

  return (
    <button
      type="button"
      onClick={onSelect}
      className={`w-full rounded-lg border p-3 text-left transition-colors ${
        selected
          ? 'border-[#58A6FF] bg-[#1F6FEB22] ring-1 ring-[#58A6FF]/40'
          : 'border-[#30363D] bg-[#161B22] hover:border-[#484F58] hover:bg-[#21262D]'
      }`}
    >
      <p className="text-[10px] font-semibold uppercase tracking-[0.12em] text-[#8B949E]">
        {gameLabel(game)}
      </p>
      <p className="mt-1 text-sm font-semibold text-[#F0F6FC]">
        {game.away_team}
        <span className="mx-1.5 font-normal text-[#6E7681]">@</span>
        {game.home_team}
      </p>
      {spLine && <p className="mt-1 text-xs text-[#58A6FF]">{spLine}</p>}
      <div className="mt-2 flex flex-wrap gap-x-3 gap-y-0.5 text-[10px] text-[#8B949E]">
        {start && <span>{start}</span>}
        {game.status && <span>{game.status}</span>}
        {game.venue && <span className="truncate">{game.venue}</span>}
      </div>
    </button>
  )
}
