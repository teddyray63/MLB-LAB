import { useEffect, useMemo, useState } from 'react'
import { useSearchParams } from 'react-router-dom'
import { CategoryBoardTable } from '../components/CategoryBoardTable'
import { GameLogChart } from '../components/GameLogChart'
import { PitchMixFilterChips } from '../components/PitchMixFilterChips'
import { PLAYER_SPLITS, PlayerDayNightTable, type PlayerSplitKey } from '../components/PlayerDayNightTable'
import { ZoneHeatmap } from '../components/ZoneHeatmap'
import { Card } from '../components/ui/Card'
import { SectionBanner } from '../components/ui/SectionBanner'
import { useExport } from '../context/ExportContext'

export function PlayerMatchupPage() {
  const data = useExport()
  const [searchParams] = useSearchParams()
  const [query, setQuery] = useState('')
  const [hitter, setHitter] = useState('')
  const [split, setSplit] = useState<PlayerSplitKey>('overall')
  const [pitchFilter, setPitchFilter] = useState<string | null>(null)

  const allHitters = useMemo(
    () => [...new Set(data.matchups.map((row) => row.hitter).filter(Boolean))].sort(),
    [data.matchups],
  )

  // Pre-select from /player?name=… (case-insensitive match against matchups)
  useEffect(() => {
    const nameParam = searchParams.get('name')?.trim()
    if (!nameParam || !allHitters.length) return
    const exact = allHitters.find((n) => n.toLowerCase() === nameParam.toLowerCase())
    if (exact) {
      setHitter(exact)
      return
    }
    const partial = allHitters.find((n) => n.toLowerCase().includes(nameParam.toLowerCase()))
    if (partial) setHitter(partial)
  }, [searchParams, allHitters])

  const filteredHitters = useMemo(() => {
    const q = query.trim().toLowerCase()
    const matches = q
      ? allHitters.filter((name) => name.toLowerCase().includes(q))
      : allHitters
    if (hitter && !matches.includes(hitter)) {
      return [hitter, ...matches]
    }
    return matches
  }, [allHitters, query, hitter])

  const rows = useMemo(() => {
    if (!hitter) return []
    return data.matchups
      .filter((row) => row.hitter === hitter)
      .slice()
      .sort((a, b) => (b.pa ?? 0) - (a.pa ?? 0))
  }, [data.matchups, hitter])

  const meta = rows[0]

  const gameLog = useMemo(() => {
    if (!hitter) return undefined
    const logs = data.player_logs ?? {}
    if (logs[hitter]) return logs[hitter]
    const key = Object.keys(logs).find((k) => k.toLowerCase() === hitter.toLowerCase())
    return key ? logs[key] : undefined
  }, [data.player_logs, hitter])

  const dayNightProfile = useMemo(() => {
    if (!hitter) return undefined
    const splits = data.player_day_night_splits ?? {}
    if (splits[hitter]) return splits[hitter]
    const key = Object.keys(splits).find((k) => k.toLowerCase() === hitter.toLowerCase())
    return key ? splits[key] : undefined
  }, [data.player_day_night_splits, hitter])

  const zoneHeatmap = useMemo(() => {
    if (!hitter) return undefined
    const maps = data.player_zone_heatmaps ?? {}
    if (maps[hitter]) return maps[hitter]
    const key = Object.keys(maps).find((k) => k.toLowerCase() === hitter.toLowerCase())
    return key ? maps[key] : undefined
  }, [data.player_zone_heatmaps, hitter])

  const pitchChips = useMemo(() => {
    const codes = [...new Set(rows.map((r) => r.pitch).filter(Boolean))].sort()
    return codes.map((pitch) => ({ pitch }))
  }, [rows])

  const displayRows = useMemo(() => {
    if (!pitchFilter) return rows
    return rows.filter((r) => r.pitch === pitchFilter)
  }, [rows, pitchFilter])

  useEffect(() => {
    setPitchFilter(null)
  }, [hitter])

  return (
    <div className="space-y-5">
      <div className="flex flex-wrap items-end justify-between gap-4">
        <div>
          <p className="text-xs font-medium uppercase tracking-[0.12em] text-[#8B949E]">
            Player Matchup
          </p>
          <h2 className="text-2xl font-bold tracking-tight">{data.date}</h2>
          <p className="mt-1 text-sm text-[#8B949E]">
            Search a hitter · season splits · pitch mix vs opposing starter
          </p>
        </div>
        <div className="flex flex-wrap items-center gap-3">
          <label className="flex items-center gap-2 text-xs text-[#8B949E]">
            Search
            <input
              type="search"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Type a name…"
              className="w-44 rounded-md border border-[#30363D] bg-[#161B22] px-2 py-1.5 text-xs text-[#F0F6FC] placeholder:text-[#6E7681]"
            />
          </label>
          <label className="flex items-center gap-2 text-xs text-[#8B949E]">
            Hitter
            <select
              value={hitter}
              onChange={(e) => setHitter(e.target.value)}
              className="min-w-[12rem] rounded-md border border-[#30363D] bg-[#161B22] px-2 py-1.5 text-xs text-[#F0F6FC]"
            >
              <option value="">Select hitter…</option>
              {filteredHitters.map((name) => (
                <option key={name} value={name}>
                  {name}
                </option>
              ))}
            </select>
          </label>
        </div>
      </div>

      <SectionBanner label={hitter ? hitter : 'Select a hitter'} count={hitter ? rows.length : undefined} />

      {!hitter ? (
        <Card title="No hitter selected" subtitle={`${allHitters.length} hitters available in today's matchups`}>
          <p className="text-sm text-[#8B949E]">
            Use search and the hitter dropdown to load pitch-mix rows and the full stat line.
          </p>
        </Card>
      ) : (
        <>
          <Card
            title="Recent game log"
            subtitle="Statcast game log · L5 / L10 / L20 · Hits / TB / HR"
          >
            <GameLogChart hitter={hitter} log={gameLog} />
          </Card>

          <Card title="Season splits" subtitle="120-day Statcast · day/night from MLB schedule">
            <div className="mb-3 flex flex-wrap gap-1">
              {PLAYER_SPLITS.map(({ key, label }) => (
                <button
                  key={key}
                  type="button"
                  onClick={() => setSplit(key)}
                  className={`rounded-md border px-3 py-1.5 text-[11px] font-medium transition-colors ${
                    split === key
                      ? 'border-[#58A6FF] bg-[#1F6FEB33] text-[#58A6FF]'
                      : 'border-[#30363D] text-[#8B949E] hover:bg-[#21262D] hover:text-[#F0F6FC]'
                  }`}
                >
                  {label}
                </button>
              ))}
            </div>
            <PlayerDayNightTable profile={dayNightProfile} activeSplit={split} />
          </Card>

          <Card
            title={hitter}
            subtitle={
              meta
                ? `${meta.team} · ${meta.game} · vs ${meta.opp_sp} · by pitch type`
                : 'No matchup rows for this hitter'
            }
          >
            {pitchChips.length > 0 && (
              <PitchMixFilterChips
                pitches={pitchChips}
                selected={pitchFilter}
                onSelect={setPitchFilter}
              />
            )}
            {pitchFilter && (
              <p className="mb-2 text-[10px] text-[#58A6FF]">
                Showing {pitchFilter} only · {displayRows.length} row
                {displayRows.length === 1 ? '' : 's'}
              </p>
            )}
            <CategoryBoardTable rows={displayRows} hideIdentity />
          </Card>

          <Card title="Zone heatmap" subtitle={`${hitter} · contact rate by pitch location`}>
            <ZoneHeatmap profile={zoneHeatmap} />
          </Card>
        </>
      )}
    </div>
  )
}
