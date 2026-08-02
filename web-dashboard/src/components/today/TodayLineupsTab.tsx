import type { GameDetail, PitchMixEntry } from '../../types/slate'
import { BullpenTable } from '../BullpenTable'
import { ExpectedLineupTable } from '../ExpectedLineupTable'
import { Card } from '../ui/Card'
import { useExport } from '../../context/ExportContext'
import { useGameContext } from '../../context/ResearchContext'
import type { TeamSide } from '../../types/research'

function normalizePitchMix(pitches: GameDetail['away_pitch_mix']): PitchMixEntry[] {
  if (!pitches?.length) return []
  return pitches.map((entry) => {
    if (typeof entry === 'string') return { pitch: entry, usage_pct: null }
    return entry
  })
}

function PitchMixChips({ pitches }: { pitches: GameDetail['away_pitch_mix'] }) {
  const items = normalizePitchMix(pitches)
  if (!items.length) {
    return <span className="text-xs text-[#6E7681]">No pitch mix</span>
  }
  return (
    <div className="flex flex-wrap gap-1.5">
      {items.map(({ pitch, usage_pct }) => {
        const pctLabel =
          usage_pct == null || Number.isNaN(usage_pct)
            ? null
            : `${((usage_pct <= 1 ? usage_pct * 100 : usage_pct)).toFixed(0)}%`
        return (
          <span
            key={pitch}
            className="rounded border border-[#30363D] bg-[#0D1117] px-2 py-0.5 font-mono text-xs text-[#58A6FF]"
          >
            {pitch}
            {pctLabel && <span className="ml-1 text-[#8B949E]">{pctLabel}</span>}
          </span>
        )
      })}
    </div>
  )
}

function lineupSourceNote(rows: GameDetail['away_lineup']): string {
  if (!rows?.length) return '120-day Statcast season line'
  const status = rows[0]?.status ?? ''
  if (status.includes('PA order')) {
    return 'Projected order · top 9 by PA from team_hitter_pool (no lineups_override.csv entry for this team)'
  }
  return 'Order from lineups_override.csv · 120-day Statcast season line'
}

function TeamLineupSide({
  team,
  sp,
  pitchMix,
  lineup,
  bullpen,
  side,
  teamSide,
}: {
  team: string
  sp: string
  pitchMix: GameDetail['away_pitch_mix']
  lineup: GameDetail['away_lineup']
  bullpen: GameDetail['away_bullpen']
  side: 'Away' | 'Home'
  teamSide: TeamSide
}) {
  return (
    <div className="space-y-3">
      <div className="flex flex-wrap items-start justify-between gap-3">
        <div>
          <p className="text-[10px] font-semibold uppercase tracking-[0.14em] text-[#8B949E]">
            {side}
          </p>
          <h3 className="text-sm font-semibold text-[#F0F6FC]">{team}</h3>
          <p className="mt-0.5 text-xs text-[#8B949E]">SP · {sp || '—'}</p>
        </div>
        <div className="text-right">
          <p className="mb-1 text-[10px] font-semibold uppercase tracking-[0.14em] text-[#8B949E]">
            Pitch mix
          </p>
          <PitchMixChips pitches={pitchMix} />
        </div>
      </div>

      <Card title="Expected batting order" subtitle={lineupSourceNote(lineup)}>
        <ExpectedLineupTable rows={lineup ?? []} teamSide={teamSide} />
      </Card>

      <Card title="Bullpen (last 4 days)" subtitle="Flagged = 3+ appearances or pitched yesterday">
        <BullpenTable rows={bullpen} />
      </Card>
    </div>
  )
}

function useSelectedGameDetail(): GameDetail | null {
  const data = useExport()
  const { selection } = useGameContext()
  if (selection.gamePk == null) return null
  return data.game_details?.find((g) => g.game_pk === selection.gamePk) ?? null
}

export function TodayLineupsTab() {
  const detail = useSelectedGameDetail()

  if (!detail) {
    return (
      <Card title="Lineups" subtitle="Select a game">
        <p className="text-sm text-[#8B949E]">No lineup data until a game is selected.</p>
      </Card>
    )
  }

  return (
    <Card
      title={`${detail.away_team} @ ${detail.home_team}`}
      subtitle="Expected batting orders · SP pitch mix · bullpen usage"
    >
      <div className="grid gap-6 lg:grid-cols-2">
        <TeamLineupSide
          side="Away"
          team={detail.away_team}
          sp={detail.away_sp}
          pitchMix={detail.away_pitch_mix}
          lineup={detail.away_lineup}
          bullpen={detail.away_bullpen}
          teamSide="away"
        />
        <TeamLineupSide
          side="Home"
          team={detail.home_team}
          sp={detail.home_sp}
          pitchMix={detail.home_pitch_mix}
          lineup={detail.home_lineup}
          bullpen={detail.home_bullpen}
          teamSide="home"
        />
      </div>
    </Card>
  )
}
