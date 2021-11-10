# Repository Library
from clrs.graph_algorithms.minimum_spanning_trees.prim import MST


def test_prim():
    num_vertices = 9
    graph = MST(num_vertices)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 7, 8)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 7, 11)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 5, 4)
    graph.add_edge(2, 8, 2)
    graph.add_edge(3, 4, 9)
    graph.add_edge(3, 5, 14)
    graph.add_edge(4, 5, 10)
    graph.add_edge(5, 6, 2)
    graph.add_edge(6, 7, 1)
    graph.add_edge(6, 8, 6)
    graph.add_edge(7, 8, 7)
    mst = graph.prim()
    assert mst == {(2, 1), (6, 5), (4, 3), (7, 6), (1, 0), (8, 2), (3, 2), (5, 2)}
    assert len(mst) == num_vertices - 1
