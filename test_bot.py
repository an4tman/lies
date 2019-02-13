"""
unit tests for the bot library
"""

import bot

class TestBot:

    def test_longest(self):
        assert "four score and seven years ago" == bot.longest("something", "something else", "four score and seven years ago")

    def test_shortest(self):
        assert "something" == bot.shortest("something", "something else", "four score and seven years ago")
