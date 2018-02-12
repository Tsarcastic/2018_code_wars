"""Test dubstep.py"""

import pytest


def test_decoding01():
    """Making sure the foundation is solid."""
    from dubstep import song_decoder
    lyrics = "AWUBBWUBC"
    assert song_decoder(lyrics) == "A B C"


def test_decoding02():
    """A little more."""
    from dubstep import song_decoder
    lyrics = "AWUBWUBWUBBWUBWUBWUBC"
    assert song_decoder(lyrics) == "A B C"
