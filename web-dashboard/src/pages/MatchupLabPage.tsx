import { useParams } from 'react-router-dom'
import { ResearchWorkspace } from './ResearchWorkspace'

/** Matchup Lab + Research workspace — `/research` and `/matchup` routes. */
export function MatchupLabPage() {
  const { gameId, playerId } = useParams()

  if (gameId && playerId) {
    return (
      <div className="space-y-6">
        <ResearchWorkspace />
        <p className="text-[10px] text-[#6E7681]">
          Deep link: {decodeURIComponent(playerId)} · {decodeURIComponent(gameId)} — use header
          controls if context is incomplete.
        </p>
      </div>
    )
  }

  return <ResearchWorkspace />
}
