import type { ReactNode } from 'react'

interface PageHeaderProps {
  kicker: string
  title: string
  accent?: string
  description?: string
  warning?: string
  action?: ReactNode
}

/** Shared page title block for new-IA workspaces (Phase F3). */
export function PageHeader({
  kicker,
  title,
  accent,
  description,
  warning,
  action,
}: PageHeaderProps) {
  return (
    <header className="flex flex-wrap items-start justify-between gap-4">
      <div className="min-w-0 flex-1">
        <p className="text-xs font-medium uppercase tracking-[0.12em] text-[#8B949E]">
          {kicker}
        </p>
        <h2 className="mt-0.5 text-2xl font-bold tracking-tight text-[#F0F6FC]">{title}</h2>
        {accent && <p className="mt-1 text-sm text-[#58A6FF]">{accent}</p>}
        {description && <p className="mt-1 text-sm text-[#8B949E]">{description}</p>}
        {warning && (
          <p className="mt-2 text-[10px] text-[#D29922]" role="status">
            {warning}
          </p>
        )}
      </div>
      {action}
    </header>
  )
}
