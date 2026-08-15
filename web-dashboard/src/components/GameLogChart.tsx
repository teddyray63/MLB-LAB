import { useEffect, useMemo, useState } from 'react'
import type { GameLogEntry } from '../types/slate'

export type GameLogMetric = 'hits' | 'tb' | 'hr'
export type GameLogWindow = 5 | 10 | 20

const METRICS: { key: GameLogMetric; label: string }[] = [
  { key: 'hits', label: 'Hits' },
  { key: 'tb', label: 'TB' },
  { key: 'hr', label: 'HR' },
]

const WINDOWS: GameLogWindow[] = [5, 10, 20]

function summarizeWindow(games: GameLogEntry[], window: number): string {
  const slice = games.slice(0, window)
  if (!slice.length) return `L${window}: no games`
  const pa = slice.reduce((n, g) => n + (g.pa ?? 0), 0)
  const hits = slice.reduce((n, g) => n + (g.hits ?? 0), 0)
  const hr = slice.reduce((n, g) => n + (g.hr ?? 0), 0)
  const tb = slice.reduce((n, g) => n + (g.tb ?? 0), 0)
  // H/PA proxy — game_log has PA not AB
  const avg = pa > 0 ? hits / pa : 0
  return `L${slice.length}: ${avg.toFixed(3)} AVG · ${hr} HR · ${tb} TB · ${hits} H`
}

interface GameLogChartProps {
  hitter: string
  log: GameLogEntry[] | undefined
  /** When set, window is controlled externally (e.g. shared FilterBar). Hides local window toggles. */
  window?: number
}

export function GameLogChart({ hitter, log, window: controlledWindow }: GameLogChartProps) {
  const isControlled = controlledWindow !== undefined
  const [metric, setMetric] = useState<GameLogMetric>('hits')
  const [localWindow, setLocalWindow] = useState<GameLogWindow>(10)

  const available = log?.length ?? 0
  const window = isControlled ? controlledWindow : localWindow

  // If current window is larger than available games, fall back (uncontrolled only)
  useEffect(() => {
    if (isControlled || available <= 0 || window <= available) return
    if (available >= 10) setLocalWindow(10)
    else if (available >= 5) setLocalWindow(5)
  }, [available, isControlled, window])

  const games = useMemo(() => {
    if (!log?.length) return []
    // log is most-recent first; chart left→right chronological
    return [...log].slice(0, window).reverse()
  }, [log, window])

  const summary = useMemo(() => {
    if (!log?.length) return ''
    return summarizeWindow(log, window)
  }, [log, window])

  if (!log || log.length === 0) {
    return (
      <p className="text-sm text-[#8B949E]">No recent game log available</p>
    )
  }

  const values = games.map((g) => Number(g[metric] ?? 0))
  const maxVal = Math.max(1, ...values)

  const width = 560
  const height = 160
  const padL = 28
  const padR = 8
  const padT = 16
  const padB = 36
  const innerW = width - padL - padR
  const innerH = height - padT - padB
  const gap = 6
  const barW = Math.max(8, (innerW - gap * Math.max(games.length - 1, 0)) / Math.max(games.length, 1))

  return (
    <div className="space-y-3">
      <div className="flex flex-wrap items-center justify-between gap-2">
        {!isControlled && (
          <div className="flex gap-1">
            {WINDOWS.map((n) => {
              const disabled = available < n
              return (
                <button
                  key={n}
                  type="button"
                  disabled={disabled}
                  title={disabled ? `Only ${available} games in log` : `Last ${n} games`}
                  onClick={() => setLocalWindow(n)}
                  className={`rounded-md border px-2.5 py-1 text-[11px] font-medium transition-colors ${
                    disabled
                      ? 'cursor-not-allowed border-[#21262D] text-[#484F58]'
                      : localWindow === n
                        ? 'border-[#58A6FF] bg-[#1F6FEB33] text-[#58A6FF]'
                        : 'border-[#30363D] text-[#8B949E] hover:bg-[#21262D] hover:text-[#F0F6FC]'
                  }`}
                >
                  L{n}
                </button>
              )
            })}
          </div>
        )}
        <div className={`flex gap-1${isControlled ? ' ml-auto' : ''}`}>
          {METRICS.map(({ key, label }) => (
            <button
              key={key}
              type="button"
              onClick={() => setMetric(key)}
              className={`rounded-md border px-2.5 py-1 text-[11px] font-medium transition-colors ${
                metric === key
                  ? 'border-[#58A6FF] bg-[#1F6FEB33] text-[#58A6FF]'
                  : 'border-[#30363D] text-[#8B949E] hover:bg-[#21262D] hover:text-[#F0F6FC]'
              }`}
            >
              {label}
            </button>
          ))}
        </div>
      </div>

      <p className="text-sm font-medium text-[#F0F6FC]">{summary}</p>
      <p className="text-xs text-[#8B949E]">
        {hitter} · showing {games.length} of {available} logged games · AVG is H/PA
      </p>

      <svg
        viewBox={`0 0 ${width} ${height}`}
        className="h-auto w-full max-w-full"
        role="img"
        aria-label={`${hitter} L${window} ${metric}`}
      >
        <line
          x1={padL}
          y1={padT + innerH}
          x2={padL + innerW}
          y2={padT + innerH}
          stroke="#30363D"
          strokeWidth={1}
        />
        {games.map((g, i) => {
          const v = values[i]
          const h = (v / maxVal) * innerH
          const x = padL + i * (barW + gap)
          const y = padT + innerH - h
          const dateLabel = g.date.slice(5)
          return (
            <g key={`${g.date}-${i}`}>
              <rect
                x={x}
                y={y}
                width={barW}
                height={Math.max(h, v > 0 ? 2 : 0)}
                rx={2}
                fill={v > 0 ? '#58A6FF' : '#21262D'}
              >
                <title>
                  {g.date}: {v} {metric}
                </title>
              </rect>
              {v > 0 && (
                <text
                  x={x + barW / 2}
                  y={y - 4}
                  textAnchor="middle"
                  fill="#8B949E"
                  fontSize={10}
                  fontFamily="ui-monospace, SFMono-Regular, Menlo, monospace"
                >
                  {v}
                </text>
              )}
              <text
                x={x + barW / 2}
                y={padT + innerH + 14}
                textAnchor="middle"
                fill="#6E7681"
                fontSize={9}
                fontFamily="ui-monospace, SFMono-Regular, Menlo, monospace"
              >
                {dateLabel}
              </text>
            </g>
          )
        })}
      </svg>
    </div>
  )
}
