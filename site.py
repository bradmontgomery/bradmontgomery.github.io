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
import shutil
from glob import glob
from pathlib import Path
from time import time

import ez_yaml
import rich_click as click
from jinja2 import Environment, PackageLoader, select_autoescape
from markdown_it import MarkdownIt
from mdit_py_plugins.front_matter import front_matter_plugin


logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)


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
    # TODO: parse any Timestamp dates into datetime.datetime objects?
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


def build_index(env, output: str, index: list, top: int = 20):
    """Build an index page with the _latest_ `top` (20) articles."""
    # Each item's keys include: url, title, date, description.
    index = sorted(index, key=lambda d: d["date"], reverse=True)

    context = {
        "title": "Brad Montgomery",
        "subtitle": "Latest posts...",
        "posts": index[:top],
    }
    template = env.get_template("index.html")
    content = template.render(**context)
    with open(Path(output) / "index.html", "w") as f:
        f.write(content)
        logger.info("Wrote index.html")

    # Now do the same thing for /blog/index.html, but list everythign.
    context = {
        "title": "Brad Montgomery",
        "subtitle": "Brad's Blog. All of it.",
        "posts": index,
    }
    template = env.get_template("index.html")
    content = template.render(**context)
    with open(Path(output) / "blog/index.html", "w") as f:
        f.write(content)
        logger.info("Wrote blog/index.html")



# TODO: how to build a linked TAGS index?
def build_tags():
    pass


# TODO: how to build a linked ARCHIVES index?
def build_archives():
    pass



# -------------------------------------------------------------
# CLI Commands.
# -------------------------------------------------------------

@click.group()
def cli():
    pass

@cli.command()
@click.option("--output", default="docs", help="Output directory from which files are served")
@click.option("--addr", default="")
@click.option("--port", default=8000)
def server(output, addr, port):
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, request, client_address, server, directory=output):
            super().__init__(request, client_address, server, directory=output)

    httpd = http.server.HTTPServer((addr, port), Handler)
    logger.info("Listeng on %s:%S in %s...", addr, port, output)
    httpd.serve_forever()


@cli.command()
@click.option("-t", "--title", help="Article title")
@click.option("--tags", help="Article title")
def new(title, tags):
    # TODO: create a new post
    # TODO: fill in title, date, tags, etc.
    # TODO: construct md template and front-matter.
    raise NotImplementedError("Haven't gotten to this yet")


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

    # Build the index(es)
    build_index(env, output, index)

    # Build static files output
    build_static(output)

    elapsed = round(time() - start, 2)
    logger.info("Completed in %s seconds", elapsed)



if __name__ == "__main__":
    cli()
