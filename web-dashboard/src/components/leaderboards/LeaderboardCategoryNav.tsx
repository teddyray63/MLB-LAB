import { useCallback } from 'react'
import {
  LEADERBOARD_CATEGORY_GROUPS,
  type LeaderboardCategory,
} from '../../types/leaderboard'

interface LeaderboardCategoryNavProps {
  category: LeaderboardCategory
  onCategoryChange: (category: LeaderboardCategory) => void
}

function categoryFromTabId(tabId: string): LeaderboardCategory | null {
  const prefix = 'leaderboard-tab-'
  if (!tabId.startsWith(prefix)) return null
  return tabId.slice(prefix.length) as LeaderboardCategory
}

export function LeaderboardCategoryNav({
  category,
  onCategoryChange,
}: LeaderboardCategoryNavProps) {
  const handleKeyDown = useCallback(
    (event: React.KeyboardEvent<HTMLButtonElement>) => {
      const tablist = event.currentTarget.closest('[role="tablist"]')
      if (!tablist) return

      const tabs = Array.from(
        tablist.querySelectorAll<HTMLButtonElement>('[role="tab"]'),
      )
      const currentIndex = tabs.indexOf(event.currentTarget)
      if (currentIndex === -1) return

      let nextIndex: number | null = null
      if (event.key === 'ArrowRight' || event.key === 'ArrowDown') {
        nextIndex = (currentIndex + 1) % tabs.length
      } else if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') {
        nextIndex = (currentIndex - 1 + tabs.length) % tabs.length
      } else if (event.key === 'Home') {
        nextIndex = 0
      } else if (event.key === 'End') {
        nextIndex = tabs.length - 1
      }
      if (nextIndex == null) return

      event.preventDefault()
      const nextTab = tabs[nextIndex]
      nextTab.focus()
      const nextCategory = categoryFromTabId(nextTab.id)
      if (nextCategory) onCategoryChange(nextCategory)
    },
    [onCategoryChange],
  )

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
                  onKeyDown={handleKeyDown}
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
