"""
MkDocs hook: give headings the same link names (anchors) that GitHub and
GitBook give them, so the in-page Table of Contents links in the book's
Markdown pages work on this site too.

Why it is needed
    GitHub keeps one hyphen for every space it removes from a heading, so
    "Using flag -s" becomes "using-flag--s". MkDocs normally squeezes
    repeated hyphens into one ("using-flag-s"), so TOC links written for
    GitHub did not jump anywhere here.

What it changes
    Only the anchor names of headings on this site. It does not change any
    file in 001-Python-book-2026, and it does not affect GitHub or GitBook.
"""
import re

_NOT_ALLOWED = re.compile(r'[^\w\- ]', re.UNICODE)


def github_slugify(value, separator='-'):
    """GitHub's rule: lower-case, drop punctuation, each space -> '-'."""
    value = value.strip().lower()
    value = _NOT_ALLOWED.sub('', value)
    return value.replace(' ', separator)


def on_config(config):
    config['mdx_configs'].setdefault('toc', {})['slugify'] = github_slugify
    return config

