# Repository Library
from clrs.graph_algorithms.elementary_graph_algorithms.graph import Graph


def test_graph_connected_components():
    num_vertices = 10
    graph = Graph(num_vertices)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 1)
    graph.add_edge(4, 5)
    graph.add_edge(4, 6)
    graph.add_edge(7, 8)
    graph.add_edge(9, 9)
    graph.connected_components()
    assert graph.same_component(0, 1) is True
    assert graph.same_component(0, 2) is True
    assert graph.same_component(2, 1) is True
    assert graph.same_component(1, 3) is True
    assert graph.same_component(0, 4) is False
    assert graph.same_component(9, 9) is True
    assert graph.same_component(4, 9) is False


def test_graph_transitive_closure():
    num_vertices = 4
    graph = Graph(num_vertices, True)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 1)
    graph.add_edge(3, 2)
    graph.add_edge(3, 0)
    assert graph.transitive_closure() == [
        [1, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
    ]
    num_vertices = 6
    graph = Graph(num_vertices, True)
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
    assert graph.transitive_closure() == [
        [1, 1, 0, 1, 1, 0],
        [1, 1, 0, 1, 1, 0],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 0],
        [1, 1, 0, 1, 1, 0],
        [1, 1, 1, 1, 1, 1],
    ]


def test_graph_transpose():
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
    assert graph.deg(0, True) == 2
    assert graph.deg(0, False) == 0
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
