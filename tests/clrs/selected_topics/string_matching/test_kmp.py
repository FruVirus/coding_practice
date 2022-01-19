# Repository Library
from clrs.selected_topics.string_matching.kmp import kmp


def test_kmp():
    t = "ababcabcabababd"
    p = "ababd"
    assert kmp(t, p) == [10]
    t = "bacbababaabcbab"
    p = "ababaca"
    assert kmp(t, p) == []
    t = "bacbababaabcbab"
    p = "aba"
    assert kmp(t, p) == [4, 6]
    t = "2359023141526739921"
    p = "23"
    assert kmp(t, p) == [0, 5]
    t = "ababcabcaabcadaabeabababd"
    p = "aabcadaabe"
    assert kmp(t, p) == [8]
