# Repository Library
from clrs.graph_algorithms.single_source_shortest_paths.dag import DAG


def test_dag():
    num_vertices = 6
    graph = DAG(num_vertices, True)
    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 2, 3)
    graph.add_edge(1, 2, 2)
    graph.add_edge(1, 3, 6)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 4, 4)
    graph.add_edge(2, 5, 2)
    graph.add_edge(3, 4, -1)
    graph.add_edge(3, 5, 1)
    graph.add_edge(4, 5, -2)
    assert graph.is_dag
    graph.dag(1)
    for v in graph.vertices.values():
        if v.k == 0:
            assert v.d == float("inf") and v.p is None
        if v.k == 1:
            assert v.d == 0 and v.p is None
        if v.k == 2:
            assert v.d == 2 and v.p.k == 1
        if v.k == 3:
            assert v.d == 6 and v.p.k == 1
        if v.k == 4:
            assert v.d == 5 and v.p.k == 3
        if v.k == 5:
            assert v.d == 3 and v.p.k == 4
