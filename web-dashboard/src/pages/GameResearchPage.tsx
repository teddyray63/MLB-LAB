import { Link, useParams } from 'react-router-dom'
import { PlaceholderPage } from '../components/ui/PlaceholderPage'
import { Card } from '../components/ui/Card'
import { useExport } from '../context/ExportContext'

export function GameResearchPage() {
  const data = useExport()
  const { gameId } = useParams()
  const games = data.game_details ?? []

  return (
    <PlaceholderPage
      kicker="Game Research"
      title={gameId ? decodeURIComponent(gameId) : 'Select a game'}
      description="One selected game: pitchers, lineups, team splits, weather, and park."
      phase="Phase 1"
      legacyLinks={[
        { to: '/legacy/games', label: 'Game Hub', note: 'Pitcher splits, lineups, bullpen' },
        { to: '/legacy/splits', label: 'Team Splits', note: 'Platoon / BVP / day-night' },
      ]}
    >
      {!gameId && games.length > 0 && (
        <Card title="Games" subtitle="Pick a game to research">
          <div className="flex flex-wrap gap-2">
            {games.map((g) => (
              <Link
                key={g.game_id}
                to={`/game/${encodeURIComponent(g.game_id)}`}
                className="rounded-md border border-[#30363D] bg-[#0D1117] px-3 py-1.5 text-xs font-medium text-[#F0F6FC] transition-colors hover:bg-[#161B22]"
              >
                {g.away_team} @ {g.home_team}
              </Link>
            ))}
          </div>
        </Card>
      )}
    </PlaceholderPage>
  )
}
