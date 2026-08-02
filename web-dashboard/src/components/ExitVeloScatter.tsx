import { useMemo, useState } from 'react'
import type { BattedBall } from '../types/slate'

type ColorMode = 'result' | 'ev' | 'barrel'

const COLOR_MODES: { key: ColorMode; label: string }[] = [
  { key: 'result', label: 'Result' },
  { key: 'ev', label: 'Exit velo' },
  { key: 'barrel', label: 'Barrels' },
]

const HIT_EVENTS = new Set(['single', 'double', 'triple', 'home_run'])

// Plot bounds (deg / mph)
const LA_MIN = -40
const LA_MAX = 60
const EV_MIN = 40
const EV_MAX = 120

function isHit(result: string): boolean {
  return HIT_EVENTS.has(result)
}

function prettyResult(result: string): string {
  return result.replace(/_/g, ' ')
}

/** Blue (soft) → amber → red (scorched) for exit velo heat */
function evColor(ev: number | null): string {
  if (ev == null) return '#6E7681'
  const t = Math.max(0, Math.min(1, (ev - 70) / (110 - 70)))
  if (t < 0.5) {
    // blue → amber
    const k = t / 0.5
    const r = Math.round(56 + k * (210 - 56))
    const g = Math.round(139 + k * (153 - 139))
    const b = Math.round(253 + k * (34 - 253))
    return `rgb(${r},${g},${b})`
  }
  // amber → red
  const k = (t - 0.5) / 0.5
  const r = Math.round(210 + k * (248 - 210))
  const g = Math.round(153 + k * (81 - 153))
  const b = Math.round(34 + k * (73 - 34))
  return `rgb(${r},${g},${b})`
}

function resultColor(bb: BattedBall): string {
  if (bb.result === 'home_run') return '#F0B429'
  if (isHit(bb.result)) return '#3FB950'
  return '#6E7681'
}

function pointColor(bb: BattedBall, mode: ColorMode): string {
  if (mode === 'ev') return evColor(bb.ev)
  if (mode === 'barrel') return bb.barrel ? '#F85149' : '#3A4149'
  return resultColor(bb)
}

interface ExitVeloScatterProps {
  hitter: string
  battedBalls: BattedBall[] | undefined
}

export function ExitVeloScatter({ hitter, battedBalls }: ExitVeloScatterProps) {
  const [mode, setMode] = useState<ColorMode>('result')
  const [hitsOnly, setHitsOnly] = useState(false)

  const balls = useMemo(
    () => (battedBalls ?? []).filter((b) => b.ev != null && b.la != null),
    [battedBalls],
  )

  const shown = useMemo(
    () => (hitsOnly ? balls.filter((b) => isHit(b.result)) : balls),
    [balls, hitsOnly],
  )

  const stats = useMemo(() => {
    if (!balls.length) return null
    const evs = balls.map((b) => b.ev as number)
    const avgEv = evs.reduce((a, b) => a + b, 0) / evs.length
    const maxEv = Math.max(...evs)
    const hardHit = balls.filter((b) => (b.ev ?? 0) >= 95).length / balls.length
    const barrels = balls.filter((b) => b.barrel).length
    const sweet = balls.filter((b) => (b.la ?? -999) >= 8 && (b.la ?? 999) <= 32).length / balls.length
    return { avgEv, maxEv, hardHit, barrels, count: balls.length, sweet }
  }, [balls])

  if (!battedBalls || battedBalls.length === 0) {
    return <p className="text-sm text-[#8B949E]">No batted-ball data available</p>
  }

  const width = 560
  const height = 360
  const padL = 40
  const padR = 12
  const padT = 14
  const padB = 34
  const innerW = width - padL - padR
  const innerH = height - padT - padB

  const xOf = (la: number) =>
    padL + ((Math.max(LA_MIN, Math.min(LA_MAX, la)) - LA_MIN) / (LA_MAX - LA_MIN)) * innerW
  const yOf = (ev: number) =>
    padT + innerH - ((Math.max(EV_MIN, Math.min(EV_MAX, ev)) - EV_MIN) / (EV_MAX - EV_MIN)) * innerH

  const evTicks = [50, 70, 90, 110]
  const laTicks = [-20, 0, 20, 40]
  const hardHitY = yOf(95)

  return (
    <div className="space-y-3">
      <div className="flex flex-wrap items-center justify-between gap-2">
        <label className="flex items-center gap-1.5 text-[11px] text-[#8B949E]">
          <input
            type="checkbox"
            checked={hitsOnly}
            onChange={(e) => setHitsOnly(e.target.checked)}
            className="accent-[#58A6FF]"
          />
          Hits only
        </label>
        <div className="flex gap-1">
          {COLOR_MODES.map(({ key, label }) => (
            <button
              key={key}
              type="button"
              onClick={() => setMode(key)}
              className={`rounded-md border px-2.5 py-1 text-[11px] font-medium transition-colors ${
                mode === key
                  ? 'border-[#58A6FF] bg-[#1F6FEB33] text-[#58A6FF]'
                  : 'border-[#30363D] text-[#8B949E] hover:bg-[#21262D] hover:text-[#F0F6FC]'
              }`}
            >
              {label}
            </button>
          ))}
        </div>
      </div>

      {stats && (
        <p className="text-sm font-medium text-[#F0F6FC]">
          {stats.count} BBE · {stats.avgEv.toFixed(1)} avg EV · {stats.maxEv.toFixed(1)} max ·{' '}
          {(stats.hardHit * 100).toFixed(0)}% hard-hit · {stats.barrels} barrels ·{' '}
          {(stats.sweet * 100).toFixed(0)}% sweet-spot
        </p>
      )}
      <p className="text-xs text-[#8B949E]">
        {hitter} · exit velo (y) vs launch angle (x) · dashed line = 95 mph hard-hit · shaded band = 8–32° sweet spot
      </p>

      <svg
        viewBox={`0 0 ${width} ${height}`}
        className="h-auto w-full max-w-full"
        role="img"
        aria-label={`${hitter} exit velocity scatter`}
      >
        {/* Sweet-spot launch-angle band (8–32°) */}
        <rect
          x={xOf(8)}
          y={padT}
          width={xOf(32) - xOf(8)}
          height={innerH}
          fill="#238636"
          opacity={0.08}
        />
        {/* Axes */}
        <line x1={padL} y1={padT} x2={padL} y2={padT + innerH} stroke="#30363D" strokeWidth={1} />
        <line
          x1={padL}
          y1={padT + innerH}
          x2={padL + innerW}
          y2={padT + innerH}
          stroke="#30363D"
          strokeWidth={1}
        />
        {/* Hard-hit reference (95 mph) */}
        <line
          x1={padL}
          y1={hardHitY}
          x2={padL + innerW}
          y2={hardHitY}
          stroke="#F85149"
          strokeWidth={1}
          strokeDasharray="4 3"
          opacity={0.55}
        />
        {/* Y ticks (EV) */}
        {evTicks.map((t) => (
          <g key={`y${t}`}>
            <text
              x={padL - 6}
              y={yOf(t) + 3}
              textAnchor="end"
              fill="#6E7681"
              fontSize={9}
              fontFamily="ui-monospace, SFMono-Regular, Menlo, monospace"
            >
              {t}
            </text>
          </g>
        ))}
        {/* X ticks (LA) */}
        {laTicks.map((t) => (
          <text
            key={`x${t}`}
            x={xOf(t)}
            y={padT + innerH + 14}
            textAnchor="middle"
            fill="#6E7681"
            fontSize={9}
            fontFamily="ui-monospace, SFMono-Regular, Menlo, monospace"
          >
            {t}°
          </text>
        ))}
        {/* Points */}
        {shown.map((b, i) => (
          <circle
            key={`${b.date}-${i}`}
            cx={xOf(b.la as number)}
            cy={yOf(b.ev as number)}
            r={b.result === 'home_run' ? 3.6 : 2.8}
            fill={pointColor(b, mode)}
            fillOpacity={0.82}
            stroke={b.barrel ? '#F0F6FC' : 'none'}
            strokeWidth={b.barrel ? 0.8 : 0}
          >
            <title>
              {b.date} · {b.ev} mph · {b.la}° · {b.dist ?? '—'} ft · {prettyResult(b.result)}
              {b.pitch ? ` · ${b.pitch}` : ''}
              {b.barrel ? ' · barrel' : ''}
            </title>
          </circle>
        ))}
      </svg>

      <Legend mode={mode} />
    </div>
  )
}

function Legend({ mode }: { mode: ColorMode }) {
  if (mode === 'ev') {
    return (
      <div className="flex items-center gap-2 text-[11px] text-[#8B949E]">
        <span>Soft</span>
        <span
          className="h-2 w-28 rounded"
          style={{
            background: `linear-gradient(to right, ${evColor(70)}, ${evColor(90)}, ${evColor(108)})`,
          }}
        />
        <span>Scorched</span>
      </div>
    )
  }
  if (mode === 'barrel') {
    return (
      <div className="flex flex-wrap items-center gap-3 text-[11px] text-[#8B949E]">
        <LegendDot color="#F85149" label="Barrel" />
        <LegendDot color="#3A4149" label="Non-barrel" />
      </div>
    )
  }
  return (
    <div className="flex flex-wrap items-center gap-3 text-[11px] text-[#8B949E]">
      <LegendDot color="#F0B429" label="Home run" />
      <LegendDot color="#3FB950" label="Hit" />
      <LegendDot color="#6E7681" label="Out / other" />
      <span className="text-[#6E7681]">· white ring = barrel</span>
    </div>
  )
}

function LegendDot({ color, label }: { color: string; label: string }) {
  return (
    <span className="flex items-center gap-1.5">
      <span className="inline-block h-2.5 w-2.5 rounded-full" style={{ background: color }} />
      {label}
    </span>
  )
}
