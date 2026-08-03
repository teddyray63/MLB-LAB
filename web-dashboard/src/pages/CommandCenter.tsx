import { Card } from '../components/ui/Card'
import { SectionBanner } from '../components/ui/SectionBanner'
import { TopPlaysTable } from '../components/TopPlaysTable'
import type { DailyExport, PlayCategory } from '../types/slate'
import { CATEGORY_LABELS, PLAY_CATEGORIES } from '../types/slate'

interface CommandCenterProps {
  data: DailyExport
}

function CategorySection({
  category,
  plays,
}: {
  category: PlayCategory
  plays: DailyExport['top_plays'][PlayCategory]
}) {
  return (
    <Card
      title={CATEGORY_LABELS[category]}
      subtitle={
        plays.length > 0
          ? `Top ${plays.length} · ${category}`
          : 'No ranked rows in the current export'
      }
    >
      <TopPlaysTable plays={plays} />
    </Card>
  )
}

export function CommandCenter({ data }: CommandCenterProps) {
  const topPlayCount = PLAY_CATEGORIES.reduce(
    (total, category) => total + data.top_plays[category].length,
    0,
  )

  return (
    <div className="space-y-5">
      <div className="flex flex-wrap items-end justify-between gap-4">
        <div>
          <p className="text-xs font-medium uppercase tracking-[0.12em] text-[#8B949E]">
            Command Center
          </p>
          <h2 className="text-2xl font-bold tracking-tight">{data.date}</h2>
          <p className="mt-1 text-sm text-[#8B949E]">
            Loaded from{' '}
            <code className="rounded bg-[#21262D] px-1.5 py-0.5 text-xs text-[#58A6FF]">
              data/daily_export.json
            </code>
          </p>
        </div>
        <div className="flex gap-3">
          <div className="rounded-lg border border-[#30363D] bg-[#161B22] px-4 py-3 text-center">
            <p className="text-[10px] uppercase tracking-wide text-[#8B949E]">Categories</p>
            <p className="text-xl font-bold tabular-nums">{PLAY_CATEGORIES.length}</p>
          </div>
          <div className="rounded-lg border border-[#30363D] bg-[#161B22] px-4 py-3 text-center">
            <p className="text-[10px] uppercase tracking-wide text-[#8B949E]">Top Plays</p>
            <p className="text-xl font-bold tabular-nums">{topPlayCount}</p>
          </div>
        </div>
      </div>

      {data.games.length > 0 && (
        <>
          <SectionBanner label="Today's Slate" count={data.games.length} />
          <div className="grid gap-3 md:grid-cols-2 lg:grid-cols-3">
            {data.games.map((game) => (
              <div
                key={game.game_id}
                className="rounded-lg border border-[#30363D] bg-[#161B22] px-4 py-3"
              >
                <p className="text-sm font-semibold text-[#F0F6FC]">{game.game_id}</p>
                <div className="mt-2 grid grid-cols-2 gap-2 text-[11px]">
                  <div>
                    <span className="text-[#6E7681]">Away SP</span>
                    <p className="font-medium text-[#C9D1D9]">{game.away_sp}</p>
                  </div>
                  <div>
                    <span className="text-[#6E7681]">Home SP</span>
                    <p className="font-medium text-[#C9D1D9]">{game.home_sp}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </>
      )}

      <SectionBanner label="Top Plays" count={topPlayCount} />
      <div className="space-y-4">
        {PLAY_CATEGORIES.map((category) => (
          <CategorySection
            key={category}
            category={category}
            plays={data.top_plays[category]}
          />
        ))}
      </div>
    </div>
  )
}
