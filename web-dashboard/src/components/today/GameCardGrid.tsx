import { useGameContext } from '../../context/ResearchContext'
import { GameCard } from './GameCard'

/** Slate picker — delegates selection to ResearchContextHeader via setGame(). */
export function GameCardGrid() {
  const { slateGames, selection, setGame } = useGameContext()

  if (!slateGames.length) {
    return (
      <p className="text-sm text-[#8B949E]">
        No games on today&apos;s slate — re-run the export to populate{' '}
        <code className="rounded bg-[#21262D] px-1">games</code>.
      </p>
    )
  }

  return (
    <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
      {slateGames.map((game) => {
        const pk = game.game_pk
        if (pk == null) return null
        return (
          <GameCard
            key={pk}
            game={game}
            selected={selection.gamePk === pk}
            onSelect={() => setGame(pk)}
          />
        )
      })}
    </div>
  )
}
