import { Link, Outlet, useLocation } from 'react-router-dom'
import { ResearchChrome } from '../components/ResearchChrome'

interface NavItem {
  to: string
  label: string
  /** Extra path prefixes that should mark this item active */
  match?: string[]
}

const PRIMARY_NAV: NavItem[] = [
  { to: '/today', label: 'Today' },
  { to: '/research', label: 'Research' },
  { to: '/leaderboards', label: 'Leaderboards' },
  { to: '/data-status', label: 'Data Status', match: ['/history'] },
  { to: '/settings', label: 'Settings' },
]

interface AppLayoutProps {
  exportDate?: string
  onReload?: () => void
}

function isActive(pathname: string, item: NavItem): boolean {
  if (pathname === item.to) return true
  if (pathname.startsWith(`${item.to}/`)) return true
  return item.match?.some((p) => pathname === p || pathname.startsWith(`${p}/`)) ?? false
}

export function AppLayout({ exportDate, onReload }: AppLayoutProps) {
  const { pathname } = useLocation()

  return (
    <div className="min-h-screen bg-[#0D1117] text-[#F0F6FC]">
      <header className="sticky top-0 z-20 border-b border-[#30363D] bg-[#0D1117]/95 backdrop-blur">
        <div className="mx-auto flex max-w-[1500px] flex-wrap items-center justify-between gap-4 px-4 py-3">
          <div>
            <p className="text-[10px] font-semibold uppercase tracking-[0.18em] text-[#58A6FF]">
              MLB-LAB
            </p>
            <h1 className="text-lg font-bold tracking-tight">Research Dashboard</h1>
          </div>
          <div className="flex flex-wrap items-center gap-3">
            {exportDate && (
              <span className="hidden text-xs text-[#8B949E] sm:inline">Export: {exportDate}</span>
            )}
            {onReload && (
              <button
                type="button"
                onClick={onReload}
                className="rounded-md border border-[#30363D] px-2.5 py-1 text-[11px] text-[#8B949E] hover:bg-[#161B22] hover:text-[#F0F6FC]"
              >
                Reload
              </button>
            )}
            <nav aria-label="Primary" className="flex flex-wrap items-center gap-1">
              {PRIMARY_NAV.map((item) => {
                const active = isActive(pathname, item)
                return (
                  <Link
                    key={item.to}
                    to={item.to}
                    aria-current={active ? 'page' : undefined}
                    className={`rounded-md px-3 py-1.5 text-xs font-medium transition-colors ${
                      active
                        ? 'bg-[#1F6FEB33] text-[#58A6FF]'
                        : 'text-[#8B949E] hover:bg-[#161B22] hover:text-[#F0F6FC]'
                    }`}
                  >
                    {item.label}
                  </Link>
                )
              })}
            </nav>
          </div>
        </div>
      </header>
      <main className="mx-auto max-w-[1500px] px-4 py-5">
        <ResearchChrome />
        <Outlet />
      </main>
    </div>
  )
}
