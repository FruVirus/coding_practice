# Third Party Library
import pytest

# Repository Library
from clrs.graph_algorithms.all_pairs_shortest_paths.floyd_warshall import FloydWarshall


def test_floyd_warshall():
    num_vertices = 5
    graph = FloydWarshall(num_vertices, True)
    graph.add_edge(0, 1, 3)
    graph.add_edge(0, 2, 8)
    graph.add_edge(0, 4, -4)
    graph.add_edge(1, 3, 1)
    graph.add_edge(1, 4, 7)
    graph.add_edge(2, 1, 4)
    graph.add_edge(3, 0, 2)
    graph.add_edge(3, 2, -5)
    graph.add_edge(4, 3, 6)
    assert graph.floyd_warshall() == [
        [0, 1, -3, 2, -4],
        [3, 0, -4, 1, -1],
        [7, 4, 0, 5, 3],
        [2, -1, -5, 0, -2],
        [8, 5, 1, 6, 0],
    ]
    num_vertices = 6
    graph = FloydWarshall(num_vertices, True)
    graph.add_edge(0, 4, -1)
    graph.add_edge(1, 0, 1)
    graph.add_edge(1, 3, 2)
    graph.add_edge(2, 1, 2)
    graph.add_edge(2, 5, -8)
    graph.add_edge(3, 0, -4)
    graph.add_edge(3, 4, 3)
    graph.add_edge(4, 1, 7)
    graph.add_edge(5, 1, 5)
    graph.add_edge(5, 2, 10)
    assert graph.floyd_warshall() == [
        [0, 6, float("inf"), 8, -1, float("inf")],
        [-2, 0, float("inf"), 2, -3, float("inf")],
        [-5, -3, 0, -1, -6, -8],
        [-4, 2, float("inf"), 0, -5, float("inf")],
        [5, 7, float("inf"), 9, 0, float("inf")],
        [3, 5, 10, 7, 2, 0],
    ]
    with pytest.raises(SystemExit):
        graph.print_path(0, 2)
    graph.print_path(0, 1)
