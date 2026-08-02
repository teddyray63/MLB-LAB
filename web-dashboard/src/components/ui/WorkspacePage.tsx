import type { ReactNode } from 'react'

interface WorkspacePageProps {
  children: ReactNode
}

/** Standard vertical rhythm wrapper for new-IA workspace pages (Phase F3). */
export function WorkspacePage({ children }: WorkspacePageProps) {
  return <div className="space-y-6">{children}</div>
}
