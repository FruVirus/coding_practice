# Repository Library
from clrs.string_matching.rabin_karp2d import rabin_karp2d


def test_rabin_karp2d():
    t = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    p = [["E", "F"], ["H", "I"]]
    assert rabin_karp2d(t, p, q=100) == [[1, 1]]
    t = [
        ["G", "H", "I", "P"],
        ["J", "K", "L", "Q"],
        ["R", "G", "H", "I"],
        ["S", "J", "K", "L"],
    ]
    p = [["G", "H", "I"], ["J", "K", "L"]]
    assert rabin_karp2d(t, p) == [[0, 0], [2, 1]]
    t = [
        ["E", "F", "C", "E", "F"],
        ["H", "I", "F", "H", "I"],
        ["E", "F", "I", "E", "F"],
        ["H", "I", "I", "H", "I"],
    ]
    p = [["E", "F"], ["H", "I"]]
    assert rabin_karp2d(t, p) == [[0, 0], [0, 3], [2, 0], [2, 3]]
