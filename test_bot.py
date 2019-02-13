#!/usr/bin/python3

"""
unit tests for the bot library
"""

import pytest

import bot


@pytest.mark.parametrize("strategy, l, expected", [
    (bot.longest, ["something", "something else", "four score and seven years ago"], "four score and seven years ago"),
    (bot.shortest, ["something", "something else", "four score and seven years ago"], "something"),
])
def test_strat(strategy, l, expected):
    """Test that the bot selects the shortest input string."""
    assert strategy(*l) == expected

