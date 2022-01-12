# Third Party Library
import pytest

# Repository Library
from clrs.graph_algorithms.elementary_graph_algorithms.bfs import BFS


def test_bfs():
    num_vertices = 5
    graph = BFS(num_vertices, False)
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
    graph = BFS(num_vertices, True)
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
    graph = BFS(num_vertices, False)
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
    num_vertices = 6
    graph = BFS(num_vertices, True)
    graph.add_edge(0, 3)
    graph.add_edge(0, 1)
    graph.add_edge(1, 4)
    graph.add_edge(3, 1)
    graph.add_edge(4, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(5, 5)
    graph.bfs(0)
    assert graph.edge_types == {
        (0, 1): "T",
        (0, 3): "T",
        (1, 4): "T",
        (3, 1): "B",
        (4, 3): "B",
    }
    num_vertices = 6
    graph = BFS(num_vertices, True)
    graph.add_edge(0, 3)
    graph.add_edge(0, 1)
    graph.add_edge(1, 4)
    graph.add_edge(3, 1)
    graph.add_edge(4, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(5, 5)
    graph.bfs(2)
    assert graph.edge_types == {
        (2, 5): "T",
        (2, 4): "T",
        (5, 5): "B",
        (4, 3): "T",
        (3, 1): "T",
        (1, 4): "B",
    }
    num_vertices = 5
    graph = BFS(num_vertices, False)
    graph.add_edge(0, 4)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.bfs(0)
    assert graph.edge_types == {
        (0, 1): "T",
        (0, 4): "T",
        (1, 4): "C",
        (1, 3): "T",
        (1, 2): "T",
        (4, 3): "T",
        (4, 1): "C",
        (3, 2): "C",
        (2, 3): "C",
    }
    num_vertices = 8
    graph = BFS(num_vertices, False)
    graph.add_edge(0, 2)
    graph.add_edge(0, 1)
    graph.add_edge(1, 4)
    graph.add_edge(1, 3)
    graph.add_edge(3, 4)
    graph.add_edge(3, 6)
    graph.add_edge(4, 6)
    graph.add_edge(4, 7)
    graph.add_edge(2, 5)
    graph.add_edge(6, 7)
    graph.bfs(0)
    assert graph.edge_types == {
        (0, 1): "T",
        (0, 2): "T",
        (1, 3): "T",
        (1, 4): "T",
        (2, 5): "T",
        (3, 6): "T",
        (3, 4): "C",
        (4, 7): "T",
        (4, 6): "T",
        (4, 3): "C",
        (6, 7): "C",
        (7, 6): "C",
    }
