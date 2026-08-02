import { CoveragePanel } from '../components/data-status/CoveragePanel'
import { ExportInfoPanel } from '../components/data-status/ExportInfoPanel'
import { FilterSupportPanel } from '../components/data-status/FilterSupportPanel'
import { PipelineStatusPanel } from '../components/data-status/PipelineStatusPanel'
import { WarningsPanel } from '../components/data-status/WarningsPanel'
import { useDataStatus } from '../hooks/useDataStatus'

/** Phase E — operational health view of the current daily export. */
export function HistoryPage() {
  const { snapshot, filterSupport } = useDataStatus()

  return (
    <div className="space-y-5">
      <div>
        <p className="text-xs font-medium uppercase tracking-[0.12em] text-[#8B949E]">
          Data Status
        </p>
        <h2 className="text-2xl font-bold tracking-tight">{snapshot.slateDate}</h2>
        <p className="mt-1 text-sm text-[#8B949E]">
          Export health, coverage, and filter capability · read-only operational view
        </p>
      </div>

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
    </div>
  )
}
