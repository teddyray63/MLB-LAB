import { formatPitchName, pitchCodesFromMix } from '../lib/pitchNames'
import { useFilters } from '../context/ResearchContext'
import { useGameContext } from '../context/ResearchContext'
import { useExport } from '../context/ExportContext'
import { useMemo } from 'react'
import { TIMEFRAME_OPTIONS, SITUATION_OPTIONS } from '../types/research'
import { normalizePitchMixItems } from './PitchMixFilterChips'

export function FilterBar() {
  const { selection } = useGameContext()
  const { filters, setTimeframe, setSituation, setPitchType } = useFilters()
  const exportData = useExport()

  const pitchOptions = useMemo(() => {
    const detail = exportData.game_details?.find((g) => g.game_pk === selection.gamePk)
    if (!detail) return pitchCodesFromMix([])
    const codes = [
      ...normalizePitchMixItems(detail.away_pitch_mix).map((p) => p.pitch),
      ...normalizePitchMixItems(detail.home_pitch_mix).map((p) => p.pitch),
    ]
    return pitchCodesFromMix(codes)
  }, [exportData.game_details, selection.gamePk])

  return (
    <div className="flex flex-wrap items-end gap-4 rounded-lg border border-[#30363D] bg-[#0D1117] px-4 py-3">
      <fieldset className="flex flex-wrap items-center gap-2">
        <legend className="sr-only">Timeframe</legend>
        <span className="text-[10px] font-semibold uppercase tracking-[0.14em] text-[#8B949E]">
          Time
        </span>
        {TIMEFRAME_OPTIONS.map(({ key, label }) => {
          const support = filters.support.timeframe[key]
          const active = filters.timeframe === key
          return (
            <button
              key={key}
              type="button"
              disabled={!support.supported}
              title={support.reason}
              onClick={() => setTimeframe(key)}
              className={`rounded-md border px-2.5 py-1 text-[11px] font-medium transition-colors ${
                active
                  ? 'border-[#58A6FF] bg-[#1F6FEB33] text-[#58A6FF]'
                  : support.supported
                    ? 'border-[#30363D] text-[#8B949E] hover:bg-[#21262D] hover:text-[#F0F6FC]'
                    : 'cursor-not-allowed border-[#30363D] text-[#484F58] opacity-60'
              }`}
            >
              {label}
            </button>
          )
        })}
      </fieldset>

      <fieldset className="flex flex-wrap items-center gap-2">
        <legend className="sr-only">Situation</legend>
        <span className="text-[10px] font-semibold uppercase tracking-[0.14em] text-[#8B949E]">
          Situation
        </span>
        {SITUATION_OPTIONS.map(({ key, label }) => {
          const support = filters.support.situation[key]
          const active = filters.situation === key
          return (
            <button
              key={key}
              type="button"
              disabled={!support.supported}
              title={support.reason}
              onClick={() => setSituation(key)}
              className={`rounded-md border px-2.5 py-1 text-[11px] font-medium transition-colors ${
                active
                  ? 'border-[#58A6FF] bg-[#1F6FEB33] text-[#58A6FF]'
                  : support.supported
                    ? 'border-[#30363D] text-[#8B949E] hover:bg-[#21262D] hover:text-[#F0F6FC]'
                    : 'cursor-not-allowed border-[#30363D] text-[#484F58] opacity-60'
              }`}
            >
              {label}
            </button>
          )
        })}
      </fieldset>

      <label className="flex flex-col gap-1">
        <span className="text-[10px] font-semibold uppercase tracking-[0.14em] text-[#8B949E]">
          Pitch type
        </span>
        <select
          value={filters.pitchType ?? ''}
          onChange={(e) => setPitchType(e.target.value || null)}
          className="min-w-[12rem] rounded-md border border-[#30363D] bg-[#161B22] px-2 py-1.5 text-xs text-[#F0F6FC]"
        >
          <option value="">All Pitches</option>
          {pitchOptions.map((code) => (
            <option key={code} value={code}>
              {formatPitchName(code, { compact: true })}
            </option>
          ))}
        </select>
      </label>
    </div>
  )
}
