#!/usr/bin/env python3
"""
Welp here we are. I built my own static site generator.
Like 10 years after this became *a thing*.

This one's pretty simple:

* Markdown (https://commonmark.org/) content goes in content/pages/ or content/blog/
* Templates are powered by Jinja2
* Run `python site.py build` to build it.
* See `python site.py --help` for more options.

There are some opinions.

"""
import http.server
import logging
import os
import re
import shutil
import string
import unicodedata
from collections import defaultdict
from glob import glob
from itertools import chain
from pathlib import Path
from time import time

import arrow
import ez_yaml
import rich_click as click
from feedgen.feed import FeedGenerator
from jinja2 import Environment, PackageLoader, select_autoescape
from markdown_it import MarkdownIt
from mdit_py_plugins.front_matter import front_matter_plugin

logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)


def to_slug(value):
    def _slugify(s):
        for c in s.lower().replace(" ", "-"):
            if c in string.ascii_lowercase + "-":
                yield c

    return "".join(list(_slugify(value)))


def find_markdown_files(parent: str) -> list:
    """Return a list of all .md files in the given parent directory"""
    files = list(glob(f"{parent}/**/*.md", recursive=True))
    logger.info("Found %s markdown files in %s", len(files), parent)
    return files


def parse_front_matter(tokens: list) -> dict:
    """Look for the *front-matter* tokens in the markdown file. Front
    matter is a blob of yaml at the top of the file. The following
    keys are *mostly* supported:

    - title: Title of the blog post or page
    - date: Published date (include timezone)
    - draft: true or false -> is it still draft?
    - tags: a list of content tags.
    - slug: a slugified url
    - url: the URL where this _should_ be posted
    - aliases: alternative urls where we want this to show up
    - description: A short description for the <meta> tags.
    - markup: may still exist, is not used. It's all markdown now.

    """
    tokens = [t for t in tokens if t.type == "front_matter"]
    if len(tokens) == 0:
        return {}

    # Assume we have one front-matter object.
    t = tokens[0]
    fm = dict(ez_yaml.to_object(t.content))

    try:
        # Parse dates from yaml TimeStamp into a datetime objects.
        dt = arrow.get(fm["date"]).to("utc").datetime
        fm["date"] = dt
    except Exception as err:
        logger.error("Failed to convert %s: %s", fm["date"], str(err))
    return fm


def get_template_context(filename):
    logger.info("Building context for %s", filename)
    content = Path(filename).read_text()
    md = MarkdownIt().use(front_matter_plugin).enable("table")
    context = parse_front_matter(md.parse(content))
    context["html_content"] = md.render(content)
    return context


def get_template_name(
    filename: str, content_dir: str, default: str = "page.html"
) -> str:
    """Figure out which .html template to use to render the given filename.

    This is typically a mapping of parent dir -> template name, e.g.:

    * blog/  -> blog.html
    * pages/ -> page.html

    """
    # mapping of content directories to template filenames used to render them.
    mappings = {
        "blog": "blog.html",
        "pages": "page.html",
    }
    parent = str(filename).strip(content_dir).split("/")[0]  # Strip off content/
    path = str(Path(mappings.get(parent, default)))
    return path


def get_output_paths(output_dir: str, context: dict, file: str) -> str:
    # If there's a URL or Aliases defined, use those.
    # Otherwise, use the filename (sans extension)
    urls = []
    if "url" in context:
        urls.append(context["url"].strip("/"))
    if "aliases" in context:
        urls += [u.strip("/") for u in context["aliases"]]

    if len(urls) == 0:
        urls = [Path(file).stem]

    results = []
    for url in urls:
        path = Path(output_dir) / Path(url)
        path.mkdir(parents=True, exist_ok=True)
        path = path / Path("index.html")
        results.append(str(path))
    return results


def build_static(output):
    """This just copies a few static files to the right place.

    Assumes: static files are in <project_root>/static/, and that
        output files go to <output>/static/
    """
    static_output = Path(output) / Path("static")
    logger.info("Building Static output in: %s", static_output)
    shutil.copytree(Path("static"), static_output, dirs_exist_ok=True)


def render(env, path, template, context):
    """Render a jinja template using the given path & context.

    - env: The jinja environment.
    - path: The path (excluding filename) to which content should be written.
    - template: The template to use (e.g. index.html)
    - context: Dictionary of context variables to use when rendering.

    """
    filename = "index.html" if template.endswith("html") else "index.md"
    template = env.get_template(template)
    content = template.render(**context)
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    path = path / Path(filename)
    with open(path, "w") as f:
        f.write(content)
        logger.info("Wrote %s", path)


def build_index(env, output: str, index: list, top: int = 20):
    """Build an index page with the _latest_ `top` (20) articles."""
    # Each item's keys include: url, title, date, description.
    index = sorted(index, key=lambda d: d["date"], reverse=True)

    context = {
        "title": "Brad Montgomery",
        "subtitle": "Latest posts...",
        "posts": index[:top],
    }
    render(env, Path(output), "index.html", context)

    # Now do the same thing for /blog/index.html, but list everythign.
    context = {
        "title": "Brad Montgomery",
        "subtitle": "Brad's Blog. All of it.",
        "posts": index,
    }
    render(env, Path(output) / Path("blog"), "index.html", context)


def build_date_archives(env, output: str, index: list):
    """Site indexing by year, month, day."""
    # Organize content by year/month/day
    articles = defaultdict(list)  # path: [article, ...]
    for post in index:
        pub_year = post["date"].strftime("%Y")
        pub_month = post["date"].strftime("%Y/%m")
        pub_day = post["date"].strftime("%Y/%m/%d")
        year_path = f"blog/{pub_year}"
        month_path = f"blog/{pub_month}"
        day_path = f"blog/{pub_day}"
        articles[year_path].append(post)
        articles[month_path].append(post)
        articles[day_path].append(post)

    for path, posts in articles.items():
        context = {
            "title": "Archive",
            "subtitle": "",
            "posts": posts,
        }
        render(env, f"{output}/{path}", "index.html", context)


def normalize_tag(value: str) -> str:
    """Borroed from Django's slugify function, this normalizes tags into
    a URL-save, and directory-save string."""
    value = (
        unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    )
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", value).strip("-_")


def build_tags(env, output: str, index: list) -> None:
    """Site indexing based on tags"""

    # /blog/tags/ -> list of all tags.
    tags = sorted(set(chain(*[post.get("tags") for post in index])))
    tags = [normalize_tag(tag) for tag in tags]
    context = {
        "title": "Brad Montgomery",
        "subtitle": "Tags",
        "tags": [(tag, f"/blog/tags/{tag}/") for tag in tags],
    }
    render(env, f"{output}/blog/tags/", "tags.html", context)

    # /blog/tag/<tagname>/ -> articles with a tag.
    by_tags = defaultdict(list)
    for post in index:
        for tag in post.get("tags"):
            tag = normalize_tag(tag)
            by_tags[tag].append(post)

    for tag, posts in by_tags.items():
        context = {
            "title": "Brad Montgomery",
            "subtitle": f"Tagged {tag}",
            "posts": posts,
        }
        render(env, f"{output}/blog/tags/{tag}", "index.html", context)


def build_feeds(output: str, index: list) -> None:
    """Build syndication feeds:

    1. RSS feed at /feed/rss/
    2. Atom feed at /feed/atom/

    """
    rss_path = Path(output) / Path("feed/rss/")
    rss_file = rss_path / Path("rss.xml")
    os.makedirs(rss_path, exist_ok=True)
    rss_file.touch(exist_ok=True)

    atom_path = Path(output) / Path("feed/atom/")
    atom_file = atom_path / Path("atom.xml")
    os.makedirs(atom_path, exist_ok=True)
    atom_file.touch(exist_ok=True)

    fg = FeedGenerator()
    fg.id("https://BradMontgomery.net")
    fg.title("BradMontgomery.net")
    fg.author({"name": "Brad Montgomery"})
    fg.link(href="https://bradmontgomery.net", rel="alternate")
    fg.subtitle("brad's blog")
    fg.language("en")

    items = sorted(
        [post for post in index if not post["draft"]], key=lambda p: p["date"]
    )
    for post in items:
        fe = fg.add_entry()
        fe.id("https://bradmontgomery.net" + post["url"])
        fe.author(name="Brad Montgomery")
        fe.title(post["title"])
        fe.link(href="https://bradmontgomery.net" + post["url"])
        fe.content(post["html_content"])
        fe.description(description=post.get("description"))
        fe.pubdate(post["date"])

    logger.info("Generating ATOM feed")
    fg.atom_file(atom_file)
    logger.info("Wrote ATOM feed to %s", atom_file)

    logger.info("Generating RSS feed")
    fg.rss_file(rss_file)
    logger.info("Wrote RSS feed to %s", rss_file)


def copy_texts(
    content: str,
    output: str,
) -> None:
    """
    Any .txt files located in /content/texts/ will just get
    copied to the root of the domain. E.g. this can be used
    for things like humans.txt or llms.txt.

    """
    src_path = Path(content) / Path("texts")
    dst_path = Path(output)
    for file in glob(f"{src_path}/*.txt"):
        logger.info("Copying %s to %s", file, dst_path)
        shutil.copyfile(file, str(dst_path / Path(file).name))


# -------------------------------------------------------------
# CLI Commands.
# -------------------------------------------------------------


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--output", default="docs", help="Output directory from which files are served"
)
@click.option("--addr", default="")
@click.option("--port", default=8000)
def server(output, addr, port):
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, request, client_address, server, directory=output):
            super().__init__(request, client_address, server, directory=output)

    httpd = http.server.HTTPServer((addr, port), Handler)
    logger.info("Listeng on %s:%s in %s...", addr, port, output)
    httpd.serve_forever()


@cli.command()
def new():
    # set up the jinja environment
    env = Environment(loader=PackageLoader("site"), autoescape=select_autoescape())

    # Prompt for content setup...
    prompts = [
        ("date", "Date (default is now): "),
        ("title", "Title: "),
        ("tags", "Tags (comma-separated): "),
        ("description", "Description: "),
        ("draft", "Draft (false): "),
    ]
    context = {}
    for key, prompt in prompts:
        context[key] = input(prompt)
        if key == "title":
            context["slug"] = to_slug(context[key])
        elif key == "date":
            context[key] = (
                arrow.utcnow().datetime
                if not context[key]
                else arrow.get(context[key]).datetime
            )
        elif key == "draft":
            context[key] = True if context[key] == "true" else False
        elif key == "tags":
            context[key] = [normalize_tag(tag) for tag in context[key].split(",")]

    context["url"] = f"/blog/{context['slug']}/"
    datestring = context["date"].strftime("%Y/%M/%d")
    context["alias"] = f"/blog/{datestring}/{context['slug']}/"
    render(env, f"content/blog/{context['slug']}", "content.md", context)


@cli.command()
@click.option("--content", default="content", help="Content directory")
@click.option("--templates", default="templates", help="Template directory")
@click.option("--output", default="docs", help="Output directory")
def build(content, templates, output):
    start = time()

    # set up the jinja environment
    env = Environment(loader=PackageLoader("site"), autoescape=select_autoescape())

    # List of context dicts for the index, blog list, and archive.
    index = []

    # get list of files, urls
    for file in find_markdown_files(content):
        context = get_template_context(file)
        template = env.get_template(get_template_name(file, content))
        html_content = template.render(**context)

        # Get output dir that we need to write to.
        for path in get_output_paths(output, context, file):
            with open(path, "w") as f:
                f.write(html_content)
                logger.info("Wrote: %s", path)

        # If a blog post, put it in the index.
        if file.strip(content).startswith("/blog"):
            index.append(context)

    # Build the index(es), tags list, archives, and feeds
    build_index(env, output, index)
    build_tags(env, output, index)
    build_date_archives(env, output, index)
    build_feeds(output, index)

    # Build static files output
    build_static(output)
    copy_texts(content, output)

    elapsed = round(time() - start, 2)
    logger.info("Completed in %s seconds", elapsed)


if __name__ == "__main__":
    cli()
