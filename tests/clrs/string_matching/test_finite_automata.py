# Repository Library
from clrs.string_matching.finite_automata import fam


def test_fam():
    t = "abababacaba"
    p = "ababaca"
    assert fam(t, p) == [2]
    t = "ACACACACAGA AGA ACACAGA ACACAGA GEEKS"
    p = "ACACAGA"
    assert fam(t, p) == [4, 16, 24]
