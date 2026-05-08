# bradmontgomery.github.io

Personal website for [bradmontgomery.net](https://bradmontgomery.net), built with
the [`site`](https://github.com/bradmontgomery/site) static site generator.

## Stack

- **Static site generator**: [`site`](https://github.com/bradmontgomery/site) (custom, Python-based)
- **Templating**: Jinja2 (`templates/`)
- **Markdown**: CommonMark via markdown-it-py
- **CSS**: [simple.css](https://simplecss.org/) v2.3.7 (`static/simple.css-2.3.7/`)
- **Hosting**: GitHub Pages, served from `docs/`

## Directory Structure

```
content/           # Source content (markdown)
  blog/<slug>/
    index.md       # Blog posts (198 posts)
  pages/
    about.md       # Static pages
    contact.md
    services.md
  texts/           # Plain text files
    humans.txt
    llms.txt
    robots.txt
docs/              # Generated site output (do not manually edit)
static/            # Static assets copied into docs/
templates/         # Jinja2 HTML templates
  base.html        # Base layout (nav, head, footer)
  blog.html        # Individual blog post
  index.html       # Post listing (homepage and tag pages)
  page.html        # Static pages
  tags.html        # Tags listing
  content.md       # Template for new content (used by `site new`)
```

## Common Commands

All commands use `uvx` (requires [uv](https://docs.astral.sh/uv/) to be installed):

```bash
# Build the static site into docs/
uvx --from git+https://github.com/bradmontgomery/site site build

# Create a new blog post interactively
uvx --from git+https://github.com/bradmontgomery/site site new

# Run a local preview server at http://localhost:8000
uvx --from git+https://github.com/bradmontgomery/site site server
```

## Content Frontmatter

Blog posts (`content/blog/<slug>/index.md`) use this frontmatter schema:

```yaml
---
date: '2024-01-01T00:00:00+00:00'
title: Post Title
draft: false
tags:
- python
- django
slug: post-slug
description: 'Short description for listings and meta tags.'
markup: md
url: /blog/post-slug/
aliases:
- /blog/2024/01/01/post-slug/
---
```

Static pages (`content/pages/<name>.md`) use a simpler schema:

```yaml
---
title: "Page Title"
date: 2024-01-01T00:00:00-06:00
draft: false
---
```

## Workflow

1. **Write content**: Create or edit files in `content/`
2. **Preview locally**: Run `site server` and visit `http://localhost:8000`
3. **Build**: Run `site build` to regenerate `docs/`
4. **Publish**: Commit and push — GitHub Pages serves from `docs/` on the `main` branch

## Important Notes

- **Never manually edit files in `docs/`** — they are overwritten on each build
- Set `draft: true` in frontmatter to prevent a post from appearing in the built site
- The `aliases` field preserves old URLs from prior blog platforms
- The `url` field controls the canonical path for the generated page
- RSS/Atom feeds are auto-generated at `/feed/rss/rss.xml` and `/feed/atom/atom.xml`

## Writing
If you are ever used to write content (anything that lives in or is a subdirectory of `content/`), append a footer
note explaining that the post was written in collaboration with an AI model (name yourself).
