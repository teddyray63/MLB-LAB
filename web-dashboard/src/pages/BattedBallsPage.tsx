import { useEffect, useMemo, useState } from 'react'
import { useSearchParams } from 'react-router-dom'
import { ExitVeloScatter } from '../components/ExitVeloScatter'
import { BattedBallProfileCard } from '../components/BattedBallProfileCard'
import { Card } from '../components/ui/Card'
import { SectionBanner } from '../components/ui/SectionBanner'
import { useExport } from '../context/ExportContext'

export function BattedBallsPage() {
  const data = useExport()
  const [searchParams] = useSearchParams()
  const [query, setQuery] = useState('')
  const [hitter, setHitter] = useState('')

  const battedBalls = data.batted_balls ?? {}

  const allHitters = useMemo(
    () => Object.keys(battedBalls).filter(Boolean).sort(),
    [battedBalls],
  )

  // Deep-link support: /batted-balls?name=…
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
    const matches = q ? allHitters.filter((name) => name.toLowerCase().includes(q)) : allHitters
    if (hitter && !matches.includes(hitter)) return [hitter, ...matches]
    return matches
  }, [allHitters, query, hitter])

  const balls = hitter ? battedBalls[hitter] : undefined
  const profile = hitter ? data.batted_ball_profiles?.[hitter] : undefined

  return (
    <div className="space-y-5">
      <div className="flex flex-wrap items-end justify-between gap-4">
        <div>
          <p className="text-xs font-medium uppercase tracking-[0.12em] text-[#8B949E]">
            Batted Balls
          </p>
          <h2 className="text-2xl font-bold tracking-tight">{data.date}</h2>
          <p className="mt-1 text-sm text-[#8B949E]">
            Per-batted-ball exit velocity &amp; launch angle · last {balls?.length ?? '150'} BBE
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

      <SectionBanner
        label={hitter ? hitter : 'Select a hitter'}
        count={hitter ? balls?.length : undefined}
      />

      {!allHitters.length ? (
        <Card title="No batted-ball data" subtitle="batted_balls is empty in today's export">
          <p className="text-sm text-[#8B949E]">
            Re-run the Python export to populate per-batted-ball exit velocity data.
          </p>
        </Card>
      ) : !hitter ? (
        <Card
          title="No hitter selected"
          subtitle={`${allHitters.length} hitters with batted-ball data`}
        >
          <p className="text-sm text-[#8B949E]">
            Pick a hitter to plot exit velocity vs launch angle for their recent batted balls.
          </p>
        </Card>
      ) : (
        <div className="grid gap-5 lg:grid-cols-2">
          <Card
            title="Exit velocity scatter"
            subtitle="Color by result, exit velo, or barrels · hover a point for details"
          >
            <ExitVeloScatter hitter={hitter} battedBalls={balls} />
          </Card>
          <Card title="Batted ball profile" subtitle={`${hitter} · spray, trajectory, distance`}>
            <BattedBallProfileCard profile={profile} />
          </Card>
        </div>
      )}
    </div>
  )
}
