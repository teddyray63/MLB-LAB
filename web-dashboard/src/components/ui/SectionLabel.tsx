interface SectionLabelProps {
  children: string
  id?: string
}

/** Uppercase section kicker beneath a page header (Phase F3). */
export function SectionLabel({ children, id }: SectionLabelProps) {
  return (
    <h3
      id={id}
      className="text-[10px] font-semibold uppercase tracking-[0.14em] text-[#8B949E]"
    >
      {children}
    </h3>
  )
}
