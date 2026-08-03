import { useMemo, useState } from 'react'
import { boardTeams, CategoryBoardTable } from '../components/CategoryBoardTable'
import { Card } from '../components/ui/Card'
import { SectionBanner } from '../components/ui/SectionBanner'
import { useExport } from '../context/ExportContext'
import { CATEGORY_LABELS, PLAY_CATEGORIES, type PlayCategory } from '../types/slate'

export function CategoryBoardsPage() {
  const data = useExport()
  const [teamFilter, setTeamFilter] = useState('')

  const allTeams = useMemo(() => {
    const teams = new Set<string>()
    for (const category of PLAY_CATEGORIES) {
      for (const team of boardTeams(data.category_boards[category])) {
        teams.add(team)
      }
    }
    return [...teams].sort()
  }, [data.category_boards])

  const totalRows = PLAY_CATEGORIES.reduce(
    (n, category) => n + data.category_boards[category].length,
    0,
  )

  return (
    <div className="space-y-5">
      <div className="flex flex-wrap items-end justify-between gap-4">
        <div>
          <p className="text-xs font-medium uppercase tracking-[0.12em] text-[#8B949E]">
            Category Boards
          </p>
          <h2 className="text-2xl font-bold tracking-tight">{data.date}</h2>
          <p className="mt-1 text-sm text-[#8B949E]">
            {totalRows > 0
              ? 'Top 20 per category · full stat columns · sortable tables'
              : 'No ranked rows are available in the current export'}
          </p>
        </div>
        <label className="flex items-center gap-2 text-xs text-[#8B949E]">
          Filter by team
          <select
            value={teamFilter}
            onChange={(e) => setTeamFilter(e.target.value)}
            className="rounded-md border border-[#30363D] bg-[#161B22] px-2 py-1.5 text-xs text-[#F0F6FC]"
          >
            <option value="">All teams</option>
            {allTeams.map((team) => (
              <option key={team} value={team}>
                {team}
              </option>
            ))}
          </select>
        </label>
      </div>

      <SectionBanner label="Category Boards" count={totalRows} />

      <div className="space-y-4">
        {PLAY_CATEGORIES.map((category) => (
          <CategoryBoardSection
            key={category}
            category={category}
            teamFilter={teamFilter}
          />
        ))}
      </div>
    </div>
  )
}

function CategoryBoardSection({
  category,
  teamFilter,
}: {
  category: PlayCategory
  teamFilter: string
}) {
  const data = useExport()
  const rows = data.category_boards[category]

  return (
    <Card
      title={CATEGORY_LABELS[category]}
      subtitle={
        rows.length > 0
          ? `Top ${rows.length} · ${category}`
          : 'No ranked rows in the current export'
      }
    >
      <CategoryBoardTable rows={rows} teamFilter={teamFilter} />
    </Card>
  )
}
