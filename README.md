# IGPC Live System

## Locked operating chain
CLIENT → CLIENT LINK → CLIENT PORTAL → VIRTUAL LIBRARY → VALIDATION GATE → RELEASE → EXISTING PROJECT FILES → ANALYTICS → DIAGNOSTICS → REPORTS

The Virtual Library flow itself is preserved as:
CLIENT → CLIENT LINK → CLIENT PORTAL → VIRTUAL LIBRARY → VALIDATION GATE → RELEASE → EXISTING PROJECT FILES

## Live architecture
- Render runs `server.js` and the API.
- PostgreSQL stores submissions, original CSV text, validation results and release state.
- GitHub Pages can host the static frontend.
- Set `window.IGPC_API_BASE` in `public/config.js` to the Render API URL when the frontend is hosted on GitHub Pages.
- When frontend and API are both on Render, leave it blank so the frontend uses the same origin.

## Render
Create a Render Web Service from this repository. Build: `npm install`. Start: `npm start`. Add `DATABASE_URL` for a Render/Postgres database. Render automatically redeploys linked-branch pushes when auto deploy is enabled.

## GitHub Pages
Enable Pages using GitHub Actions. The workflow publishes `/public`. GitHub Pages is static, so the live upload/validation API remains on Render.

## Production notes
- Do not put database passwords or provider API keys in GitHub.
- Add authentication/signed client links before exposing the upload endpoint to external clients.
- For SMS/email, connect provider credentials through Render environment variables.
