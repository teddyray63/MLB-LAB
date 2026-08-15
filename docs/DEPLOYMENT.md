# MLB-LAB Dashboard — Static Deployment

Manual deployment guide for the React/Vite dashboard (`web-dashboard/`).

## Architecture

- **Build:** Vite static SPA → `web-dashboard/dist/`
- **Data:** Promoted export is injected at `data/daily_export.json` **before** build (file stays gitignored)
- **Bundle path:** `prebuild` runs `sync-data` → `public/data/daily_export.json`; Vite `closeBundle` also copies to `dist/data/daily_export.json`
- **Runtime:** Browser fetches `/data/daily_export.json` from the static host (bundled in `dist/`)
- **Artifact:** Upload the entire `web-dashboard/dist/` directory to a static host
- **SPA routing:** `web-dashboard/public/_redirects` provides Netlify-style fallback (`/* → /index.html`)

Export files are **not** committed to git. Remote git checkout alone cannot supply `daily_export.json`.

## Manual deployment flow

### 1. Obtain approved export

Use a validated candidate or the current promoted live export on the operator machine. Record the approved SHA256.

### 2. Verify / pin SHA

```bash
shasum -a 256 /path/to/daily_export.json
```

Pin the exact 64-character lowercase hex SHA256 for this deploy.

### 3. Install export for build

From repository root:

```bash
chmod +x scripts/prepare_export_for_build.sh

scripts/prepare_export_for_build.sh \
  <EXPECTED_SHA256> \
  <SOURCE_PATH>
```

The script verifies the source SHA, copies to `data/daily_export.json`, and re-verifies the destination. If source is already `data/daily_export.json` with matching SHA, copy is skipped.

### 4. Build dashboard

```bash
cd web-dashboard
npm run build
```

### 5. Verify dist export SHA

```bash
shasum -a 256 dist/data/daily_export.json
```

Must match the pinned SHA from step 2.

### 6. Upload dist/

Deploy **all** contents of `web-dashboard/dist/` to your static host (Cloudflare Pages, Netlify, S3+CDN, etc.). Configure SPA fallback if the host does not read `_redirects` automatically.

### 7. Smoke-test

After upload, verify:

- `/` loads
- `/research` loads (client route; requires SPA fallback)
- `/today` loads
- `/data/daily_export.json` returns JSON with expected date and `player_logs`

## Rollback

- **Data rollback:** Restore a previous approved export from `data/backups/` or a saved candidate; run `prepare_export_for_build.sh` with that file’s SHA; rebuild and redeploy `dist/`.
- **Artifact rollback:** Redeploy a previously saved `dist/` tarball from a known-good build if kept locally.

Always record the export SHA256 deployed with each release.

## Explicit non-goals (current)

- No git-tracked `daily_export.json`
- No automatic CI deploy (yet)
- No backend web service for the React dashboard
- No runtime remote JSON fetch (export is baked into `dist/` at build time)

## Future automation

Planned path (not implemented):

1. After promotion, upload `data/daily_export.json` to artifact storage keyed by SHA256
2. CI job (manual or workflow dispatch) fetches export by pinned SHA
3. Run `prepare_export_for_build.sh` → `npm run build`
4. Upload `dist/` to static host

See `scripts/prepare_export_for_build.sh` for the local export-injection step.
