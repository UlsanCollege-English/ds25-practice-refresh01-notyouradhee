"""
Refresh-01 Practice Module
A tiny hello-world style script to test cloning, editing, committing, and pushing.

Run pytest in the repo root to verify everything works.
"""

from typing import Optional


def greet(name: Optional[str] = None) -> str:
    """
    Return a greeting string.

    Args:
        name: optional name to greet.

    Returns:
        str: A greeting like "Hello, world!" or "Hello, Alice!"
    """
    if not name:
        return "Hello, world!"
    return f"Hello, {name}!"
