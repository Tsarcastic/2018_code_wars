"""."""
import pytest


def test_setup01():
    """Making sure the foundation is solid."""
    from parts_of_a_list import partlist
    the_input = ["this", "is", "annoying"]
    assert partlist(the_input) == [("this", "is annoying"), ("this is", "annoying")]