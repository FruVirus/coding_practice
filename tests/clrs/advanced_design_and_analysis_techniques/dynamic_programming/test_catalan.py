# Repository Library
from clrs.advanced_design_and_analysis_techniques.dynamic_programming.catalan import (
    catalan,
)


def test_catalan():
    assert catalan(4, False) == ([1, 1, 2, 5, 14], 14)
    assert catalan(4, True) == ([1, 1, 2, 5, 14], 14)
    assert catalan(5, False) == ([1, 1, 2, 5, 14, 42], 42)
    assert catalan(5, True) == ([1, 1, 2, 5, 14, 42], 42)
