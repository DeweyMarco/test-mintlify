---
name: "translation"
on:
  push: deweymarco/test-mintlify
automerge: true
---

Translate any MDX or markdown files changed by the last merged PR into all supported languages, and mirror any structural changes to the navigation config.

## Steps

1. Detect which languages this project supports by inspecting the repo structure (for example, look for language subdirectories such as `es/`, `fr/`, `de/`, `ja/`, or similar patterns). Do not assume a fixed set of languages—derive them from what exists.
2. Identify all files changed in the last merged PR using git, including added, modified, and deleted files. Only process English-language source files; skip any files that already live inside a language subdirectory.
3. For each **deleted** source file, delete the corresponding file in every supported language directory, mirroring the source path.
4. For each **added or modified** source file, translate the changed content into each supported language. Only change content that changed in the git diff, plus any surrounding content required to maintain coherency. Write translated files to the corresponding path in each language directory, mirroring the source file path.
5. If the navigation config file was changed (detect its name and location from the repo—common names include `docs.json`, `mint.json`, or similar), apply the equivalent structural changes to each translated language section in that file. Mirror additions, removals, and renames. Mirror any new redirects by prefixing both `source` and `destination` with the language code.
6. Open a pull request with all translated files and any navigation config changes.

## Important

- Preserve all markup, frontmatter, component syntax, code samples, prop names, and code block titles exactly. Only translate prose content.
- Use real quotation marks (`"`, `'`) instead of HTML entities (`&quot;`, `&#39;`, `&amp;`).
- The exact conventions for this project (path structure, config file format, language subdirectory names) vary. Detect them from the repo rather than assuming any specific layout.
- If no translatable content changed in the last merged PR, do nothing.