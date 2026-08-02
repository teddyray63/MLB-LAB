import type { ReactNode } from 'react'

interface CardProps {
  title?: string
  subtitle?: string
  action?: ReactNode
  children: ReactNode
  className?: string
}

export function Card({ title, subtitle, action, children, className = '' }: CardProps) {
  return (
    <section
      className={`overflow-hidden rounded-lg border border-[#30363D] bg-[#161B22] shadow-lg shadow-black/20 ${className}`}
    >
      {(title || action) && (
        <header className="flex items-start justify-between gap-3 border-b border-[#21262D] px-4 py-3">
          <div>
            {title && <h3 className="text-sm font-semibold tracking-tight text-[#F0F6FC]">{title}</h3>}
            {subtitle && <p className="mt-0.5 text-xs text-[#8B949E]">{subtitle}</p>}
          </div>
          {action}
        </header>
      )}
      <div className="p-4">{children}</div>
    </section>
  )
}
