import { useMemo, useState } from 'react'
import { BullpenTable } from '../components/BullpenTable'
import { ExpectedLineupTable } from '../components/ExpectedLineupTable'
import { GameContextStrip } from '../components/GameContextStrip'
import { PitcherPlatoonTable } from '../components/PitcherPlatoonTable'
import { PitcherSituationTable } from '../components/PitcherSituationTable'
import { SpInningSplitsTable } from '../components/SpInningSplitsTable'
import { Card } from '../components/ui/Card'
import { SectionBanner } from '../components/ui/SectionBanner'
import { useExport } from '../context/ExportContext'
import type { GameDetail, PitchMixEntry } from '../types/slate'

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

function PitcherBlock({
  name,
  situation,
  platoon,
  inningSplits,
}: {
  name: string
  situation: GameDetail['away_sp_situation']
  platoon: GameDetail['away_sp_platoon']
  inningSplits: GameDetail['away_sp_inning_splits']
}) {
  return (
    <div className="space-y-4">
      <h4 className="text-sm font-semibold text-[#F0F6FC]">{name || 'TBD'}</h4>
      <div>
        <p className="mb-2 text-[10px] font-semibold uppercase tracking-[0.12em] text-[#8B949E]">
          By situation
        </p>
        <PitcherSituationTable rows={situation ?? []} pitcherName={name} />
      </div>
      <div>
        <p className="mb-2 text-[10px] font-semibold uppercase tracking-[0.12em] text-[#8B949E]">
          vs RHB / vs LHB
        </p>
        <PitcherPlatoonTable rows={platoon ?? []} pitcherName={name} />
      </div>
      <div>
        <p className="mb-2 text-[10px] font-semibold uppercase tracking-[0.12em] text-[#8B949E]">
          Runs allowed through inning
        </p>
        <SpInningSplitsTable pitcher={name} rows={inningSplits} />
      </div>
    </div>
  )
}

function TeamSide({
  team,
  sp,
  pitchMix,
  lineup,
  bullpen,
  side,
}: {
  team: string
  sp: string
  pitchMix: GameDetail['away_pitch_mix']
  lineup: GameDetail['away_lineup']
  bullpen: GameDetail['away_bullpen']
  side: 'Away' | 'Home'
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
        <ExpectedLineupTable rows={lineup ?? []} />
      </Card>

      <Card
        title="Bullpen (last 4 days)"
        subtitle="Flagged = 3+ appearances or pitched yesterday"
      >
        <BullpenTable rows={bullpen} />
      </Card>
    </div>
  )
}

export function GameHubPage() {
  const data = useExport()
  const games = data.game_details ?? []
  const [gameId, setGameId] = useState(games[0]?.game_id ?? '')

  const selected = useMemo(
    () => games.find((g) => g.game_id === gameId) ?? games[0],
    [games, gameId],
  )

  if (!games.length || !selected) {
    return (
      <div className="space-y-5">
        <div>
          <p className="text-xs font-medium uppercase tracking-[0.12em] text-[#8B949E]">
            Game Hub
          </p>
          <h2 className="text-2xl font-bold tracking-tight">{data.date}</h2>
        </div>
        <Card title="No games" subtitle="game_details is empty in today's export">
          <p className="text-sm text-[#8B949E]">
            Re-run the Python export to populate per-game hitter pools, pitch mix, and bullpen.
          </p>
        </Card>
      </div>
    )
  }

  return (
    <div className="space-y-5">
      <div className="flex flex-wrap items-end justify-between gap-4">
        <div>
          <p className="text-xs font-medium uppercase tracking-[0.12em] text-[#8B949E]">
            Game Hub
          </p>
          <h2 className="text-2xl font-bold tracking-tight">{data.date}</h2>
          <p className="mt-1 text-sm text-[#8B949E]">
            Game context · pitcher splits · expected lineups · bullpen
          </p>
        </div>
        <label className="flex items-center gap-2 text-xs text-[#8B949E]">
          Game
          <select
            value={selected.game_id}
            onChange={(e) => setGameId(e.target.value)}
            className="min-w-[16rem] rounded-md border border-[#30363D] bg-[#161B22] px-2 py-1.5 text-xs text-[#F0F6FC]"
          >
            {games.map((g) => (
              <option key={g.game_id} value={g.game_id}>
                {g.away_team} @ {g.home_team}
              </option>
            ))}
          </select>
        </label>
      </div>

      <SectionBanner label={selected.game_id} />

      <Card title="Game context" subtitle={`${selected.away_team} @ ${selected.home_team}`}>
        <GameContextStrip
          awayTeam={selected.away_team}
          homeTeam={selected.home_team}
          context={selected.context}
        />
      </Card>

      <Card
        title="Pitcher splits by situation"
        subtitle={`${selected.away_sp} vs ${selected.home_sp} · 120-day Statcast`}
      >
        <div className="grid gap-6 lg:grid-cols-2">
          <PitcherBlock
            name={selected.away_sp}
            situation={selected.away_sp_situation}
            platoon={selected.away_sp_platoon}
            inningSplits={selected.away_sp_inning_splits}
          />
          <PitcherBlock
            name={selected.home_sp}
            situation={selected.home_sp_situation}
            platoon={selected.home_sp_platoon}
            inningSplits={selected.home_sp_inning_splits}
          />
        </div>
      </Card>

      <Card
        title={`${selected.away_team} @ ${selected.home_team}`}
        subtitle="Expected batting orders · SP pitch mix · bullpen usage"
      >
        <div className="grid gap-6 lg:grid-cols-2">
          <TeamSide
            side="Away"
            team={selected.away_team}
            sp={selected.away_sp}
            pitchMix={selected.away_pitch_mix}
            lineup={selected.away_lineup}
            bullpen={selected.away_bullpen}
          />
          <TeamSide
            side="Home"
            team={selected.home_team}
            sp={selected.home_sp}
            pitchMix={selected.home_pitch_mix}
            lineup={selected.home_lineup}
            bullpen={selected.home_bullpen}
          />
        </div>
      </Card>
    </div>
  )
}
