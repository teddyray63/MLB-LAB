/** User-facing copy for pitch-type matchup panels (G0b: batter+pitch-type rates, SP mix context). */

export function pitchMatchupPanelSubtitle(pitchNote: string): string {
  return `Hitter rates by pitch type · SP repertoire context · ${pitchNote}`
}

export function pitchMatchupTeamCardSubtitle(oppSp: string, rowCount: number): string {
  const sp = oppSp || 'opposing SP'
  return `Hitter rates by pitch type · ${sp} repertoire · ${rowCount} rows`
}

export function pitchMatchupScopeNote(oppSp: string, pitchNote: string): string {
  const sp = oppSp || 'opposing SP'
  return `Hitter performance by pitch type · ${sp} mix in filter context · ${pitchNote}`
}

export function pitchFilterHitterLine(sp: string, count: number): string {
  return `Hitter rates by pitch type · ${sp} repertoire · ${count} hitter${count === 1 ? '' : 's'}`
}
