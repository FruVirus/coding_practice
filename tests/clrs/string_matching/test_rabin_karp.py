# Repository Library
from clrs.string_matching.rabin_karp import rabin_karp


def test_rabin_karp():
    assert rabin_karp("2359023141526739921", "31415", 10) == [6]
    assert rabin_karp("2359023141526739921", "31416", 10, q=10) == []
    assert rabin_karp("2359023141526739921", "23", 10, q=17) == [0, 5]
