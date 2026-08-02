import { Card } from '../ui/Card'
import { useResearchPlayerData } from '../../hooks/useResearchPlayerData'

export function PlayerSummaryCard() {
  const {
    selection,
    opponentTeam,
    recentTrend,
    gameDetail,
  } = useResearchPlayerData()

  const player = selection.player
  const pitcher = selection.pitcher ?? selection.opposingPitcher

  if (!player) {
    return (
      <Card title="Player summary" subtitle="Select a player in the header to begin">
        <p className="text-sm text-[#8B949E]">
          Open Today, pick a game, and click a hitter — or choose a player from the header dropdown.
        </p>
      </Card>
    )
  }

  const matchupLabel =
    opponentTeam && pitcher?.name
      ? `${player.team} vs ${opponentTeam} · ${pitcher.name}`
      : player.team

  return (
    <div className="rounded-lg border border-[#30363D] bg-[#161B22] p-4">
      <div className="flex flex-wrap items-start justify-between gap-4">
        <div>
          <p className="text-[10px] font-semibold uppercase tracking-[0.14em] text-[#8B949E]">
            Player
          </p>
          <h2 className="text-xl font-bold tracking-tight text-[#F0F6FC]">{player.name}</h2>
          <p className="mt-1 text-sm text-[#58A6FF]">{matchupLabel}</p>
        </div>
        {recentTrend && (
          <div className="text-right">
            <p className="text-[10px] font-semibold uppercase tracking-[0.14em] text-[#8B949E]">
              Recent
            </p>
            <p className="text-sm font-medium tabular-nums text-[#F0F6FC]">{recentTrend}</p>
          </div>
        )}
      </div>

      <dl className="mt-4 grid gap-3 sm:grid-cols-2 lg:grid-cols-5">
        <SummaryItem label="Team" value={player.team} />
        <SummaryItem label="Opponent" value={opponentTeam ?? '—'} />
        <SummaryItem label="Today's pitcher" value={pitcher?.name ?? 'TBD'} />
        <SummaryItem label="Hand" value={player.hand ?? '—'} />
        <SummaryItem
          label="Lineup"
          value={player.lineupOrder ? `#${player.lineupOrder}` : '—'}
        />
      </dl>

      {gameDetail && (
        <p className="mt-3 text-[10px] text-[#6E7681]">
          {gameDetail.game_id}
          {gameDetail.venue ? ` · ${gameDetail.venue}` : ''}
        </p>
      )}
    </div>
  )
}

function SummaryItem({ label, value }: { label: string; value: string }) {
  return (
    <div>
      <dt className="text-[10px] font-semibold uppercase tracking-[0.12em] text-[#8B949E]">
        {label}
      </dt>
      <dd className="mt-0.5 text-sm font-medium text-[#F0F6FC]">{value}</dd>
    </div>
  )
}
