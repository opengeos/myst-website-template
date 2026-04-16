#!/usr/bin/env python3
"""Generate RSS and Atom feeds for blog posts.

Reads frontmatter from ``posts/*.md``, writes ``rss.xml`` and ``atom.xml`` to the
repository root, and (if a MyST build exists) copies them into ``_build/html/``.

Usage: python generate_rss.py
"""

from __future__ import annotations

import re
import shutil
from datetime import date as date_cls, datetime, time, timezone
from pathlib import Path

import yaml
from feedgen.feed import FeedGenerator

# TODO: Update these with your site details
SITE_URL = "https://example.com"
SITE_TITLE = "Jane Doe's Blog"
SITE_SUBTITLE = "Thoughts on data science, open-source software, and teaching."
AUTHOR = {"name": "Jane Doe", "email": "jane.doe@example.com"}
LANGUAGE = "en"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.DOTALL)
SUMMARY_CHARS = 500


def summarize(body: str) -> str:
    """Return a short plain-text summary of a Markdown post body.

    Strips the leading ``#`` heading, collapses whitespace, and truncates at
    roughly :data:`SUMMARY_CHARS` characters on a word boundary.
    """
    text = re.sub(r"^#\s.*$", "", body, count=1, flags=re.MULTILINE)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= SUMMARY_CHARS:
        return text
    cut = text[:SUMMARY_CHARS].rsplit(" ", 1)[0]
    return cut + "..."


def parse_post(path: Path) -> dict | None:
    """Parse a blog post's frontmatter and body.

    Args:
        path: Path to a Markdown file.

    Returns:
        Dict with ``title``, ``date``, ``slug``, ``description``, ``tags``,
        and ``content`` keys, or ``None`` if the file has no frontmatter or
        no ``date`` field.
    """
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    meta = yaml.safe_load(match.group(1)) or {}
    if "date" not in meta:
        return None
    date = meta["date"]
    if isinstance(date, str):
        date = datetime.fromisoformat(date)
    if isinstance(date, datetime):
        if date.tzinfo is None:
            date = date.replace(tzinfo=timezone.utc)
    elif isinstance(date, date_cls):
        date = datetime.combine(date, time.min, tzinfo=timezone.utc)
    return {
        "title": meta.get("title", path.stem),
        "date": date,
        "slug": f"posts/{path.stem}",
        "description": meta.get("description", ""),
        "tags": meta.get("tags", []) or [],
        "summary": summarize(match.group(2)),
    }


def build_feed(posts: list[dict]) -> FeedGenerator:
    """Build a FeedGenerator populated with the given posts.

    Args:
        posts: List of post dicts from :func:`parse_post`, sorted newest first.

    Returns:
        A configured ``FeedGenerator`` instance.
    """
    fg = FeedGenerator()
    fg.id(SITE_URL)
    fg.title(SITE_TITLE)
    fg.author(AUTHOR)
    fg.link(href=SITE_URL, rel="alternate")
    fg.link(href=f"{SITE_URL}/rss.xml", rel="self")
    fg.subtitle(SITE_SUBTITLE)
    fg.language(LANGUAGE)

    for post in posts:
        fe = fg.add_entry()
        url = f"{SITE_URL}/{post['slug']}"
        fe.id(url)
        fe.title(post["title"])
        fe.link(href=url)
        fe.author(AUTHOR)
        fe.published(post["date"])
        fe.updated(post["date"])
        fe.description(post["description"] or post["summary"])
        for tag in post["tags"]:
            fe.category({"term": str(tag)})
    return fg


def main() -> None:
    """Generate ``rss.xml`` and ``atom.xml`` from the ``posts/`` directory."""
    root = Path(__file__).parent
    blog_dir = root / "posts"
    posts = [p for p in (parse_post(f) for f in blog_dir.glob("*.md")) if p]
    posts.sort(key=lambda p: p["date"], reverse=True)

    if not posts:
        print("No blog posts found; skipping RSS generation.")
        return

    fg = build_feed(posts)
    rss_path = root / "rss.xml"
    atom_path = root / "atom.xml"
    fg.rss_file(str(rss_path), pretty=True)
    fg.atom_file(str(atom_path), pretty=True)
    print(f"Wrote {rss_path} and {atom_path} ({len(posts)} posts).")

    build_html = root / "_build" / "html"
    if build_html.exists():
        shutil.copy(rss_path, build_html / "rss.xml")
        shutil.copy(atom_path, build_html / "atom.xml")
        print(f"Copied feeds into {build_html}.")


if __name__ == "__main__":
    main()
