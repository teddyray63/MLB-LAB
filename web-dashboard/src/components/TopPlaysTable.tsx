import { TierBadge } from './ui/TierBadge'
import { HitterLink } from './ui/HitterLink'
import { fmtKeyVal, fmtScore } from '../design/format'
import type { TopPlay } from '../types/slate'
import type { ReactNode } from 'react'

export type TopPlayRow = TopPlay & {
  category?: string
}

interface TopPlaysTableProps {
  plays: TopPlayRow[]
  showCategory?: boolean
  emptyMessage?: string
  /** Custom hitter cell — used by leaderboards for row-scoped research navigation */
  renderHitter?: (play: TopPlayRow) => ReactNode
}

export function TopPlaysTable({
  plays,
  showCategory = false,
  emptyMessage = 'No plays',
  renderHitter,
}: TopPlaysTableProps) {
  const headers = [
    'Rank',
    ...(showCategory ? ['Category'] : []),
    'Hitter',
    'Team',
    'Game',
    'Opp SP',
    'Pitch',
    'Score',
    'Tier',
    'Key Stat',
    'Key Val',
  ]

  return (
    <div className="overflow-auto rounded-md border border-[#21262D]">
      <table className="w-full min-w-[960px] border-collapse text-left">
        <thead className="sticky top-0 z-10 bg-[#161B22]">
          <tr className="border-b border-[#30363D]">
            {headers.map((label) => (
              <th
                key={label}
                className="whitespace-nowrap px-2 py-2 text-[10px] font-semibold uppercase tracking-wider text-[#8B949E]"
              >
                {label}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {plays.length === 0 ? (
            <tr>
              <td colSpan={headers.length} className="px-2 py-4 text-center text-xs text-[#6E7681]">
                {emptyMessage}
              </td>
            </tr>
          ) : (
            plays.map((play, index) => (
              <tr
                key={`${play.category ?? 'row'}-${play.rank}-${play.hitter}-${index}`}
                className="border-b border-[#21262D] transition-colors hover:bg-[#1C2128]"
              >
                <td className="px-2 py-1.5 text-xs tabular-nums text-[#6E7681]">{play.rank}</td>
                {showCategory && (
                  <td className="px-2 py-1.5 text-xs font-medium text-[#58A6FF]">{play.category}</td>
                )}
                <td className="px-2 py-1.5 text-xs font-medium">
                  {renderHitter ? (
                    renderHitter(play)
                  ) : (
                    <HitterLink name={play.hitter} />
                  )}
                </td>
                <td className="px-2 py-1.5 text-xs text-[#C9D1D9]">{play.team}</td>
                <td
                  className="max-w-[180px] truncate px-2 py-1.5 text-xs text-[#8B949E]"
                  title={play.game}
                >
                  {play.game}
                </td>
                <td className="px-2 py-1.5 text-xs text-[#C9D1D9]">{play.opp_sp}</td>
                <td className="px-2 py-1.5 text-xs font-mono text-[#58A6FF]">{play.pitch}</td>
                <td className="px-2 py-1.5 text-xs tabular-nums text-[#F0F6FC]">
                  {fmtScore(play.score)}
                </td>
                <td className="px-2 py-1.5">
                  <TierBadge tier={play.tier} />
                </td>
                <td className="px-2 py-1.5 text-xs text-[#8B949E]">{play.key_stat}</td>
                <td className="px-2 py-1.5 text-xs tabular-nums text-[#F0F6FC]">
                  {fmtKeyVal(play.key_stat, play.key_val)}
                </td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  )
}
