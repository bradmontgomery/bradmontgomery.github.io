# bradmontgomery.github.io

_refreshed, simpler bradmontgomery.net -- coming soon_


## Goals

- Ability to write content in markdown
- simple template layouts (e.g. something like jinja)
- ability to keep the same URLs that I had in django-blargg
- command-line tool to build content.
- publish on github pages

### Content

Directory structure is broken into

    content/
        blog/
            <title-slug>/index.md
        page/
            <title>.md

The index page should be a listing of _recent_ posts.


### built with

- https://jinja.palletsprojects.com/
- https://github.com/executablebooks/markdown-it-py
- https://github.com/kevquirk/simple.css
