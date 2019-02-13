#!/usr/bin/python3

"""
unit tests for the bot library
"""

import bot
import pytest

with open("test_data/true", "r") as true_fo:
    true_input = true_fo.readlines()
true_input = [i.strip() for i in true_input]

with open("test_data/false", "r") as false_fo:
    false_input = false_fo.readlines()
false_input = [i.strip() for i in false_input]

with open("test_data/misspelled", "r") as misspelled_fo:
    misspelled_input = misspelled_fo.readlines()
misspelled_input = [i.strip() for i in misspelled_input]

with open("test_data/evil", "r") as evil_fo:
    evil_input = evil_fo.readlines()
evil_input = [i.strip() for i in evil_input]

# print(true_input)
# print(false_input)

@pytest.mark.parametrize("us, expected", [
    ("What is my name?", False),
    ("Foo is my name.", True),
])
def test_val_sentence(us, expected):
    """Test sentence validation."""
    assert bot.validate_sentence(us) == expected


@pytest.mark.parametrize("us, expected", [
    ("A" * 141, False),
    ("A" * 140, True),
    ("A" * 139, True),
])
def test_val_length(us, expected):
    """Test length validation."""
    assert bot.validate_length(us) == expected
