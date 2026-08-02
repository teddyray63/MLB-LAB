import { useEffect, useState } from 'react'
import { loadDailyExport } from '../data/loadExport'
import type { DailyExport } from '../types/slate'

interface UseDailyExportResult {
  data: DailyExport | null
  loading: boolean
  error: string | null
  reload: () => void
}

export function useDailyExport(): UseDailyExportResult {
  const [data, setData] = useState<DailyExport | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [tick, setTick] = useState(0)

  useEffect(() => {
    let cancelled = false
    setLoading(true)
    setError(null)

    loadDailyExport()
      .then((payload) => {
        if (!cancelled) setData(payload)
      })
      .catch((err: unknown) => {
        if (!cancelled) {
          setError(err instanceof Error ? err.message : 'Failed to load export')
          setData(null)
        }
      })
      .finally(() => {
        if (!cancelled) setLoading(false)
      })

    return () => {
      cancelled = true
    }
  }, [tick])

  return {
    data,
    loading,
    error,
    reload: () => setTick((n) => n + 1),
  }
}
