import { PitcherSplitsBlock } from './PitcherSplitsBlock'
import { Card } from '../ui/Card'
import { useExport } from '../../context/ExportContext'
import { useGameContext } from '../../context/ResearchContext'
import type { GameDetail } from '../../types/slate'

function useSelectedGameDetail(): GameDetail | null {
  const data = useExport()
  const { selection } = useGameContext()
  if (selection.gamePk == null) return null
  return data.game_details?.find((g) => g.game_pk === selection.gamePk) ?? null
}

export function TodayPitchersTab() {
  const detail = useSelectedGameDetail()

  if (!detail) {
    return (
      <Card title="Pitchers" subtitle="Select a game">
        <p className="text-sm text-[#8B949E]">No pitcher splits until a game is selected.</p>
      </Card>
    )
  }

  return (
    <Card
      title="Pitcher splits by situation"
      subtitle={`${detail.away_sp} vs ${detail.home_sp} · 120-day Statcast`}
    >
      <div className="grid gap-6 lg:grid-cols-2">
        <PitcherSplitsBlock
          name={detail.away_sp}
          situation={detail.away_sp_situation}
          platoon={detail.away_sp_platoon}
          inningSplits={detail.away_sp_inning_splits}
        />
        <PitcherSplitsBlock
          name={detail.home_sp}
          situation={detail.home_sp_situation}
          platoon={detail.home_sp_platoon}
          inningSplits={detail.home_sp_inning_splits}
        />
      </div>
    </Card>
  )
}
