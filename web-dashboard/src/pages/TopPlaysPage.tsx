import { useMemo } from 'react'
import { Card } from '../components/ui/Card'
import { SectionBanner } from '../components/ui/SectionBanner'
import { TopPlaysTable, type TopPlayRow } from '../components/TopPlaysTable'
import { useExport } from '../context/ExportContext'
import { CATEGORY_LABELS, PLAY_CATEGORIES } from '../types/slate'

export function TopPlaysPage() {
  const data = useExport()

  const allPlays = useMemo(() => {
    const rows: TopPlayRow[] = []
    for (const category of PLAY_CATEGORIES) {
      for (const play of data.top_plays[category]) {
        rows.push({ ...play, category: CATEGORY_LABELS[category] })
      }
    }
    return rows
  }, [data.top_plays])

  return (
    <div className="space-y-5">
      <div>
        <p className="text-xs font-medium uppercase tracking-[0.12em] text-[#8B949E]">Top Plays</p>
        <h2 className="text-2xl font-bold tracking-tight">{data.date}</h2>
        <p className="mt-1 text-sm text-[#8B949E]">
          {allPlays.length} plays · 5 per category · matches Excel Top Plays tab
        </p>
      </div>

      <SectionBanner label="All Categories" count={allPlays.length} />
      <Card title="Top Plays — Full Slate" subtitle="Rank, Category, Hitter, Team, Game, Opp SP, Pitch, Score, Tier, Key Stat, Key Val">
        <TopPlaysTable plays={allPlays} showCategory />
      </Card>

      <SectionBanner label="By Category" />
      <div className="space-y-4">
        {PLAY_CATEGORIES.map((category) => (
          <Card key={category} title={CATEGORY_LABELS[category]} subtitle="Top 5">
            <TopPlaysTable
              plays={data.top_plays[category].map((play) => ({
                ...play,
                category: CATEGORY_LABELS[category],
              }))}
            />
          </Card>
        ))}
      </div>
    </div>
  )
}
