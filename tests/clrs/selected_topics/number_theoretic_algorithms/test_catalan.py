# Repository Library
from clrs.selected_topics.number_theoretic_algorithms.catalan import catalan


def test_catalan():
    assert catalan(4) == 14
    assert catalan(5) == 42
