# Repository Library
from clrs.graph_algorithms.single_source_shortest_paths.dijkstra import Dijkstra


def test_dijkstra():
    num_vertices = 5
    graph = Dijkstra(num_vertices, True)
    graph.add_edge(0, 1, 10)
    graph.add_edge(0, 3, 5)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 2)
    graph.add_edge(2, 4, 4)
    graph.add_edge(3, 1, 3)
    graph.add_edge(3, 2, 9)
    graph.add_edge(3, 4, 2)
    graph.add_edge(4, 0, 7)
    graph.add_edge(4, 2, 6)
    assert graph.is_dag
    graph.dijkstra(0)
    for v in graph.vertices.values():
        if v.k == 0:
            assert v.d == 0 and v.p is None
        if v.k == 1:
            assert v.d == 8 and v.p.k == 3
        if v.k == 2:
            assert v.d == 9 and v.p.k == 1
        if v.k == 3:
            assert v.d == 5 and v.p.k == 0
        if v.k == 4:
            assert v.d == 7 and v.p.k == 3
