# Repository Library
from clrs.graphs.elementary_graph_algorithms.graph import Graph


def test_graph_tranpose():
    num_vertices = 6
    graph = Graph(num_vertices, True)
    graph.add_edge(0, 3)
    graph.add_edge(0, 1)
    graph.add_edge(1, 4)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 1)
    graph.add_edge(4, 3)
    graph.add_edge(5, 5)
    graph.transpose()
    adj_list_transpose = graph.adj_list_transpose
    all_edges = []
    for i in range(num_vertices):
        foo = adj_list_transpose[i].head
        while foo is not None:
            all_edges.append(foo.k)
            foo = foo.next
    assert all_edges == [3, 0, 4, 0, 2, 1, 5, 2]
    assert graph.adj_matrix_transpose == [
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 1],
    ]
