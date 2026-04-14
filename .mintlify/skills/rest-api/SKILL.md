---
name: quotes-rest-api
description: >-
  REST integration skill for the Quotes API — endpoints, query parameters, response fields,
  and error handling. Use for implementation tasks, debugging HTTP status codes, and validating
  category names.
license: MIT
compatibility: Any HTTP/1.1 client; responses are JSON. Local server assumed at port 3000 unless overridden.
metadata:
  skill_type: integration
  api_version: "1.0.0"
---

# Quotes REST API

## Summary

Public JSON API: list quotes, random quote, quote by ID, list categories. No auth headers.

## Endpoints

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/quotes` | List quotes; optional `category`, `limit` |
| GET | `/quotes/random` | One random quote; optional `category` |
| GET | `/quotes/{id}` | Single quote by string ID |
| GET | `/categories` | Available category names |

## Parameters

- **category** (query): One of `marco original`, `motivation`, `philosophy`, `technology`, `wisdom`. Use correct spelling and URL encoding for spaces.
- **limit** (query, list quotes): Positive integer cap on returned items.

## Success model

- Quote object fields typically include: `id`, `text`, `author`, `category` (see OpenAPI schemas for authoritative field list).

## Errors

- Client errors return JSON with `error` and `message` keys (e.g. unknown category) — align examples with the Introduction page.

## Testing locally

```bash
curl http://localhost:3000/quotes/random
curl "http://localhost:3000/quotes/random?category=technology"
```
