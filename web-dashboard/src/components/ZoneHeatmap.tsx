import type { ZoneHeatmapProfile } from '../types/slate'

const MIN_SWINGS = 5

/** Statcast 13-zone layout (catcher's view): 1–9 strike zone + 11–14 chase. */
const GRID_ZONES: number[][] = [
  [7, 8, 9],
  [4, 5, 6],
  [1, 2, 3],
]

function zoneMap(profile: ZoneHeatmapProfile): Map<number, ZoneHeatmapProfile['zones'][number]> {
  return new Map(profile.zones.map((z) => [z.zone, z]))
}

function cellColor(rate: number | null | undefined, lowSample: boolean): string {
  if (lowSample || rate == null) return '#21262D'
  const t = Math.max(0, Math.min(1, (rate - 0.05) / 0.45))
  const r = Math.round(31 + t * (63 - 31))
  const g = Math.round(111 + t * (185 - 111))
  const b = Math.round(235 + t * (80 - 235))
  return `rgb(${r},${g},${b})`
}

function ZoneCell({
  zone,
  data,
  x,
  y,
  size,
}: {
  zone: number
  data: ZoneHeatmapProfile['zones'][number] | undefined
  x: number
  y: number
  size: number
}) {
  const lowSample = !data || data.swings < MIN_SWINGS
  const rate = data?.contact_rate
  const fill = cellColor(rate, lowSample)
  const label = lowSample ? '—' : rate != null ? `${Math.round(rate * 100)}%` : '—'

  return (
    <g>
      <rect
        x={x}
        y={y}
        width={size}
        height={size}
        rx={4}
        fill={fill}
        stroke="#30363D"
        strokeWidth={1}
      />
      <text
        x={x + size / 2}
        y={y + size / 2 - 4}
        textAnchor="middle"
        fill={lowSample ? '#6E7681' : '#F0F6FC'}
        fontSize={11}
        fontWeight={600}
      >
        {label}
      </text>
      <text
        x={x + size / 2}
        y={y + size / 2 + 10}
        textAnchor="middle"
        fill="#8B949E"
        fontSize={8}
      >
        z{zone}
        {data ? ` · ${data.swings}s` : ''}
      </text>
    </g>
  )
}

export function ZoneHeatmap({ profile }: { profile: ZoneHeatmapProfile | undefined }) {
  if (!profile?.zones?.length) {
    return (
      <p className="text-sm text-[#8B949E]">
        No zone-level pitch data for this hitter in the current Statcast window.
      </p>
    )
  }

  const byZone = zoneMap(profile)
  const cell = 56
  const gap = 4
  const gridW = cell * 3 + gap * 2
  const gridH = cell * 3 + gap * 2
  const pad = 8
  const svgW = gridW + pad * 2 + cell + gap
  const svgH = gridH + pad * 2 + cell + gap

  const gridX = pad + cell + gap
  const gridY = pad + cell + gap

  const chasePositions: Record<number, { x: number; y: number }> = {
    11: { x: gridX + cell + gap, y: pad },
    12: { x: gridX + cell + gap, y: gridY + gridH + gap },
    13: { x: pad, y: gridY + cell + gap },
    14: { x: gridX + gridW + gap, y: gridY + cell + gap },
  }

  return (
    <div>
      <p className="mb-3 text-[10px] text-[#8B949E]">
        Contact rate by Statcast zone (ball in play ÷ swings) · cells with &lt;{MIN_SWINGS} swings
        shown as low-confidence · 120-day window
      </p>
      <svg
        viewBox={`0 0 ${svgW} ${svgH}`}
        className="mx-auto block max-w-full"
        role="img"
        aria-label="Strike zone contact rate heatmap"
      >
        {/* Strike zone outline */}
        <rect
          x={gridX - 2}
          y={gridY - 2}
          width={gridW + 4}
          height={gridH + 4}
          fill="none"
          stroke="#484F58"
          strokeWidth={2}
          rx={6}
        />
        {GRID_ZONES.map((row, ri) =>
          row.map((zone, ci) => (
            <ZoneCell
              key={zone}
              zone={zone}
              data={byZone.get(zone)}
              x={gridX + ci * (cell + gap)}
              y={gridY + ri * (cell + gap)}
              size={cell}
            />
          )),
        )}
        {[11, 12, 13, 14].map((zone) => {
          const pos = chasePositions[zone]
          return (
            <ZoneCell
              key={zone}
              zone={zone}
              data={byZone.get(zone)}
              x={pos.x}
              y={pos.y}
              size={cell}
            />
          )
        })}
      </svg>
      <div className="mt-2 flex items-center justify-center gap-2 text-[9px] text-[#8B949E]">
        <span>Low contact</span>
        <div
          className="h-2 w-24 rounded"
          style={{
            background: 'linear-gradient(to right, rgb(31,111,235), rgb(63,185,80))',
          }}
        />
        <span>High contact</span>
      </div>
    </div>
  )
}
