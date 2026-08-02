import { Card } from '../ui/Card'
import type { DataStatusSnapshot } from '../../lib/dataStatus'

export function WarningsPanel({ snapshot }: { snapshot: DataStatusSnapshot }) {
  const { exportWarnings, derivedWarnings, duplicateGamePks, allWarnings } = snapshot

  return (
    <Card
      title="Warnings"
      subtitle={
        allWarnings.length
          ? `${allWarnings.length} issue${allWarnings.length === 1 ? '' : 's'} from export_meta and derived checks`
          : 'No warnings detected'
      }
    >
      {exportWarnings.length > 0 && (
        <div className="mb-4">
          <h4 className="mb-2 text-[10px] font-semibold uppercase tracking-[0.12em] text-[#8B949E]">
            From export_meta.warnings
          </h4>
          <ul className="space-y-1.5 text-sm text-[#F0F6FC]">
            {exportWarnings.map((w) => (
              <li key={w} className="flex gap-2">
                <span className="text-[#D29922]" aria-hidden>
                  •
                </span>
                <span>{w}</span>
              </li>
            ))}
          </ul>
        </div>
      )}

      {derivedWarnings.length > 0 && (
        <div className="mb-4">
          <h4 className="mb-2 text-[10px] font-semibold uppercase tracking-[0.12em] text-[#8B949E]">
            Derived from export data
          </h4>
          <ul className="space-y-1.5 text-sm text-[#F0F6FC]">
            {derivedWarnings.map((w) => (
              <li key={w} className="flex gap-2">
                <span className="text-[#D29922]" aria-hidden>
                  •
                </span>
                <span>{w}</span>
              </li>
            ))}
          </ul>
        </div>
      )}

      {duplicateGamePks.length > 0 && (
        <div className="border-t border-[#30363D] pt-4">
          <h4 className="mb-2 text-[10px] font-semibold uppercase tracking-[0.12em] text-[#8B949E]">
            Duplicate game_pk detail
          </h4>
          {duplicateGamePks.map((dup) => (
            <div key={dup.gamePk} className="mb-3 last:mb-0">
              <p className="text-xs font-medium text-[#58A6FF]">
                game_pk {dup.gamePk} · {dup.count} entries
              </p>
              <ul className="mt-1 space-y-1 text-[11px] text-[#8B949E]">
                {dup.entries.map((e) => (
                  <li key={`${dup.gamePk}-${e.game_id}-${e.away_sp}`}>
                    {e.away_team} @ {e.home_team} · {e.away_sp} vs {e.home_sp}
                    {e.away_sp === 'TBD' || e.home_sp === 'TBD' ? ' (placeholder)' : ''}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      )}

      {allWarnings.length === 0 && (
        <p className="text-sm text-[#8B949E]">No export or derived warnings.</p>
      )}
    </Card>
  )
}
