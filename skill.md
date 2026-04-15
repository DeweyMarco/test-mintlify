---
name: quotes-api-docs
description: >-
  Mintlify documentation for the Quotes API — a public REST API for listing, filtering,
  and retrieving quotes by category. Use when answering questions about endpoints, request
  parameters, categories, error shapes, local development, or navigating this docs site.
license: MIT
compatibility: >-
  HTTP clients only; no SDK required. Base URL is http://localhost:3000 for local docs
  playground configuration. Production base URL is not yet published.
metadata:
  product: Quotes API
  docs_framework: Mintlify
  openapi: openapi.yaml
---

# Quotes API — documentation skill

## Capabilities

- Explain how to list quotes, fetch a random quote, get a quote by ID, and list categories.
- Describe valid categories and how URL encoding works for multi-word categories (e.g. `marco original`).
- Show example `curl` requests matching the quickstart and API reference.
- Interpret JSON success and error responses, including `invalid_category` and validation messages.

## When to use this skill

Use this skill when the user is integrating with the Quotes API, writing examples, or navigating the Mintlify docs (introduction, quickstart, OpenAPI-based reference pages).

## Constraints

- The API does not require authentication; do not invent API keys or OAuth flows for this product.
- Prefer the documented base URL from `docs.json` / OpenAPI (`http://localhost:3000`) unless the user provides another environment.
- Categories are fixed; invalid categories return a `400` with a message listing valid values.

## Workflows

### Get a random quote

1. `GET /quotes/random` with optional `?category=<name>` (URL-encoded spaces as `+` or `%20`).
2. Parse JSON body: `id`, `text`, `author`, `category`.

### List quotes with filters

1. `GET /quotes` with optional `category` and `limit`.
2. Response includes `quotes` array and `total` where applicable.

### Resolve a quote by ID

1. `GET /quotes/{id}`.
2. Handle `404` if the ID does not exist (see API reference for exact error shape).

### Discover categories

1. `GET /categories` to enumerate valid category names for filters.

## Integration notes

- OpenAPI specification path in the repo: `openapi.yaml` (referenced from `docs.json`).
- For Mintlify-specific behavior (navigation, playground, components), defer to the published docs site structure.
