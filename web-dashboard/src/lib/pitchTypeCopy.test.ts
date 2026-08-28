import { describe, expect, it } from 'vitest'
import {
  pitchFilterHitterLine,
  pitchMatchupPanelSubtitle,
  pitchMatchupScopeNote,
  pitchMatchupTeamCardSubtitle,
} from './pitchTypeCopy'

const MISLEADING = [
  'Per-pitch vs opposing SP',
  'Batter vs opposing SP by pitch type',
  'Per-pitch stats vs',
]

describe('pitchTypeCopy', () => {
  it('does not imply pitcher-filtered hitter rates', () => {
    const lines = [
      pitchMatchupPanelSubtitle('All pitches'),
      pitchMatchupTeamCardSubtitle('Clayton Kershaw', 12),
      pitchMatchupScopeNote('Clayton Kershaw', 'All pitches'),
      pitchFilterHitterLine('Clayton Kershaw', 3),
    ]
    for (const line of lines) {
      for (const phrase of MISLEADING) {
        expect(line).not.toContain(phrase)
      }
    }
  })

  it('names hitter rates and SP repertoire context separately', () => {
    expect(pitchMatchupPanelSubtitle('FF')).toContain('Hitter rates by pitch type')
    expect(pitchMatchupPanelSubtitle('FF')).toContain('SP repertoire context')
    expect(pitchMatchupTeamCardSubtitle('SP Name', 5)).toContain('SP Name repertoire')
  })
})
