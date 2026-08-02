import { Link, useLocation } from 'react-router-dom'
import { useOptionalGameContext } from '../../context/ResearchContext'
import type { TeamSide } from '../../types/research'

interface HitterLinkProps {
  name: string
  className?: string
  /** Batter's team side in the selected game — forwarded to /research URL */
  side?: TeamSide
  /** Team name — used to infer side from shared game context when side is omitted */
  team?: string
  /** Row game_pk — overrides header selection (leaderboard/slate rows) */
  gamePk?: number | null
  /** Opposing SP from row — overrides inferred pitcher */
  pitcher?: string | null
  /** Force legacy `/legacy/player?name=` navigation even on new-IA routes */
  legacy?: boolean
}

function inferSide(
  team: string | undefined,
  awayTeam: string | null,
  homeTeam: string | null,
): TeamSide | undefined {
  if (!team) return undefined
  if (awayTeam && team === awayTeam) return 'away'
  if (homeTeam && team === homeTeam) return 'home'
  return undefined
}

/**
 * Hitter navigation:
 * - Legacy routes (`/legacy/*`) → `/legacy/player?name=` (unchanged legacy behavior)
 * - New IA routes → `openResearch()` preserving game, filters, side, and opposing SP
 */
export function HitterLink({
  name,
  className = '',
  side,
  team,
  gamePk,
  pitcher,
  legacy = false,
}: HitterLinkProps) {
  const location = useLocation()
  const gameCtx = useOptionalGameContext()

  if (!name) return <span className={className}>—</span>

  const useLegacy = legacy || location.pathname.startsWith('/legacy')
  const linkClass = `text-[#F0F6FC] hover:text-[#58A6FF] hover:underline ${className}`

  if (!useLegacy && gameCtx) {
    const resolvedSide =
      side ?? inferSide(team, gameCtx.selection.awayTeam, gameCtx.selection.homeTeam)
    const rowPitcher = pitcher && pitcher !== 'TBD' ? pitcher : undefined
    const opposingPitcher =
      rowPitcher ??
      (resolvedSide === 'away'
        ? gameCtx.selection.homeSp?.name
        : resolvedSide === 'home'
          ? gameCtx.selection.awaySp?.name
          : undefined)

    const resolvedGame =
      gamePk !== undefined ? gamePk : gameCtx.selection.gamePk

    return (
      <button
        type="button"
        onClick={() =>
          gameCtx.openResearch({
            player: name,
            game: resolvedGame,
            side: resolvedSide,
            pitcher: opposingPitcher ?? undefined,
            tab: 'overview',
          })
        }
        className={`text-left ${linkClass}`}
      >
        {name}
      </button>
    )
  }

  return (
    <Link
      to={`/legacy/player?name=${encodeURIComponent(name)}`}
      className={linkClass}
    >
      {name}
    </Link>
  )
}
