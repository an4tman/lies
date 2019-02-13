#!/usr/bin/python3

import pytest

import val

@pytest.mark.parametrize("us, expected", [
    ("What is my name?", False),
    ("Foo is my name.", True),
])
def test_val_sentence(us, expected):
    """Test sentence validation."""
    assert val.validate_sentence(us) == expected


@pytest.mark.parametrize("us, expected", [
    ("A" * 141, False),
    ("A" * 140, True),
    ("A" * 139, True),
])
def test_val_length(us, expected):
    """Test length validation."""
    assert val.validate_length(us) == expected


@pytest.mark.parametrize("us, expected", [
    ("apple", True),
    ("bannana", False),
    ("asd;flkjasdk", False),
])
def test_val_english(us, expected):
    """Test English validation."""
    assert val.is_english_word(us) == expected
    
