import { LEADERBOARD_SCOPES, type LeaderboardScope } from '../../types/leaderboard'

interface LeaderboardScopeControlProps {
  scope: LeaderboardScope
  onScopeChange: (scope: LeaderboardScope) => void
  hasValidGame: boolean
  dataWindow: string | null
}

export function LeaderboardScopeControl({
  scope,
  onScopeChange,
  hasValidGame,
  dataWindow,
}: LeaderboardScopeControlProps) {
  return (
    <div className="space-y-2">
      <div className="flex flex-wrap items-center gap-2">
        <span className="text-[10px] font-semibold uppercase tracking-[0.14em] text-[#8B949E]">
          Scope
        </span>
        <div
          className="flex flex-wrap gap-1"
          role="group"
          aria-label="Leaderboard scope"
        >
          {LEADERBOARD_SCOPES.map(({ key, label, description }) => {
            const disabled = key === 'game' && !hasValidGame
            return (
              <button
                key={key}
                type="button"
                title={description}
                disabled={disabled}
                aria-pressed={scope === key}
                onClick={() => onScopeChange(key)}
                className={`rounded-md px-3 py-1.5 text-[11px] font-medium transition-colors ${
                  scope === key
                    ? 'bg-[#1F6FEB33] text-[#58A6FF]'
                    : disabled
                      ? 'cursor-not-allowed text-[#484F58]'
                      : 'text-[#8B949E] hover:bg-[#21262D] hover:text-[#F0F6FC]'
                }`}
              >
                {label}
              </button>
            )
          })}
        </div>
      </div>
      {scope === 'league' && dataWindow && (
        <p className="text-[10px] text-[#8B949E]">
          Export Statcast window: {dataWindow}. This is the widest dataset in the daily export — not full-season league coverage.
        </p>
      )}
    </div>
  )
}
