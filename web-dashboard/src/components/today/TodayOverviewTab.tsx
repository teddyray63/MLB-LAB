import { GameContextStrip } from '../GameContextStrip'
import { Card } from '../ui/Card'
import { SectionBanner } from '../ui/SectionBanner'
import { useExport } from '../../context/ExportContext'
import { useGameContext } from '../../context/ResearchContext'
import type { GameDetail } from '../../types/slate'

function useSelectedGameDetail(): GameDetail | null {
  const data = useExport()
  const { selection } = useGameContext()
  if (selection.gamePk == null) return null
  return data.game_details?.find((g) => g.game_pk === selection.gamePk) ?? null
}

export function TodayOverviewTab() {
  const { selection, matchupLabel } = useGameContext()
  const detail = useSelectedGameDetail()

  if (!detail) {
    return (
      <Card title="No game selected" subtitle="Pick a game from the cards above or the header">
        <p className="text-sm text-[#8B949E]">
          game_details is empty or the selected game_pk is missing from the export.
        </p>
      </Card>
    )
  }

  return (
    <div className="space-y-5">
      <SectionBanner label={detail.game_id} />

      <Card
        title="Game context"
        subtitle={matchupLabel ?? `${detail.away_team} @ ${detail.home_team}`}
      >
        <GameContextStrip
          awayTeam={detail.away_team}
          homeTeam={detail.home_team}
          context={detail.context}
        />
      </Card>

      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <StatTile label="Away SP" value={detail.away_sp || 'TBD'} />
        <StatTile label="Home SP" value={detail.home_sp || 'TBD'} />
        <StatTile label="Export date" value={selection.date} />
        <StatTile
          label="Game PK"
          value={selection.gamePk != null ? String(selection.gamePk) : '—'}
          mono
        />
      </div>
    </div>
  )
}

function StatTile({
  label,
  value,
  mono = false,
}: {
  label: string
  value: string
  mono?: boolean
}) {
  return (
    <div className="rounded-lg border border-[#30363D] bg-[#161B22] px-4 py-3">
      <p className="text-[10px] font-semibold uppercase tracking-[0.12em] text-[#8B949E]">
        {label}
      </p>
      <p className={`mt-1 text-sm font-medium text-[#F0F6FC] ${mono ? 'font-mono text-xs' : ''}`}>
        {value}
      </p>
    </div>
  )
}
