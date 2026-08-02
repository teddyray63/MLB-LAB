import { useLayoutEffect, type RefObject } from 'react'

/** Writes an element's border-box height to a CSS custom property on `:root`. */
export function useLayoutHeightVar(
  ref: RefObject<HTMLElement | null>,
  cssVar: string,
  enabled = true,
) {
  useLayoutEffect(() => {
    const root = document.documentElement
    const el = ref.current

    if (!enabled || !el) {
      root.style.setProperty(cssVar, '0px')
      return
    }

    const update = () => {
      root.style.setProperty(cssVar, `${el.getBoundingClientRect().height}px`)
    }

    update()
    const observer = new ResizeObserver(update)
    observer.observe(el)
    window.addEventListener('resize', update)

    return () => {
      observer.disconnect()
      window.removeEventListener('resize', update)
      root.style.setProperty(cssVar, '0px')
    }
  }, [ref, cssVar, enabled])
}
