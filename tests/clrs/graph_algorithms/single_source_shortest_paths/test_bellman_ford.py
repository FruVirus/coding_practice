# Repository Library
from clrs.graph_algorithms.single_source_shortest_paths.bellman_ford import BellmanFord


def test_bellman_ford():
    num_vertices = 5
    graph = BellmanFord(num_vertices, True)
    graph.add_edge(0, 1, 6)
    graph.add_edge(0, 3, 7)
    graph.add_edge(1, 2, 5)
    graph.add_edge(1, 3, 8)
    graph.add_edge(1, 4, -4)
    graph.add_edge(2, 1, -2)
    graph.add_edge(3, 2, -3)
    graph.add_edge(3, 4, 9)
    graph.add_edge(4, 0, 2)
    graph.add_edge(4, 2, 7)
    assert graph.bellman_ford(0) is True
    for v in graph.vertices.values():
        if v.k == 0:
            assert v.d == 0 and v.p is None
        if v.k == 1:
            assert v.d == 2 and v.p.k == 2
        if v.k == 2:
            assert v.d == 4 and v.p.k == 3
        if v.k == 3:
            assert v.d == 7 and v.p.k == 0
        if v.k == 4:
            assert v.d == -2 and v.p.k == 1
    num_vertices = 5
    graph = BellmanFord(num_vertices, True)
    graph.add_edge(0, 1, -6)
    graph.add_edge(0, 3, 7)
    graph.add_edge(1, 2, 5)
    graph.add_edge(1, 3, 8)
    graph.add_edge(1, 4, -4)
    graph.add_edge(2, 1, -2)
    graph.add_edge(3, 2, -3)
    graph.add_edge(3, 4, 9)
    graph.add_edge(4, 0, 2)
    graph.add_edge(4, 2, 7)
    assert graph.bellman_ford(0) is False
    num_vertices = 6
    graph = BellmanFord(num_vertices, True)
    graph.add_edge(0, 1, 6)
    graph.add_edge(0, 3, 7)
    graph.add_edge(1, 2, 5)
    graph.add_edge(1, 3, 8)
    graph.add_edge(1, 4, -4)
    graph.add_edge(2, 1, -2)
    graph.add_edge(3, 2, -3)
    graph.add_edge(3, 4, 9)
    graph.add_edge(4, 0, 2)
    graph.add_edge(4, 2, 7)
    graph.add_edge(5, 5, 7)
    graph.bellman_ford(0)
    assert graph.vertices[5].d == float("inf")
    assert graph.vertices[5].p is None
