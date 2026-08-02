import { PitcherPlatoonTable } from '../PitcherPlatoonTable'
import { PitcherSituationTable } from '../PitcherSituationTable'
import { SpInningSplitsTable } from '../SpInningSplitsTable'
import type { GameDetail } from '../../types/slate'

interface PitcherSplitsBlockProps {
  name: string
  situation: GameDetail['away_sp_situation']
  platoon: GameDetail['away_sp_platoon']
  inningSplits: GameDetail['away_sp_inning_splits']
}

export function PitcherSplitsBlock({
  name,
  situation,
  platoon,
  inningSplits,
}: PitcherSplitsBlockProps) {
  return (
    <div className="space-y-4">
      <h4 className="text-sm font-semibold text-[#F0F6FC]">{name || 'TBD'}</h4>
      <div>
        <p className="mb-2 text-[10px] font-semibold uppercase tracking-[0.12em] text-[#8B949E]">
          By situation
        </p>
        <PitcherSituationTable rows={situation ?? []} pitcherName={name} />
      </div>
      <div>
        <p className="mb-2 text-[10px] font-semibold uppercase tracking-[0.12em] text-[#8B949E]">
          vs RHB / vs LHB
        </p>
        <PitcherPlatoonTable rows={platoon ?? []} pitcherName={name} />
      </div>
      <div>
        <p className="mb-2 text-[10px] font-semibold uppercase tracking-[0.12em] text-[#8B949E]">
          Runs allowed through inning
        </p>
        <SpInningSplitsTable pitcher={name} rows={inningSplits} />
      </div>
    </div>
  )
}
