import { describe, expect, it } from 'vitest'
import { buildFilterSupportMatrix, parseSituation, resolveFilters } from './filterSupport'
import {
  SITUATION_OPTIONS,
  situationToSplitKey,
  type SituationKey,
} from '../types/research'
import type { DailyExport, SplitHitter, SplitLine } from '../types/slate'

const seasonLine: SplitLine = {
  pa: 40,
  ab: 36,
  hits: 10,
  hr: 2,
  avg: 0.278,
  slg: 0.5,
}

const bvpLine: SplitLine = {
  pa: 10,
  ab: 9,
  hits: 3,
  hr: 1,
  avg: 0.333,
  slg: 0.667,
}

const lhpLine: SplitLine = {
  pa: 8,
  ab: 7,
  hits: 1,
  hr: 0,
  avg: 0.143,
  slg: 0.143,
}

function splitHitter(name: string, bvp: SplitLine | null): SplitHitter {
  return {
    hitter: name,
    bvp_pitcher: 'Home Pitcher',
    overall: seasonLine,
    vs_lhp: lhpLine,
    vs_rhp: seasonLine,
    bvp,
  }
}

function exportWithSplits(rows: SplitHitter[]): DailyExport {
  return {
    date: '2026-08-01',
    games: [
      {
        game_pk: 100001,
        game_id: 'Away Team @ Home Team',
        away_team: 'Away Team',
        home_team: 'Home Team',
        away_sp: 'Away Pitcher',
        home_sp: 'Home Pitcher',
      },
    ],
    matchups: [],
    game_details: [
      {
        game_pk: 100001,
        game_id: 'Away Team @ Home Team',
        away_team: 'Away Team',
        home_team: 'Home Team',
        away_sp: 'Away Pitcher',
        home_sp: 'Home Pitcher',
        away_splits: rows,
        home_splits: [],
      },
    ],
  } as DailyExport
}

describe('shared BVP situation contract', () => {
  it('includes vs Today’s SP with shared key bvp', () => {
    const option = SITUATION_OPTIONS.find((item) => item.key === 'bvp')
    expect(option).toBeDefined()
    expect(option?.label).toBe('vs Today’s SP')
    expect(parseSituation('bvp')).toBe('bvp')
  })

  it('maps the shared situation key only to bvp', () => {
    expect(situationToSplitKey('bvp')).toBe('bvp')
    expect(situationToSplitKey('vlhp')).toBe('vs_lhp')
    expect(situationToSplitKey('vrhp')).toBe('vs_rhp')
    expect(situationToSplitKey('overall')).toBe('overall')
    expect(situationToSplitKey('bvp')).not.toBe('overall')
    expect(situationToSplitKey('bvp')).not.toBe('vs_lhp')
    expect(situationToSplitKey('bvp')).not.toBe('vs_rhp')
  })

  it('marks BVP supported when the selected player has a sample', () => {
    const exportData = exportWithSplits([splitHitter('Test Hitter', bvpLine)])
    const support = buildFilterSupportMatrix(exportData, {
      gamePk: 100001,
      player: { name: 'Test Hitter', team: 'Away Team', side: 'away' },
    })
    expect(support.situation.bvp.supported).toBe(true)
    expect(support.situation.bvp.source).toBe('export')
    const resolved = resolveFilters(exportData, {
      gamePk: 100001,
      player: { name: 'Test Hitter', team: 'Away Team', side: 'away' },
    }, { situation: 'bvp' })
    expect(resolved.situation).toBe('bvp')
  })

  it('marks BVP unsupported when the sample is missing', () => {
    const exportData = exportWithSplits([splitHitter('Test Hitter', null)])
    const support = buildFilterSupportMatrix(exportData, {
      gamePk: 100001,
      player: { name: 'Test Hitter', team: 'Away Team', side: 'away' },
    })
    expect(support.situation.bvp.supported).toBe(false)
    expect(support.situation.bvp.source).toBe('unsupported')
    expect(support.situation.bvp.reason).toMatch(/starting pitcher/i)
  })

  it('does not treat handedness or season lines as BVP support', () => {
    const exportData = exportWithSplits([splitHitter('Test Hitter', null)])
    const support = buildFilterSupportMatrix(exportData, {
      gamePk: 100001,
      player: { name: 'Test Hitter', team: 'Away Team', side: 'away' },
    })
    expect(support.situation.vlhp.supported).toBe(true)
    expect(support.situation.overall.supported).toBe(true)
    expect(support.situation.bvp.supported).toBe(false)
    expect(situationToSplitKey('bvp')).toBe('bvp')
  })

  it('uses the same mapping for Today and Research situation keys', () => {
    const keys: SituationKey[] = ['overall', 'vlhp', 'vrhp', 'day', 'night', 'bvp']
    const today = Object.fromEntries(keys.map((key) => [key, situationToSplitKey(key)]))
    const research = Object.fromEntries(keys.map((key) => [key, situationToSplitKey(key)]))
    expect(today).toEqual(research)
    expect(today.bvp).toBe('bvp')
  })

  it('supports game-level BVP when any hitter in the game has a sample', () => {
    const exportData = exportWithSplits([
      splitHitter('No Sample', null),
      splitHitter('Has Sample', bvpLine),
    ])
    const gameSupport = buildFilterSupportMatrix(exportData, { gamePk: 100001, player: null })
    expect(gameSupport.situation.bvp.supported).toBe(true)
    const missingPlayer = buildFilterSupportMatrix(exportData, {
      gamePk: 100001,
      player: { name: 'No Sample', team: 'Away Team', side: 'away' },
    })
    expect(missingPlayer.situation.bvp.supported).toBe(false)
  })
})
