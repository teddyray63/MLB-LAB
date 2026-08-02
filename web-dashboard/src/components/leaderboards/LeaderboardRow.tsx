import { useExport } from '../../context/ExportContext'
import { useOptionalGameContext } from '../../context/ResearchContext'
import { inferTeamSide } from '../../lib/leaderboardData'
import type { HitterRow, TopPlay } from '../../types/slate'

type LeaderboardRowData = Pick<
  HitterRow | TopPlay,
  'hitter' | 'team' | 'game_pk' | 'game' | 'opp_sp'
>

/** Single leaderboard row player link — opens research with row-resolved context. */
export function LeaderboardPlayerLink({ row }: { row: LeaderboardRowData }) {
  const exportData = useExport()
  const gameCtx = useOptionalGameContext()

  if (!row.hitter) return <span>—</span>

  const linkClass =
    'text-left text-[#F0F6FC] hover:text-[#58A6FF] hover:underline font-medium'

  if (!gameCtx) {
    return <span className={linkClass}>{row.hitter}</span>
  }

  const side = inferTeamSide(exportData, row)
  const rowGamePk = row.game_pk ?? null
  const rowPitcher = row.opp_sp && row.opp_sp !== 'TBD' ? row.opp_sp : undefined

  return (
    <button
      type="button"
      onClick={() =>
        gameCtx.openResearch({
          player: row.hitter,
          game: rowGamePk,
          side,
          pitcher: rowPitcher,
          tab: 'overview',
        })
      }
      className={linkClass}
    >
      {row.hitter}
    </button>
  )
}
