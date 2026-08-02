import { Navigate, useLocation, useParams } from 'react-router-dom'
import { buildResearchRedirectPath } from '../lib/routeRedirects'

/** Redirect old IA player/matchup/game routes to canonical `/research`. */
export function ResearchRedirect() {
  const { search } = useLocation()
  const { gameId, playerId } = useParams()
  const target = buildResearchRedirectPath(search, { gameId, playerId })
  return <Navigate to={target} replace />
}
