import type { ReactNode } from 'react'
import { Link } from 'react-router-dom'
import { Card } from './Card'

export interface LegacyLink {
  to: string
  label: string
  note?: string
}

interface PlaceholderPageProps {
  kicker: string
  title: string
  description?: string
  /** Phase in which this page's real UI lands (shown as a small badge) */
  phase?: string
  /** Operational legacy pages this view will eventually absorb */
  legacyLinks?: LegacyLink[]
  children?: ReactNode
}

/**
 * Phase 1 shell for a new information-architecture route. Renders the new
 * page header/layout and links out to the still-operational legacy pages.
 * No page internals are implemented here yet.
 */
export function PlaceholderPage({
  kicker,
  title,
  description,
  phase,
  legacyLinks,
  children,
}: PlaceholderPageProps) {
  return (
    <div className="space-y-5">
      <div className="flex flex-wrap items-end justify-between gap-4">
        <div>
          <p className="text-xs font-medium uppercase tracking-[0.12em] text-[#8B949E]">
            {kicker}
          </p>
          <h2 className="text-2xl font-bold tracking-tight">{title}</h2>
          {description && <p className="mt-1 text-sm text-[#8B949E]">{description}</p>}
        </div>
        {phase && (
          <span className="rounded-full border border-[#30363D] bg-[#161B22] px-3 py-1 text-[10px] font-semibold uppercase tracking-[0.14em] text-[#8B949E]">
            {phase}
          </span>
        )}
      </div>

      <Card
        title="Placeholder — Phase 1 scaffold"
        subtitle="Navigation and routing only. The full experience arrives in a later phase."
      >
        <p className="text-sm text-[#8B949E]">
          This route is wired into the new information architecture. Its detailed layout,
          filters, and tables have not been built yet.
        </p>

        {legacyLinks && legacyLinks.length > 0 && (
          <div className="mt-4">
            <p className="mb-2 text-[10px] font-semibold uppercase tracking-[0.12em] text-[#8B949E]">
              Existing tools (still fully operational)
            </p>
            <div className="flex flex-wrap gap-2">
              {legacyLinks.map((link) => (
                <Link
                  key={link.to}
                  to={link.to}
                  className="rounded-md border border-[#30363D] bg-[#0D1117] px-3 py-1.5 text-xs font-medium text-[#58A6FF] transition-colors hover:bg-[#161B22]"
                  title={link.note}
                >
                  {link.label} →
                </Link>
              ))}
            </div>
          </div>
        )}
      </Card>

      {children}
    </div>
  )
}
