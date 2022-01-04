# Repository Library
from clrs.selected_topics.string_matching.rabin_karp import rabin_karp


def test_rabin_karp():
    assert rabin_karp("2359023141526739921", "31415") == [[0, 6]]
    assert rabin_karp("2359023141526739921", "31416", q=100) == []
    assert rabin_karp("2359023141526739921", "23") == [[0, 0], [0, 5]]
