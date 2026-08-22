import { describe, expect, it } from 'vitest'
import { isResearchContextNavPath, primaryNavLinkTo } from './researchChromeNav'

describe('researchChromeNav', () => {
  it('identifies research-context nav paths', () => {
    expect(isResearchContextNavPath('/today')).toBe(true)
    expect(isResearchContextNavPath('/research')).toBe(true)
    expect(isResearchContextNavPath('/leaderboards')).toBe(true)
    expect(isResearchContextNavPath('/settings')).toBe(false)
  })

  it('preserves search among research-context routes', () => {
    const search = '?v=2&game=100001&player=Test+Hitter&tf=l10'
    expect(primaryNavLinkTo('/today', search)).toEqual({ pathname: '/today', search })
    expect(primaryNavLinkTo('/research', search)).toEqual({ pathname: '/research', search })
    expect(primaryNavLinkTo('/leaderboards', search)).toEqual({
      pathname: '/leaderboards',
      search,
    })
  })

  it('does not preserve search for unrelated routes', () => {
    expect(primaryNavLinkTo('/settings', '?v=2&game=1')).toBe('/settings')
    expect(primaryNavLinkTo('/data-status', '?v=2&game=1')).toBe('/data-status')
  })
})
