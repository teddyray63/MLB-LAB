import { describe, expect, it } from 'vitest'
import { resolveResearchSelection, firstValidGamePk } from './researchResolver'
import fixture from '../test-fixtures/research-handoff.json'
import type { DailyExport } from '../types/slate'

const exportData = fixture as unknown as DailyExport

describe('resolveResearchSelection', () => {
  it('resolves game and hitter from URL input', () => {
    const sel = resolveResearchSelection(exportData, {
      date: '2026-08-01',
      gamePk: 100001,
      playerName: 'Test Hitter',
      teamSide: 'away',
    })
    expect(sel.gamePk).toBe(100001)
    expect(sel.player?.name).toBe('Test Hitter')
    expect(sel.player?.side).toBe('away')
    expect(sel.awayTeam).toBe('Away Team')
    expect(sel.homeTeam).toBe('Home Team')
  })

  it('preserves side from lineup match', () => {
    const sel = resolveResearchSelection(exportData, {
      gamePk: 100001,
      playerName: 'Test Hitter',
    })
    expect(sel.teamSide).toBe('away')
    expect(sel.player?.team).toBe('Away Team')
  })

  it('warns when player is not in selected game', () => {
    const sel = resolveResearchSelection(exportData, {
      gamePk: 100001,
      playerName: 'Unknown Player',
    })
    expect(sel.player).toBeNull()
    expect(sel.warnings.some((w) => w.includes('Unknown Player'))).toBe(true)
  })

  it('falls back when game_pk is missing from export', () => {
    const sel = resolveResearchSelection(exportData, {
      gamePk: 999999,
      playerName: 'Test Hitter',
    })
    expect(sel.gamePk).toBe(firstValidGamePk(exportData))
    expect(sel.warnings.some((w) => w.includes('999999'))).toBe(true)
  })

  it('defaults to export date and first game when URL sparse', () => {
    const sel = resolveResearchSelection(exportData, {})
    expect(sel.date).toBe('2026-08-01')
    expect(sel.gamePk).toBe(100001)
  })
})
