# Documentation agent instructions — Quotes API

These instructions apply to all automated documentation work for this Mintlify project (dashboard agent, API, or integrations). They extend the default Mintlify agent behavior.

## Product facts

- **Product name:** Quotes API (see `docs.json` `name`).
- **Positioning:** Lightweight, **unauthenticated** REST API; JSON only; consistent error envelope.
- **OpenAPI:** Single file `openapi.yaml`; `docs.json` references it under **API Reference** navigation.
- **Local base URL:** `http://localhost:3000` (also in OpenAPI `servers`). Call out that production URL is not yet documented when users ask for “prod”.

## Voice and audience

- Write for backend and full-stack developers who want to copy-paste and go.
- Use **second person** (“you”) for procedures; **active voice**.
- Keep lines scannable: short paragraphs, tables for endpoint summaries, `curl` for shell examples.

## Code and examples

- Prefer **`curl`** for shell examples unless the page is explicitly about a language SDK (none shipped yet).
- Show **full URLs** including query strings; URL-encode spaces in category names (`marco+original` or `%20`).
- For API reference pages generated from OpenAPI, ensure descriptions stay in sync with `openapi.yaml` when editing behavior — update the spec first, then adjust MDX only for extra narrative or playground notes.
- Include **success and error** samples where non-obvious (e.g. invalid category).

## Structure and navigation

- **Get Started** group: `introduction`, `quickstart`.
- **API Reference** group: OpenAPI-driven pages under `api-reference/` — keep filenames aligned with `docs.json` `navigation.groups` `pages` array.
- New user-facing pages: add frontmatter `title` and `description`; keep `description` under ~300 characters for LLM directory snippets.

## AI and LLM-facing assets

- Custom **`llms-full.txt`**, **`skill.md`**, and **`.mintlify/skills/**`** are maintained in-repo. If you change API behavior, update those assets in the same PR when the change is user-visible.
- Do not duplicate secrets (none required for this API).

## What not to do

- Do not add fake authentication, rate limits, or enterprise features unless they appear in `openapi.yaml` or product requirements.
- Do not rename public paths (`/quotes`, `/categories`, etc.) in prose without matching OpenAPI and examples.
