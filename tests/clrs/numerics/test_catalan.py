# Repository Library
from clrs.numerics.catalan import catalan


def test_catalan():
    assert catalan(4) == 14
    assert catalan(5) == 42
