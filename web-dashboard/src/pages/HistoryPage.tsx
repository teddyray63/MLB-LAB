import { CoveragePanel } from '../components/data-status/CoveragePanel'
import { ExportInfoPanel } from '../components/data-status/ExportInfoPanel'
import { FilterSupportPanel } from '../components/data-status/FilterSupportPanel'
import { PipelineStatusPanel } from '../components/data-status/PipelineStatusPanel'
import { WarningsPanel } from '../components/data-status/WarningsPanel'
import { PageHeader } from '../components/ui/PageHeader'
import { WorkspacePage } from '../components/ui/WorkspacePage'
import { useDataStatus } from '../hooks/useDataStatus'

/** Phase E — operational health view of the current daily export. */
export function HistoryPage() {
  const { snapshot, filterSupport } = useDataStatus()

  return (
    <WorkspacePage>
      <PageHeader
        kicker="Data Status"
        title={snapshot.slateDate}
        description="Export health, coverage, and filter capability · read-only operational view"
      />

      <div className="grid gap-5 lg:grid-cols-2">
        <ExportInfoPanel snapshot={snapshot} />
        <PipelineStatusPanel items={snapshot.pipeline} />
      </div>

      <CoveragePanel metrics={snapshot.coverage} />

      <WarningsPanel snapshot={snapshot} />

      <FilterSupportPanel
        support={filterSupport}
        contextNote={snapshot.filterContextNote}
      />
    </WorkspacePage>
  )
}
