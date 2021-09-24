# Repository Library
from clrs.string_matching.naive import naive


def test_naive():
    t = "acaabc"
    p = "aab"
    assert naive(t, p) == [2]
    p = "xyz"
    assert naive(t, p) == []
