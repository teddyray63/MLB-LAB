import type { GameContext, RecentGame, TeamRecord } from '../types/slate'

function fmtRecord(rec: TeamRecord | null | undefined): string {
  if (!rec || rec.wins == null || rec.losses == null) return '—'
  const pct = rec.pct ? ` (${rec.pct})` : ''
  return `${rec.wins}-${rec.losses}${pct}`
}

function LastFive({ label, games }: { label: string; games: RecentGame[] }) {
  if (!games.length) {
    return (
      <div>
        <p className="mb-1 text-[10px] font-semibold uppercase tracking-[0.12em] text-[#8B949E]">
          {label} · L5
        </p>
        <p className="text-xs text-[#6E7681]">No recent results in export</p>
      </div>
    )
  }
  return (
    <div>
      <p className="mb-1 text-[10px] font-semibold uppercase tracking-[0.12em] text-[#8B949E]">
        {label} · L5
      </p>
      <ul className="space-y-0.5">
        {games.map((g) => (
          <li key={`${g.date}-${g.opponent}`} className="text-xs text-[#F0F6FC]">
            <span
              className={`mr-1.5 inline-block w-4 font-bold ${
                g.result === 'W' ? 'text-[#3FB950]' : g.result === 'L' ? 'text-[#F85149]' : 'text-[#8B949E]'
              }`}
            >
              {g.result}
            </span>
            <span className="text-[#8B949E]">{g.date.slice(5)}</span>
            <span className="mx-1 text-[#6E7681]">·</span>
            {g.is_home ? 'vs' : '@'} {g.opponent}
            <span className="ml-1 tabular-nums text-[#8B949E]">{g.score}</span>
          </li>
        ))}
      </ul>
    </div>
  )
}

interface GameContextStripProps {
  awayTeam: string
  homeTeam: string
  context: GameContext | undefined
}

export function GameContextStrip({ awayTeam, homeTeam, context }: GameContextStripProps) {
  if (!context) {
    return (
      <p className="text-xs text-[#6E7681]">
        Game context unavailable — re-run export with MLB Stats API access
      </p>
    )
  }

  const weather = context.weather
  const weatherParts: string[] = []
  if (weather?.condition) weatherParts.push(weather.condition)
  if (weather?.temp) weatherParts.push(`${weather.temp}°F`)
  if (weather?.wind) weatherParts.push(`Wind ${weather.wind}`)

  return (
    <div className="space-y-4">
      <div className="flex flex-wrap gap-x-8 gap-y-2 text-sm">
        <div>
          <span className="text-[#8B949E]">{awayTeam}</span>
          <span className="ml-2 font-semibold tabular-nums text-[#F0F6FC]">
            {fmtRecord(context.away_record)}
          </span>
        </div>
        <div>
          <span className="text-[#8B949E]">{homeTeam}</span>
          <span className="ml-2 font-semibold tabular-nums text-[#F0F6FC]">
            {fmtRecord(context.home_record)}
          </span>
        </div>
        {context.park && (
          <div className="text-[#8B949E]">
            Park · <span className="text-[#F0F6FC]">{context.park}</span>
          </div>
        )}
        {weatherParts.length > 0 && (
          <div className="text-[#8B949E]">
            Weather · <span className="text-[#F0F6FC]">{weatherParts.join(' · ')}</span>
          </div>
        )}
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        <LastFive label={awayTeam} games={context.away_last5 ?? []} />
        <LastFive label={homeTeam} games={context.home_last5 ?? []} />
      </div>
    </div>
  )
}
