import { CategoryBoardTable } from '../CategoryBoardTable'
import { GameLogChart } from '../GameLogChart'
import { ExitVeloScatter } from '../ExitVeloScatter'
import { BattedBallProfileCard } from '../BattedBallProfileCard'
import { PlayerDayNightTable } from '../PlayerDayNightTable'
import { TeamSplitsTable, type SplitKey } from '../TeamSplitsTable'
import { ZoneHeatmap } from '../ZoneHeatmap'
import { StatCell } from '../ui/StatCell'
import { ScoutingSummaryCard } from './ScoutingSummaryCard'
import { ResearchPanelShell } from './FilterContextNote'
import { useResearchPlayerData } from '../../hooks/useResearchPlayerData'
import { fmtInt, fmtMph, fmtPct, fmtRate } from '../../design/format'
import { battingRateToHeat, powerRateToHeat, rateToHeat, type HeatLevel } from '../../design/tokens'
import { formatPitchName } from '../../lib/pitchNames'
import type { SituationKey } from '../../types/research'
import { TIMEFRAME_OPTIONS, SITUATION_OPTIONS } from '../../types/research'

function NoPlayer() {
  return <p className="text-sm text-[#8B949E]">Select a player in the header to load this panel.</p>
}

function situationToSplitKey(situation: SituationKey): SplitKey {
  switch (situation) {
    case 'vlhp':
      return 'vs_lhp'
    case 'vrhp':
      return 'vs_rhp'
    case 'day':
      return 'day_split'
    case 'night':
      return 'night_split'
    default:
      return 'overall'
  }
}

function situationToPlayerSplit(situation: SituationKey): 'overall' | 'day_split' | 'night_split' {
  if (situation === 'day') return 'day_split'
  if (situation === 'night') return 'night_split'
  return 'overall'
}

function MetricTile({ label, value, heat }: { label: string; value: string; heat?: HeatLevel }) {
  return (
    <div className="rounded border border-[#30363D] bg-[#0D1117] px-3 py-2 text-center">
      <p className="text-[10px] text-[#8B949E]">{label}</p>
      {heat ? (
        <StatCell value={value} heat={heat} className="mt-1 justify-center" />
      ) : (
        <p className="mt-1 font-mono text-sm text-[#F0F6FC]">{value}</p>
      )}
    </div>
  )
}

export function ResearchOverviewTab() {
  const data = useResearchPlayerData()
  if (!data.playerName) return <ResearchPanelShell title="Overview"><NoPlayer /></ResearchPanelShell>

  const pitcher = data.selection.pitcher?.name ?? data.selection.opposingPitcher?.name ?? 'TBD'

  return (
    <ResearchPanelShell
      title="Overview"
      subtitle={`${data.playerName} vs ${pitcher} · ${data.matchupRows.length} pitch rows`}
    >
      <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
        <MetricTile label="xwOBA" value={fmtRate(data.aggregates.xwoba)} />
        <MetricTile label="wOBA" value={fmtRate(data.aggregates.woba)} />
        <MetricTile label="Barrel%" value={fmtPct(data.aggregates.barrelPct)} />
        <MetricTile label="Hard Hit%" value={fmtPct(data.aggregates.hardHitPct)} />
      </div>
      <p className="mt-4 text-xs text-[#8B949E]">
        Who is today&apos;s opponent?{' '}
        <span className="text-[#F0F6FC]">{data.opponentTeam ?? '—'}</span> · SP{' '}
        <span className="text-[#F0F6FC]">{pitcher}</span>
      </p>
      {data.recentTrend && (
        <p className="mt-2 text-xs text-[#8B949E]">
          Recent form: <span className="text-[#58A6FF]">{data.recentTrend}</span>
        </p>
      )}
    </ResearchPanelShell>
  )
}

export function ResearchMatchupTab() {
  const data = useResearchPlayerData()
  if (!data.playerName) return <ResearchPanelShell title="Matchup"><NoPlayer /></ResearchPanelShell>

  const pitcher = data.selection.pitcher?.name ?? data.selection.opposingPitcher?.name
  const rows = data.pitcherMatchupRows.length ? data.pitcherMatchupRows : data.matchupRows

  return (
    <ResearchPanelShell
      title="Matchup"
      subtitle={
        pitcher
          ? `${data.playerName} vs ${pitcher} · by pitch type`
          : `${data.playerName} · by pitch type`
      }
    >
      <CategoryBoardTable rows={rows} hideIdentity />
    </ResearchPanelShell>
  )
}

export function ResearchRecentGamesTab() {
  const data = useResearchPlayerData()
  if (!data.playerName) return <ResearchPanelShell title="Recent games"><NoPlayer /></ResearchPanelShell>

  return (
    <ResearchPanelShell title="Recent games" subtitle="Statcast game log · L5 / L10 / L20">
      <GameLogChart hitter={data.playerName} log={data.gameLog} />
    </ResearchPanelShell>
  )
}

export function ResearchSplitsTab() {
  const data = useResearchPlayerData()
  if (!data.playerName) return <ResearchPanelShell title="Splits"><NoPlayer /></ResearchPanelShell>

  const situation = data.filters.situation
  const sitLabel = SITUATION_OPTIONS.find((o) => o.key === situation)?.label ?? situation

  if (situation === 'vlhp' || situation === 'vrhp') {
    const split = situationToSplitKey(situation)
    const rows = data.teamSplitHitter ? [data.teamSplitHitter] : []
    return (
      <ResearchPanelShell title="Splits" subtitle={`${sitLabel} · team export splits`}>
        <TeamSplitsTable rows={rows} split={split} teamSide={data.selection.teamSide ?? undefined} />
      </ResearchPanelShell>
    )
  }

  const activeSplit = situationToPlayerSplit(situation)
  return (
    <ResearchPanelShell title="Splits" subtitle={`${sitLabel} · 120-day Statcast`}>
      <PlayerDayNightTable profile={data.dayNightProfile} activeSplit={activeSplit} />
    </ResearchPanelShell>
  )
}

export function ResearchPitchMatchupTab() {
  const data = useResearchPlayerData()
  if (!data.playerName) return <ResearchPanelShell title="Pitch matchup"><NoPlayer /></ResearchPanelShell>

  const pitchNote = data.filters.pitchType
    ? formatPitchName(data.filters.pitchType, { compact: true })
    : 'All pitches'

  return (
    <ResearchPanelShell
      title="Pitch matchup"
      subtitle={`Per-pitch vs opposing SP · ${pitchNote}`}
    >
      <CategoryBoardTable rows={data.pitcherMatchupRows} hideIdentity />
    </ResearchPanelShell>
  )
}

export function ResearchHeatmapsTab() {
  const data = useResearchPlayerData()
  if (!data.playerName) return <ResearchPanelShell title="Heatmaps"><NoPlayer /></ResearchPanelShell>

  return (
    <ResearchPanelShell title="Heatmaps" subtitle="Contact rate by pitch location">
      <ZoneHeatmap profile={data.zoneHeatmap} />
    </ResearchPanelShell>
  )
}

export function ResearchBattedBallsTab() {
  const data = useResearchPlayerData()
  if (!data.playerName) return <ResearchPanelShell title="Batted balls"><NoPlayer /></ResearchPanelShell>

  return (
    <div className="grid gap-5 lg:grid-cols-2">
      <ResearchPanelShell title="Exit velocity scatter" subtitle="Recent batted balls · color by result">
        <ExitVeloScatter hitter={data.playerName} battedBalls={data.battedBalls} />
      </ResearchPanelShell>
      <ResearchPanelShell title="Batted ball profile" subtitle="Spray, trajectory, distance">
        <BattedBallProfileCard profile={data.battedBallProfile} />
      </ResearchPanelShell>
    </div>
  )
}

export function ResearchSwingMetricsTab() {
  const data = useResearchPlayerData()
  if (!data.playerName) return <ResearchPanelShell title="Swing metrics"><NoPlayer /></ResearchPanelShell>

  const { aggregates } = data
  return (
    <ResearchPanelShell title="Swing metrics" subtitle="Bat tracking · PA-weighted across pitch rows">
      <div className="grid gap-3 sm:grid-cols-3">
        <MetricTile label="Bat Speed" value={fmtMph(aggregates.batSpeed)} />
        <MetricTile label="Squared Up%" value={fmtPct(aggregates.squaredUpPct)} />
        <MetricTile label="Blast%" value={fmtPct(aggregates.blastPct)} />
        <MetricTile label="Whiff%" value={fmtPct(aggregates.whiffPct)} />
        <MetricTile label="Sweet Spot%" value={fmtPct(aggregates.sweetSpotPct)} />
        <MetricTile label="Barrel%" value={fmtPct(aggregates.barrelPct)} />
      </div>
      <div className="mt-4">
        <CategoryBoardTable rows={data.matchupRows} hideIdentity />
      </div>
    </ResearchPanelShell>
  )
}

export function ResearchOutcomeProfileTab() {
  const data = useResearchPlayerData()
  if (!data.playerName) return <ResearchPanelShell title="Outcome profile"><NoPlayer /></ResearchPanelShell>

  const line = data.activeSplitLine
  const agg = data.aggregates

  const metrics = [
    { label: 'AVG', value: line?.avg ?? agg.avg, heat: battingRateToHeat(line?.avg ?? agg.avg) },
    { label: 'SLG', value: line?.slg ?? agg.slg, heat: powerRateToHeat(line?.slg ?? agg.slg) },
    { label: 'ISO', value: line?.iso ?? agg.iso, heat: powerRateToHeat(line?.iso ?? agg.iso) },
    { label: 'wOBA', value: line?.woba ?? agg.woba, heat: battingRateToHeat(line?.woba ?? agg.woba) },
    { label: 'xwOBA', value: agg.xwoba, heat: battingRateToHeat(agg.xwoba) },
    { label: 'Barrel%', value: line?.barrel_pct ?? agg.barrelPct, heat: rateToHeat((line?.barrel_pct ?? agg.barrelPct ?? 0) <= 1 ? (line?.barrel_pct ?? agg.barrelPct ?? 0) * 100 : (line?.barrel_pct ?? agg.barrelPct ?? 0)) },
    { label: 'Hard Hit%', value: line?.hard_hit_pct ?? agg.hardHitPct, heat: rateToHeat((line?.hard_hit_pct ?? agg.hardHitPct ?? 0) <= 1 ? (line?.hard_hit_pct ?? agg.hardHitPct ?? 0) * 100 : (line?.hard_hit_pct ?? agg.hardHitPct ?? 0)) },
  ]

  return (
    <ResearchPanelShell
      title="Outcome profile"
      subtitle={`${SITUATION_OPTIONS.find((o) => o.key === data.filters.situation)?.label ?? 'Overall'} · ${TIMEFRAME_OPTIONS.find((o) => o.key === data.filters.timeframe)?.label ?? 'Season'}`}
    >
      <div className="grid gap-3 sm:grid-cols-3 lg:grid-cols-4">
        {metrics.map(({ label, value, heat }) => (
          <MetricTile key={label} label={label} value={value != null ? (label.includes('%') ? fmtPct(value) : fmtRate(value)) : '—'} heat={heat} />
        ))}
      </div>
      {line?.pa != null && (
        <p className="mt-3 text-[10px] text-[#6E7681]">Split sample: {fmtInt(line.pa)} PA</p>
      )}
    </ResearchPanelShell>
  )
}

export function ResearchScoutingSummaryTab() {
  return <ScoutingSummaryCard />
}
