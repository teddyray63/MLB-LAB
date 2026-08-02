import { createContext, useContext, type ReactNode } from 'react'
import type { DailyExport } from '../types/slate'

const ExportContext = createContext<DailyExport | null>(null)

export function ExportProvider({
  data,
  children,
}: {
  data: DailyExport
  children: ReactNode
}) {
  return <ExportContext.Provider value={data}>{children}</ExportContext.Provider>
}

export function useExport(): DailyExport {
  const data = useContext(ExportContext)
  if (!data) {
    throw new Error('useExport must be used within ExportProvider')
  }
  return data
}
