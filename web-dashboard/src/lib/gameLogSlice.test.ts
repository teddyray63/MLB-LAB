import { describe, expect, it } from 'vitest'
import { sliceGameLogByTimeframe, timeframeToGameLimit } from './gameLogSlice'
import type { GameLogEntry } from '../types/slate'

const sampleLog: GameLogEntry[] = Array.from({ length: 12 }, (_, i) => ({
  date: `2026-07-${String(20 - i).padStart(2, '0')}`,
  pa: 4,
  hits: 1,
  singles: 1,
  tb: 1,
  hr: 0,
  avg_ev: 90,
  barrels: 0,
}))

describe('timeframeToGameLimit', () => {
  it('maps l5 and l10 to numeric limits', () => {
    expect(timeframeToGameLimit('l5')).toBe(5)
    expect(timeframeToGameLimit('l10')).toBe(10)
  })

  it('returns null for season', () => {
    expect(timeframeToGameLimit('season')).toBeNull()
  })
})

describe('sliceGameLogByTimeframe', () => {
  it('returns empty array for undefined or empty input', () => {
    expect(sliceGameLogByTimeframe(undefined, 'l5')).toEqual([])
    expect(sliceGameLogByTimeframe([], 'l10')).toEqual([])
  })

  it('returns at most 5 entries for l5', () => {
    const sliced = sliceGameLogByTimeframe(sampleLog, 'l5')
    expect(sliced).toHaveLength(5)
    expect(sliced[0].date).toBe('2026-07-20')
    expect(sliced[4].date).toBe('2026-07-16')
  })

  it('returns at most 10 entries for l10', () => {
    const sliced = sliceGameLogByTimeframe(sampleLog, 'l10')
    expect(sliced).toHaveLength(10)
  })

  it('returns full log for season', () => {
    expect(sliceGameLogByTimeframe(sampleLog, 'season')).toHaveLength(12)
  })

  it('returns short log unchanged when smaller than requested timeframe', () => {
    const short = sampleLog.slice(0, 3)
    expect(sliceGameLogByTimeframe(short, 'l10')).toHaveLength(3)
    expect(sliceGameLogByTimeframe(short, 'l5')).toHaveLength(3)
  })
})
