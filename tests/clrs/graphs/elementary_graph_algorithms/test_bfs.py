# Third Party Library
import pytest

# Repository Library
from clrs.graphs.elementary_graph_algorithms.bfs import BFSGraph


def test_bfsgraph():
    num_vertices = 5
    graph = BFSGraph(num_vertices, False)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.bfs(0)
    graph.print_path(0, 3)
    with pytest.raises(SystemExit):
        graph.print_path(3, 4)
    for i in range(num_vertices):
        assert graph.vertices[i].c == 1
    assert graph.vertices[0].d == 0
    assert graph.vertices[1].d == 1
    assert graph.vertices[2].d == 2
    assert graph.vertices[3].d == 2
    assert graph.vertices[4].d == 1
    assert graph.adj_matrix == [
        [0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 0, 1],
        [1, 1, 0, 1, 0],
    ]
    num_vertices = 6
    graph = BFSGraph(num_vertices, True)
    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 1)
    graph.add_edge(4, 3)
    graph.add_edge(5, 5)
    graph.bfs(0)
    graph.print_path(0, 4)
    for i in range(num_vertices):
        if i in [2, 5]:
            assert graph.vertices[i].c == 0
        else:
            assert graph.vertices[i].c == 1
    assert graph.vertices[0].d == 0
    assert graph.vertices[1].d == 1
    assert graph.vertices[2].d == float("inf")
    assert graph.vertices[3].d == 1
    assert graph.vertices[4].d == 2
    assert graph.vertices[5].d == float("inf")
    assert graph.adj_matrix == [
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1],
    ]
    num_vertices = 8
    graph = BFSGraph(num_vertices, False)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 6)
    graph.add_edge(4, 5)
    graph.add_edge(6, 7)
    graph.bfs(0)
    graph.print_path(0, 5)
    for i in range(num_vertices):
        assert graph.vertices[i].c == 1
    assert graph.vertices[0].d == 0
    assert graph.vertices[1].d == 1
    assert graph.vertices[2].d == 1
    assert graph.vertices[3].d == 2
    assert graph.vertices[4].d == 2
    assert graph.vertices[5].d == 3
    assert graph.vertices[6].d == 2
    assert graph.vertices[7].d == 3
    assert graph.adj_matrix == [
        [0, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0],
    ]
