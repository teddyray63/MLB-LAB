import {
  LEADERBOARD_CATEGORY_GROUPS,
  type LeaderboardCategory,
} from '../../types/leaderboard'

interface LeaderboardCategoryNavProps {
  category: LeaderboardCategory
  onCategoryChange: (category: LeaderboardCategory) => void
}

export function LeaderboardCategoryNav({
  category,
  onCategoryChange,
}: LeaderboardCategoryNavProps) {
  return (
    <div className="space-y-3">
      <span className="text-[10px] font-semibold uppercase tracking-[0.14em] text-[#8B949E]">
        Category
      </span>
      <div className="flex flex-wrap gap-x-4 gap-y-2">
        {LEADERBOARD_CATEGORY_GROUPS.map((group) => (
          <div key={group.label} className="flex flex-wrap items-center gap-1">
            <span className="mr-1 text-[10px] text-[#484F58]">{group.label}:</span>
            {group.categories.map(({ key, label }) => (
              <button
                key={key}
                type="button"
                role="tab"
                aria-selected={category === key}
                onClick={() => onCategoryChange(key)}
                className={`rounded-md px-2.5 py-1 text-[11px] font-medium transition-colors ${
                  category === key
                    ? 'bg-[#1F6FEB33] text-[#58A6FF]'
                    : 'text-[#8B949E] hover:bg-[#21262D] hover:text-[#F0F6FC]'
                }`}
              >
                {label}
              </button>
            ))}
          </div>
        ))}
      </div>
    </div>
  )
}
