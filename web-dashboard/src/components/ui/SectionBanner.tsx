interface SectionBannerProps {
  label: string
  count?: number
}

export function SectionBanner({ label, count }: SectionBannerProps) {
  return (
    <div className="flex items-center justify-between rounded-md bg-[#0B1F3A] px-4 py-2.5">
      <h2 className="text-xs font-bold uppercase tracking-[0.14em] text-[#58A6FF]">{label}</h2>
      {count != null && (
        <span className="text-xs font-medium text-[#8B949E]">{count} rows</span>
      )}
    </div>
  )
}
