# Repository Library
from clrs.advanced_design_and_analysis_techniques.greedy_algorithms.huffman_codes import (  # noqa: E501
    huffman_solution,
)


def test_huffman_bottom_up():
    c = {"a": 45, "b": 13, "c": 12, "d": 16, "e": 9, "f": 75}
    assert huffman_solution(c) == {
        "a": [1, 0],
        "b": [1, 1, 1, 0],
        "c": [1, 1, 0, 1],
        "d": [1, 1, 1, 1],
        "e": [1, 1, 0, 0],
        "f": [0],
    }
