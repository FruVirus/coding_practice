# Repository Library
from clrs.selected_topics.string_matching.finite_automata import fa


def test_fa():
    t = "abababacaba"
    p = "ababaca"
    assert fa(t, p) == [2]
    t = "ACACACACAGA AGA ACACAGA ACACAGA GEEKS"
    p = "ACACAGA"
    assert fa(t, p) == [4, 16, 24]
