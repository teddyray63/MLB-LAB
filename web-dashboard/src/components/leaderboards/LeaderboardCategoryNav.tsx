import { useCallback } from 'react'
import {
  LEADERBOARD_CATEGORY_GROUPS,
  LEADERBOARD_CATEGORIES,
  type LeaderboardCategory,
} from '../../types/leaderboard'

interface LeaderboardCategoryNavProps {
  category: LeaderboardCategory
  onCategoryChange: (category: LeaderboardCategory) => void
}

const ALL_CATEGORIES = LEADERBOARD_CATEGORIES

export function LeaderboardCategoryNav({
  category,
  onCategoryChange,
}: LeaderboardCategoryNavProps) {
  const focusCategory = useCallback(
    (index: number) => {
      const next = ALL_CATEGORIES[index]
      if (next) onCategoryChange(next)
    },
    [onCategoryChange],
  )

  const handleKeyDown = useCallback(
    (event: React.KeyboardEvent<HTMLButtonElement>, index: number) => {
      let nextIndex: number | null = null
      if (event.key === 'ArrowRight' || event.key === 'ArrowDown') {
        nextIndex = (index + 1) % ALL_CATEGORIES.length
      } else if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') {
        nextIndex = (index - 1 + ALL_CATEGORIES.length) % ALL_CATEGORIES.length
      } else if (event.key === 'Home') {
        nextIndex = 0
      } else if (event.key === 'End') {
        nextIndex = ALL_CATEGORIES.length - 1
      }
      if (nextIndex == null) return
      event.preventDefault()
      focusCategory(nextIndex)
      const tablist = event.currentTarget.closest('[role="tablist"]')
      const buttons = tablist?.querySelectorAll<HTMLButtonElement>('[role="tab"]')
      buttons?.[nextIndex]?.focus()
    },
    [focusCategory],
  )

  let tabIndex = 0

  return (
    <div className="space-y-3">
      <span
        id="leaderboard-category-label"
        className="text-[10px] font-semibold uppercase tracking-[0.14em] text-[#8B949E]"
      >
        Category
      </span>
      <div
        className="flex flex-wrap gap-x-4 gap-y-2"
        role="tablist"
        aria-labelledby="leaderboard-category-label"
      >
        {LEADERBOARD_CATEGORY_GROUPS.map((group) => (
          <div key={group.label} className="flex flex-wrap items-center gap-1">
            <span className="mr-1 text-[10px] text-[#484F58]">{group.label}:</span>
            {group.categories.map(({ key, label }) => {
              const index = tabIndex++
              const selected = category === key
              return (
                <button
                  key={key}
                  type="button"
                  role="tab"
                  id={`leaderboard-tab-${key}`}
                  aria-selected={selected}
                  tabIndex={selected ? 0 : -1}
                  onClick={() => onCategoryChange(key)}
                  onKeyDown={(event) => handleKeyDown(event, index)}
                  className={`rounded-md px-2.5 py-1 text-[11px] font-medium transition-colors ${
                    selected
                      ? 'bg-[#1F6FEB33] text-[#58A6FF]'
                      : 'text-[#8B949E] hover:bg-[#21262D] hover:text-[#F0F6FC]'
                  }`}
                >
                  {label}
                </button>
              )
            })}
          </div>
        ))}
      </div>
    </div>
  )
}
