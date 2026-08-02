import { fmtInt, fmtPct } from '../design/format'
import type { BattedBallProfile } from '../types/slate'

function pctCell(value: number | null | undefined) {
  if (value == null || Number.isNaN(value)) return '—'
  return fmtPct(value)
}

export function BattedBallProfileCard({ profile }: { profile: BattedBallProfile | undefined }) {
  if (!profile) {
    return (
      <p className="text-sm text-[#8B949E]">No batted-ball profile for this hitter in the export window.</p>
    )
  }

  const directionSum =
    (profile.pull_pct ?? 0) + (profile.straight_pct ?? 0) + (profile.oppo_pct ?? 0)
  const trajSum = (profile.gb_pct ?? 0) + (profile.ld_pct ?? 0) + (profile.fb_pct ?? 0)

  return (
    <div className="space-y-4">
      <p className="text-[10px] text-[#8B949E]">
        {profile.bbe} batted balls · spray from Statcast hc_x/hc_y · trajectory: GB &lt;10°, LD 10–25°, FB
        &gt;25°
      </p>
      <div className="grid gap-4 sm:grid-cols-2">
        <div className="rounded-md border border-[#30363D] bg-[#0D1117] p-3">
          <p className="mb-2 text-[11px] font-medium uppercase tracking-wide text-[#8B949E]">
            Direction
          </p>
          <dl className="grid grid-cols-3 gap-2 text-center text-xs">
            <div>
              <dt className="text-[#6E7681]">Pull</dt>
              <dd className="mt-1 font-mono text-lg text-[#F0F6FC]">{pctCell(profile.pull_pct)}</dd>
            </div>
            <div>
              <dt className="text-[#6E7681]">Straight</dt>
              <dd className="mt-1 font-mono text-lg text-[#F0F6FC]">{pctCell(profile.straight_pct)}</dd>
            </div>
            <div>
              <dt className="text-[#6E7681]">Oppo</dt>
              <dd className="mt-1 font-mono text-lg text-[#F0F6FC]">{pctCell(profile.oppo_pct)}</dd>
            </div>
          </dl>
          <p className="mt-2 text-center text-[9px] text-[#6E7681]">
            sum {Math.round(directionSum * 100)}%
          </p>
        </div>
        <div className="rounded-md border border-[#30363D] bg-[#0D1117] p-3">
          <p className="mb-2 text-[11px] font-medium uppercase tracking-wide text-[#8B949E]">
            Trajectory
          </p>
          <dl className="grid grid-cols-3 gap-2 text-center text-xs">
            <div>
              <dt className="text-[#6E7681]">GB</dt>
              <dd className="mt-1 font-mono text-lg text-[#F0F6FC]">{pctCell(profile.gb_pct)}</dd>
            </div>
            <div>
              <dt className="text-[#6E7681]">LD</dt>
              <dd className="mt-1 font-mono text-lg text-[#F0F6FC]">{pctCell(profile.ld_pct)}</dd>
            </div>
            <div>
              <dt className="text-[#6E7681]">FB</dt>
              <dd className="mt-1 font-mono text-lg text-[#F0F6FC]">{pctCell(profile.fb_pct)}</dd>
            </div>
          </dl>
          <p className="mt-2 text-center text-[9px] text-[#6E7681]">sum {Math.round(trajSum * 100)}%</p>
        </div>
      </div>
      <dl className="grid grid-cols-3 gap-3 text-xs">
        <div className="rounded border border-[#30363D] px-3 py-2">
          <dt className="text-[#6E7681]">Avg distance</dt>
          <dd className="mt-1 font-mono text-[#F0F6FC]">
            {profile.avg_dist != null ? `${profile.avg_dist.toFixed(0)} ft` : '—'}
          </dd>
        </div>
        <div className="rounded border border-[#30363D] px-3 py-2">
          <dt className="text-[#6E7681]">300 ft+</dt>
          <dd className="mt-1 font-mono text-[#F0F6FC]">{fmtInt(profile.dist_300_plus)}</dd>
        </div>
        <div className="rounded border border-[#30363D] px-3 py-2">
          <dt className="text-[#6E7681]">350 ft+</dt>
          <dd className="mt-1 font-mono text-[#F0F6FC]">{fmtInt(profile.dist_350_plus)}</dd>
        </div>
      </dl>
    </div>
  )
}
