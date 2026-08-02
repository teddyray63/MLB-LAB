import type { ReactNode } from 'react'

interface EmptyStateProps {
  children: ReactNode
}

/** Shared empty-state panel for new-IA workspaces (Phase F3). */
export function EmptyState({ children }: EmptyStateProps) {
  return (
    <div
      className="rounded-lg border border-[#30363D] bg-[#161B22] px-4 py-10 text-center"
      role="status"
    >
      <p className="text-sm text-[#8B949E]">{children}</p>
    </div>
  )
}
