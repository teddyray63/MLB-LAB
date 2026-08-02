import { Card } from '../components/ui/Card'
import { PageHeader } from '../components/ui/PageHeader'
import { WorkspacePage } from '../components/ui/WorkspacePage'

export function SettingsPage() {
  return (
    <WorkspacePage>
      <PageHeader
        kicker="Settings"
        title="Settings"
        description="Display preferences, default filters, and column customization."
        action={
          <span className="shrink-0 rounded-full border border-[#30363D] bg-[#161B22] px-3 py-1 text-[10px] font-semibold uppercase tracking-[0.14em] text-[#8B949E]">
            Phase 1
          </span>
        }
      />

      <Card
        title="Placeholder — Phase 1 scaffold"
        subtitle="Navigation and routing only. The full experience arrives in a later phase."
      >
        <p className="text-sm text-[#8B949E]">
          This route is wired into the new information architecture. Its detailed layout,
          filters, and tables have not been built yet.
        </p>
      </Card>
    </WorkspacePage>
  )
}
