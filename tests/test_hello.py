import pytest
from src.hello import greet


def test_default_greeting():
    assert greet() == "Hello, world!"


def test_custom_greeting():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"


def test_edge_cases():
    # Empty string should fall back to default
    assert greet("") == "Hello, world!"
    # Whitespace still counts as a name
    assert greet("   ") == "Hello,    !"  # preserve spaces literally
