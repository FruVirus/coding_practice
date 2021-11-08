# Repository Library
from clrs.graphs.mst.kruskal import MST


def test_kruskal():
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
    mst = graph.kruskal()
    assert mst == {(0, 1), (0, 7), (3, 4), (2, 3), (6, 7), (5, 6), (2, 5), (2, 8)}
    assert len(mst) == num_vertices - 1
