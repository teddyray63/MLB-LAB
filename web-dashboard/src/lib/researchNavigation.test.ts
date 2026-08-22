import { describe, expect, it } from 'vitest'
import { buildResearchNavigation } from './researchNavigation'
import { RESEARCH_SCHEMA_VERSION } from '../types/research'

function params(search: string): URLSearchParams {
  return new URLSearchParams(search)
}

describe('buildResearchNavigation', () => {
  const ctx = {
    currentParams: params('v=2&date=2026-08-01&game=100001&tf=season&sit=overall&pitch=FF'),
    selection: { date: '2026-08-01', gamePk: 100001 },
  }

  it('sets Today handoff params including tf=l10', () => {
    const { search } = buildResearchNavigation(ctx, {
      player: 'Test Hitter',
      game: 100001,
      side: 'away',
      pitcher: 'Home Pitcher',
      tab: 'overview',
      filters: { timeframe: 'l10' },
    })
    const next = params(search)
    expect(next.get('v')).toBe(String(RESEARCH_SCHEMA_VERSION))
    expect(next.get('date')).toBe('2026-08-01')
    expect(next.get('game')).toBe('100001')
    expect(next.get('player')).toBe('Test Hitter')
    expect(next.get('side')).toBe('away')
    expect(next.get('pitcher')).toBe('Home Pitcher')
    expect(next.get('tf')).toBe('l10')
    expect(next.get('sit')).toBe('overall')
    expect(next.get('pitch')).toBe('FF')
    expect(next.get('tab')).toBe('overview')
  })

  it('preserves existing query state when filters are not overridden', () => {
    const { search } = buildResearchNavigation(ctx, {
      player: 'Test Hitter',
      tab: 'overview',
    })
    const next = params(search)
    expect(next.get('tf')).toBe('season')
    expect(next.get('pitch')).toBe('FF')
    expect(next.get('game')).toBe('100001')
  })

  it('does not force l10 when filters omitted (non-Today paths)', () => {
    const { search } = buildResearchNavigation(ctx, {
      player: 'Test Hitter',
      game: 100001,
      side: 'home',
      tab: 'overview',
    })
    expect(params(search).get('tf')).toBe('season')
  })
})
