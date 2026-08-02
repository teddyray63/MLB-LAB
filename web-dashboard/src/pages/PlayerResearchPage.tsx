import { useParams } from 'react-router-dom'
import { PlaceholderPage } from '../components/ui/PlaceholderPage'

export function PlayerResearchPage() {
  const { playerId } = useParams()
  return (
    <PlaceholderPage
      kicker="Player Research"
      title={playerId ? decodeURIComponent(playerId) : 'Player search'}
      description="Season summary, game log, splits, pitch mix, zones, batted balls, and bat tracking."
      phase="Phase 1"
      legacyLinks={[
        { to: '/legacy/player', label: 'Player Matchup', note: 'Splits, pitch mix, zone heatmap' },
        { to: '/legacy/batted-balls', label: 'Batted Balls', note: 'EV/LA scatter + profile' },
      ]}
    />
  )
}
