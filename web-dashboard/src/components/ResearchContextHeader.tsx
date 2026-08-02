import { Link, useLocation } from 'react-router-dom'
import { useGameContext, useFilters } from '../context/ResearchContext'
import { formatPitchName } from '../lib/pitchNames'
import { gameLabel } from '../lib/researchResolver'
import { TIMEFRAME_OPTIONS, SITUATION_OPTIONS } from '../types/research'
import type { Game } from '../types/slate'

export function ResearchContextHeader() {
  const location = useLocation()
  const {
    selection,
    slateGames,
    gamePlayers,
    setGame,
    setPlayer,
    setPitcher,
    setLeagueMode,
    matchupLabel: matchup,
  } = useGameContext()
  const { filters } = useFilters()

  const selectedGame = slateGames.find((g) => g.game_pk === selection.gamePk) ?? null
  const filterSummary = [
    TIMEFRAME_OPTIONS.find((o) => o.key === filters.timeframe)?.label ?? filters.timeframe,
    SITUATION_OPTIONS.find((o) => o.key === filters.situation)?.label ?? filters.situation,
    filters.pitchType ? formatPitchName(filters.pitchType, { compact: true }) : 'All Pitches',
  ].join(' · ')

  const preserveSearch = location.search

  return (
    <div className="space-y-3 rounded-lg border border-[#30363D] bg-[#161B22] p-4">
      {/* Row 1: primary context controls */}
      <div className="flex flex-wrap items-end gap-4">
        <div>
          <p className="mb-1 text-[10px] font-semibold uppercase tracking-[0.14em] text-[#8B949E]">
            Date
          </p>
          <p className="text-sm font-medium text-[#F0F6FC]">{selection.date}</p>
        </div>

        <label className="flex min-w-[12rem] flex-col gap-1">
          <span className="text-[10px] font-semibold uppercase tracking-[0.14em] text-[#8B949E]">
            Game
          </span>
          <select
            value={selection.gamePk ?? ''}
            onChange={(e) => setGame(Number(e.target.value))}
            className="rounded-md border border-[#30363D] bg-[#0D1117] px-2 py-1.5 text-xs text-[#F0F6FC]"
          >
            {slateGames.map((g: Game) => (
              <option key={g.game_pk ?? g.game_id} value={g.game_pk ?? ''}>
                {gameLabel(g)}
                {g.away_sp && g.home_sp ? ` · ${g.away_sp} vs ${g.home_sp}` : ''}
              </option>
            ))}
          </select>
        </label>

        {location.pathname.startsWith('/research') && (
          <>
            <label className="flex min-w-[10rem] flex-col gap-1">
              <span className="text-[10px] font-semibold uppercase tracking-[0.14em] text-[#8B949E]">
                Player
              </span>
              <select
                value={selection.player?.name ?? ''}
                onChange={(e) => {
                  const name = e.target.value
                  if (!name) return
                  const p = gamePlayers.find((x) => x.name === name)
                  setPlayer(name, p?.side)
                  setLeagueMode(false)
                }}
                className="rounded-md border border-[#30363D] bg-[#0D1117] px-2 py-1.5 text-xs text-[#F0F6FC]"
              >
                <option value="">Select player…</option>
                <optgroup label="Away">
                  {gamePlayers
                    .filter((p) => p.side === 'away')
                    .map((p) => (
                      <option key={`a-${p.name}`} value={p.name}>
                        {p.lineupOrder ? `#${p.lineupOrder} ` : ''}
                        {p.name}
                      </option>
                    ))}
                </optgroup>
                <optgroup label="Home">
                  {gamePlayers
                    .filter((p) => p.side === 'home')
                    .map((p) => (
                      <option key={`h-${p.name}`} value={p.name}>
                        {p.lineupOrder ? `#${p.lineupOrder} ` : ''}
                        {p.name}
                      </option>
                    ))}
                </optgroup>
              </select>
            </label>

            <label className="flex min-w-[10rem] flex-col gap-1">
              <span className="text-[10px] font-semibold uppercase tracking-[0.14em] text-[#8B949E]">
                Pitcher
              </span>
              <select
                value={selection.pitcher?.name ?? ''}
                onChange={(e) => setPitcher(e.target.value)}
                className="rounded-md border border-[#30363D] bg-[#0D1117] px-2 py-1.5 text-xs text-[#F0F6FC]"
              >
                {[selection.awaySp, selection.homeSp]
                  .filter((p): p is NonNullable<typeof p> => Boolean(p?.name))
                  .map((p) => (
                    <option key={p.name} value={p.name}>
                      {p.name}
                    </option>
                  ))}
              </select>
            </label>
          </>
        )}

        {matchup && (
          <div className="hidden lg:block">
            <p className="mb-1 text-[10px] font-semibold uppercase tracking-[0.14em] text-[#8B949E]">
              Matchup
            </p>
            <p className="text-sm font-medium text-[#58A6FF]">{matchup}</p>
          </div>
        )}

        <div className="hidden xl:block">
          <p className="mb-1 text-[10px] font-semibold uppercase tracking-[0.14em] text-[#8B949E]">
            Filters
          </p>
          <p className="text-xs text-[#8B949E]">{filterSummary}</p>
        </div>
      </div>

      {/* Breadcrumb */}
      <nav
        className="flex flex-wrap items-center gap-1 pt-1 text-xs text-[#8B949E]"
        aria-label="Breadcrumb"
      >
        <Link to={{ pathname: '/today', search: preserveSearch }} className="hover:text-[#58A6FF]">
          Today
        </Link>
        {selectedGame && (
          <>
            <span aria-hidden>→</span>
            <Link
              to={{ pathname: '/today', search: preserveSearch }}
              className="hover:text-[#58A6FF]"
            >
              {gameLabel(selectedGame)}
            </Link>
          </>
        )}
        {selection.player && (
          <>
            <span aria-hidden>→</span>
            <Link
              to={{ pathname: '/research', search: preserveSearch }}
              className="font-medium text-[#F0F6FC] hover:text-[#58A6FF]"
            >
              {selection.player.name}
            </Link>
          </>
        )}
      </nav>

      {selection.warnings.length > 0 && (
        <ul className="text-[10px] text-[#D29922]">
          {selection.warnings.map((w) => (
            <li key={w}>{w}</li>
          ))}
        </ul>
      )}
    </div>
  )
}
