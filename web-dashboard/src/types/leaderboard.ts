import type { PlayCategory } from './slate'

/** Leaderboard scope — URL key `scope`. */
export type LeaderboardScope = 'game' | 'slate' | 'league'

/** Workspace category/view — URL key `tab` on /leaderboards. */
export type LeaderboardCategory = 'top-plays' | PlayCategory

export const LEADERBOARD_SCOPES: { key: LeaderboardScope; label: string; description: string }[] = [
  {
    key: 'game',
    label: 'Selected Game',
    description: 'Rows for the game selected in the header',
  },
  {
    key: 'slate',
    label: "Today's Slate",
    description: 'All valid games on the export date',
  },
  {
    key: 'league',
    label: 'Entire League',
    description: 'Widest dataset present in the export (not full-season coverage)',
  },
]

/** Category navigation groups — export categories are authoritative; labels are UI-only. */
export const LEADERBOARD_CATEGORY_GROUPS: {
  label: string
  categories: { key: LeaderboardCategory; label: string }[]
}[] = [
  {
    label: 'Curated',
    categories: [{ key: 'top-plays', label: 'Top Plays' }],
  },
  {
    label: 'Overall Hitting',
    categories: [{ key: 'hits', label: 'Hits' }],
  },
  {
    label: 'Contact Quality',
    categories: [{ key: 'singles', label: 'Singles' }],
  },
  {
    label: 'Power',
    categories: [
      { key: 'total_bases', label: 'Total Bases' },
      { key: 'home_runs', label: 'Home Runs' },
    ],
  },
  {
    label: 'Plate Discipline',
    categories: [{ key: 'hrr', label: 'HRR' }],
  },
]

export const LEADERBOARD_CATEGORIES: LeaderboardCategory[] = [
  'top-plays',
  'hits',
  'singles',
  'total_bases',
  'hrr',
  'home_runs',
]
