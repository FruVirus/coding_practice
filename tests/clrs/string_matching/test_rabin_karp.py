# Repository Library
from clrs.string_matching.rabin_karp import rabin_karp


def test_rabin_karp():
    assert rabin_karp("2359023141526739921", "31415", 10) == 1
    assert rabin_karp("2359023141526739921", "31416", 10, q=10) == 0
    assert rabin_karp("2359023141526739921", "23", 10, q=17) == 2
