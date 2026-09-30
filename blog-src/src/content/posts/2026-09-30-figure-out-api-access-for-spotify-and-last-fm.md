---
title: "Figure out API access for Spotify and Last.fm"
date: 2026-09-30
description: "Figure out API access for Spotify and Last.fm"
tags: [spotify, lastfm, report]
public: false
---

*Report — a research report (2026-09-30), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary

Both APIs support what's needed. Spotify requires a one-time OAuth Authorization Code flow (Marvin signs in once in a browser) that yields a refresh token good for 6 months of use, read through `user-top-read` + `user-read-recently-played` scopes — Development Mode is sufficient since jimbo-api serves one user, not 250k. Last.fm is simpler: register an app for an API key + shared secret, then one manual auth step yields a session key with no expiry. Both slot into jimbo-api's existing secret-in-env pattern; neither needs new infrastructure, only two new services shaped like `spotify.ts` and `google-auth.ts` respectively.

## From prior context

None. The vault note carries no linked prior-context notes (`related: []`), and no `skill_context.prior_context` was supplied for this dispatch. The note's own `<!-- groomed -->` block already establishes ground truth I'm treating as settled without re-verifying:

- jimbo-api's only Spotify code today is `src/services/spotify.ts` — client-credentials flow, public catalog search only, consumed by `src/routes/enrich.ts` for Boris's gig enrichment. No user-authorized Spotify access exists.
- No Last.fm integration exists in jimbo-api at all.
- The real goal is broader than the title — Jimbo knowing Marvin's music taste — with Spotify/Last.fm as the assumed (not mandated) means.

## New findings

### Spotify: Authorization Code Flow

**Scopes needed** (developer.spotify.com/documentation/web-api/concepts/scopes):
- `user-top-read` — top artists and tracks (`GET /me/top/artists`, `GET /me/top/tracks`)
- `user-read-recently-played` — last ~50 played tracks (`GET /me/player/recently-played`)
- Optional: `user-read-currently-playing` / `user-read-playback-state` if "what's playing right now" ever matters

**One-time app registration** (developer.spotify.com/documentation/web-api/concepts/apps):
1. Create an app in the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) — app name + description (shown to the user on the consent screen), accept the Developer Terms of Service.
2. In Edit Settings, add a **Redirect URI** to the allowlist — this must exactly match what the auth request sends (scheme, case, trailing slash all matter). For a one-time personal setup, `http://127.0.0.1:PORT/callback` or even a jimbo-api route works; it only needs to resolve once during setup.
3. Note the Client ID and Client Secret (secret must never be exposed client-side).

**Auth flow** (developer.spotify.com/documentation/web-api/tutorials/code-flow, /refreshing-tokens):
1. Send Marvin's browser to `GET https://accounts.spotify.com/authorize` with `client_id`, `response_type=code`, `redirect_uri`, `scope`, `state`.
2. Marvin logs in and approves; Spotify redirects to the callback with `?code=...`.
3. Exchange the code: `POST https://accounts.spotify.com/api/token` with `grant_type=authorization_code`, `code`, `redirect_uri`, and `Authorization: Basic base64(client_id:client_secret)`. Response includes `access_token` (1 hour) and `refresh_token`.
4. Thereafter, refresh via `grant_type=refresh_token` — same shape as `jimbo-api/src/services/google-auth.ts`'s existing pattern (cached access token, refreshed on expiry using a long-lived credential).

**Refresh token lifetime — the one real gotcha:** refresh tokens issued via the Developer Dashboard now expire **6 months after the user first signs in**; refreshing does *not* reset the clock. At expiry the token endpoint returns `400 invalid_grant` and Marvin has to redo the one-time browser consent. This is a hard difference from the Google pattern, where the refresh token is effectively permanent — plan for a periodic "Spotify needs reauth" nudge rather than assuming set-and-forget.

**Development Mode is enough — do not pursue Extended Quota Mode.** Since May 2025, Extended Quota Mode requires a registered legal business, an active launched service, and 250,000+ monthly active users. That's irrelevant here: jimbo-api serves one user. As of the February 2026 Dev Mode changes, Development Mode apps must have an owner with an active Spotify **Premium** subscription (app stops working if it lapses), and new apps are capped at 5 authorized users — both fine for a single-user tool. The endpoints needed (`/me/top/artists`, `/me/top/tracks`, `/me/player/recently-played`) are explicitly unaffected by the February 2026 endpoint deprecations, which targeted bulk/automated-misuse surfaces (e.g. `audio-features`, `related-artists`, `recommendations`), not personal listening history.

**Rate limits:** Spotify doesn't publish a numeric cap; it's a rolling 30-second window, tighter in Development Mode than Extended Quota Mode. For a personal-taste poll (say, once a day), this is a non-issue.

### Last.fm: API key + session key

**Registration** (last.fm/api/account/create — requires a logged-in Last.fm account): fill in application name, description, and website/contact email. Callback URL can be left blank for a non-web (desktop-style) auth flow. Submission is instant — no review process, unlike Spotify's Extended Quota Mode. Returns an **API key** and a **shared secret** immediately, retrievable later at last.fm/api/accounts.

**Auth flow** (last.fm/api/webauth):
1. `auth.getToken` (signed with API key + shared secret) returns a token valid for 60 minutes.
2. Send Marvin to `https://www.last.fm/api/auth/?api_key=...&token=...` to grant permission — no callback needed if using the token/desktop variant rather than the callback-URL web variant.
3. Call `auth.getSession` with the token (one-time use — it's consumed on exchange) to receive a **session key**.
4. The session key **has no expiry by default** — store it once, use indefinitely, until Marvin manually revokes it in Last.fm account settings.

This is materially simpler than Spotify's flow: no refresh cycle, no reauth cadence, no quota tiers to worry about.

**Endpoints for taste-profiling** once authenticated: `user.getRecentTracks`, `user.getTopArtists`, `user.getTopTracks` (all take a `user` param — Marvin's Last.fm username — and don't strictly require the session key for public profiles, though the session key is needed if his profile/scrobbles are private).

**Rate limits:** unpublished exact number; Last.fm's guidance is "don't hammer it with several calls/second" — error code 29 (`Rate Limit Exceeded`) if you do. A daily or hourly poll is well within bounds.

## Comparison

| | Spotify | Last.fm |
|---|---|---|
| Credential type | OAuth 2.0 Authorization Code, refresh token | API key + shared secret, then session key |
| One-time manual step | Yes — browser consent | Yes — browser consent |
| Credential lifetime | Refresh token expires 6 months after first sign-in; must redo consent | Session key: indefinite, until manually revoked |
| Personal-use tier | Development Mode (sufficient; Extended Quota Mode is for 250k+ MAU businesses) | No tiers — one registration, immediate key |
| Extra account requirement | App owner needs active Spotify Premium | None |
| Data available | Top artists/tracks (multiple time ranges), recently played (~50 tracks) | Recent tracks, top artists, top tracks — deeper scrobble history if Marvin already scrobbles |
| Registration friction | Dashboard app + ToS acceptance + redirect URI allowlist | Single form, no review |

## Recommendation

Build both — they're complementary, not redundant. Spotify gives native top-artists/top-tracks with genre/popularity metadata (same shape jimbo-api already parses in `spotify.ts`); Last.fm gives a longer scrobble history if Marvin's been scrobbling, and its session key is a lower-maintenance credential than Spotify's 6-month-expiring refresh token.

Concretely:
1. **Spotify**: add a new service alongside the existing `spotify.ts`, modeled on `google-auth.ts`'s refresh-token-cache pattern rather than `spotify.ts`'s client-credentials pattern (they're different grant types — don't try to reuse `spotify.ts`'s token cache directly). Store `SPOTIFY_REFRESH_TOKEN` next to the existing `SPOTIFY_CLIENT_ID`/`SPOTIFY_CLIENT_SECRET` in `/opt/jimbo-api.env` on the VPS (same destination google.md documents for the Google OAuth secrets). Because the refresh token expires every 6 months, add a lightweight check (e.g. surfaced in a healthcheck or briefing) that flags when reauth is due — this is the one operational cost Google's pattern doesn't have.
2. **Last.fm**: new service, new env vars (`LASTFM_API_KEY`, `LASTFM_SHARED_SECRET`, `LASTFM_SESSION_KEY`) in the same env file. Simpler to build and to maintain — no refresh logic needed at all, just a signed-request helper.
3. **Marvin's manual steps** (not this task, but sequenced for him): register the Spotify app in the Developer Dashboard and add a redirect URI; register the Last.fm API account; run the one-time auth flow for each to mint the refresh token / session key, then hand those to whoever implements the services.
4. If either API turns out more awkward in practice than this research suggests, the fallback per the note's own framing is to drop the assumed means (these two APIs) without dropping the goal (Jimbo learning Marvin's taste) — e.g. manual taste logging via `/log-food`-style quick capture. Not needed now; both APIs check out as straightforward for a single-user read-only use case.

## Sources

1. [Spotify — Authorization Code Flow](https://developer.spotify.com/documentation/web-api/tutorials/code-flow) — auth request/token exchange parameters, redirect URI rules.
2. [Spotify — Refreshing tokens](https://developer.spotify.com/documentation/web-api/tutorials/refreshing-tokens) — 6-month refresh token lifetime, rotation behavior, `invalid_grant` handling.
3. [Spotify — Scopes](https://developer.spotify.com/documentation/web-api/concepts/scopes) — exact scope strings (`user-top-read`, `user-read-recently-played`, etc.) and their descriptions.
4. [Spotify — Apps (registration)](https://developer.spotify.com/documentation/web-api/concepts/apps) — Dashboard app creation steps, Developer ToS, redirect URI configuration.
5. [Spotify — February 2026 Web API Dev Mode migration guide](https://developer.spotify.com/documentation/web-api/tutorials/february-2026-migration-guide) — Premium requirement for Dev Mode app owners, 5-user cap for new apps, confirms `/me/top/*` and `/me/player/recently-played` are unaffected.
6. [Spotify — Rate Limits](https://developer.spotify.com/documentation/web-api/concepts/rate-limits) — rolling 30-second window, Dev Mode vs Extended Quota Mode.
7. [Spotify Community — Clarification on Extended Quota Mode Eligibility](https://community.spotify.com/t5/Spotify-for-Developers/Clarification-on-Extended-Quota-Mode-Eligibility/td-p/7503072) — confirms May 2025 tightening to registered business + 250k MAU threshold.
8. [Last.fm — Web application authentication](https://www.last.fm/api/webauth) — `auth.getToken` → user grant → `auth.getSession` flow, 60-minute token validity, session key's indefinite lifetime.
9. [Last.fm — Create an API account](https://www.last.fm/api/account/create) — registration fields (name, description, website), instant API key + shared secret issuance.
10. [Last.fm Support — API rate limit for user API](https://support.last.fm/t/api-rate-limit-for-user-api/112610) — no published numeric limit; guidance to avoid rapid-fire calls, error code 29 on abuse.
11. `jimbo-api/src/services/spotify.ts` (repo, read directly) — existing client-credentials pattern, token cache shape to diverge from for the new OAuth service.
12. `jimbo-api/src/services/google-auth.ts` (repo, read directly) — the refresh-token-cache pattern to reuse for Spotify's user-auth service.
13. `jimbo-api/docs/modules/google.md` (repo, read directly) — confirms secrets deploy to `/opt/jimbo-api.env` on the VPS; the destination for the new Spotify/Last.fm env vars.

