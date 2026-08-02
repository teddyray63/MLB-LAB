import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'
import fs from 'fs'
import path from 'path'
import { fileURLToPath } from 'url'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const EXPORT_SRC = path.resolve(__dirname, '../data/daily_export.json')
const EXPORT_URL = '/data/daily_export.json'

function serveDailyExport() {
  return {
    name: 'serve-daily-export',
    configureServer(server: { middlewares: { use: (fn: (req: any, res: any, next: () => void) => void) => void } }) {
      server.middlewares.use((req, res, next) => {
        if (req.url !== EXPORT_URL) {
          next()
          return
        }
        if (!fs.existsSync(EXPORT_SRC)) {
          res.statusCode = 404
          res.end('daily_export.json not found — run mlb_lab_runner.py first')
          return
        }
        res.setHeader('Content-Type', 'application/json')
        res.end(fs.readFileSync(EXPORT_SRC))
      })
    },
    closeBundle() {
      if (!fs.existsSync(EXPORT_SRC)) return
      const dest = path.resolve(__dirname, 'dist/data/daily_export.json')
      fs.mkdirSync(path.dirname(dest), { recursive: true })
      fs.copyFileSync(EXPORT_SRC, dest)
    },
  }
}

export default defineConfig({
  plugins: [react(), tailwindcss(), serveDailyExport()],
  server: {
    port: 5173,
    fs: {
      allow: ['..'],
    },
  },
})
