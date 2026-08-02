import { BrowserRouter, Navigate, Route, Routes, useLocation } from 'react-router-dom'
import { AppLayout } from './layouts/AppLayout'
import { CommandCenter } from './pages/CommandCenter'
import { TopPlaysPage } from './pages/TopPlaysPage'
import { CategoryBoardsPage } from './pages/CategoryBoardsPage'
import { PlayerMatchupPage } from './pages/PlayerMatchupPage'
import { GameHubPage } from './pages/GameHubPage'
import { BattedBallsPage } from './pages/BattedBallsPage'
import { TeamSplitsPage } from './pages/TeamSplitsPage'
import { TodayPage } from './pages/TodayPage'
import { MatchupLabPage } from './pages/MatchupLabPage'
import { LeaderboardsPage } from './pages/LeaderboardsPage'
import { HistoryPage } from './pages/HistoryPage'
import { SettingsPage } from './pages/SettingsPage'
import { ResearchRedirect } from './components/ResearchRedirect'
import { ExportProvider } from './context/ExportContext'
import { ResearchProviders } from './context/ResearchContext'
import { useDailyExport } from './hooks/useDailyExport'
import { EXPORT_URL } from './data/loadExport'
import type { DailyExport } from './types/slate'

function LoadingState() {
  return (
    <div className="flex min-h-[40vh] items-center justify-center">
      <p className="text-sm text-[#8B949E]">Loading {EXPORT_URL}…</p>
    </div>
  )
}

function ErrorState({ message, onRetry }: { message: string; onRetry: () => void }) {
  return (
    <div className="mx-auto max-w-lg rounded-lg border border-[#DA3633] bg-[#4C1D1D]/40 p-6">
      <h2 className="text-lg font-semibold text-[#F85149]">Export not available</h2>
      <p className="mt-2 text-sm text-[#F0F6FC]">{message}</p>
      <p className="mt-3 text-xs text-[#8B949E]">
        Run{' '}
        <code className="rounded bg-[#21262D] px-1 py-0.5">python3 scripts/mlb_lab_runner.py</code>{' '}
        from the repo root to generate{' '}
        <code className="rounded bg-[#21262D] px-1 py-0.5">data/daily_export.json</code>.
      </p>
      <button
        type="button"
        onClick={onRetry}
        className="mt-4 rounded-md border border-[#30363D] bg-[#161B22] px-3 py-1.5 text-xs font-medium text-[#F0F6FC] hover:bg-[#21262D]"
      >
        Retry
      </button>
    </div>
  )
}

/** Redirect that preserves the original query string (legacy deep links). */
function QueryRedirect({ to }: { to: string }) {
  const { search } = useLocation()
  return <Navigate to={`${to}${search}`} replace />
}

export function App() {
  const { data, loading, error, reload } = useDailyExport()

  if (loading) return <LoadingState />
  if (error || !data) {
    return <ErrorState message={error ?? 'Unknown error'} onRetry={reload} />
  }

  return (
    <ExportProvider data={data}>
      <BrowserRouter>
        <ResearchProviders>
          <Routes>
            <Route element={<AppLayout exportDate={data.date} onReload={reload} />}>
            <Route index element={<Navigate to="/today" replace />} />

            {/* Canonical new-IA workspaces */}
            <Route path="today" element={<TodayPage />} />
            <Route path="research" element={<MatchupLabPage />} />
            <Route path="leaderboards" element={<LeaderboardsPage />} />
            <Route path="data-status" element={<HistoryPage />} />
            <Route path="settings" element={<SettingsPage />} />

            {/* Old new-IA aliases → canonical `/research` */}
            <Route path="game" element={<ResearchRedirect />} />
            <Route path="game/:gameId" element={<ResearchRedirect />} />
            <Route path="player" element={<ResearchRedirect />} />
            <Route path="player/:playerId" element={<ResearchRedirect />} />
            <Route path="matchup" element={<ResearchRedirect />} />
            <Route path="matchup/:gameId/:playerId" element={<ResearchRedirect />} />

            {/* Legacy pages — still fully operational, removed from primary nav */}
            <Route path="legacy">
              <Route path="command-center" element={<LegacyCommandCenter data={data} />} />
              <Route path="top-plays" element={<TopPlaysPage />} />
              <Route path="boards" element={<CategoryBoardsPage />} />
              <Route path="games" element={<GameHubPage />} />
              <Route path="player" element={<PlayerMatchupPage />} />
              <Route path="batted-balls" element={<BattedBallsPage />} />
              <Route path="splits" element={<TeamSplitsPage />} />
            </Route>

            {/* Backward-compatible redirects (bookmarks / deep links) */}
            <Route path="history" element={<QueryRedirect to="/data-status" />} />
            <Route path="top-plays" element={<QueryRedirect to="/legacy/top-plays" />} />
            <Route path="boards" element={<QueryRedirect to="/legacy/boards" />} />
            <Route path="games" element={<QueryRedirect to="/legacy/games" />} />
            <Route path="batted-balls" element={<QueryRedirect to="/legacy/batted-balls" />} />
            <Route path="splits" element={<QueryRedirect to="/legacy/splits" />} />

            <Route path="*" element={<Navigate to="/today" replace />} />
          </Route>
        </Routes>
        </ResearchProviders>
      </BrowserRouter>
    </ExportProvider>
  )
}

/** Legacy Command Center kept operational at /legacy/command-center. */
function LegacyCommandCenter({ data }: { data: DailyExport }) {
  return <CommandCenter data={data} />
}
