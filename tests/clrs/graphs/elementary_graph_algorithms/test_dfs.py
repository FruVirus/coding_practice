# Repository Library
from clrs.graphs.elementary_graph_algorithms.dfs import DFSGraph


def test_dfsgraph():
    num_vertices = 6
    graph = DFSGraph(num_vertices, True)
    graph.add_edge(0, 3)
    graph.add_edge(0, 1)
    graph.add_edge(1, 4)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 1)
    graph.add_edge(4, 3)
    graph.add_edge(5, 5)
    graph.dfs(recurse=True)
    graph.print_path(0, 4)
    for i in range(num_vertices):
        assert graph.vertices[i].c == 2
    assert graph.vertices[0].d == 1
    assert graph.vertices[0].f == 8
    assert graph.vertices[1].d == 2
    assert graph.vertices[1].f == 7
    assert graph.vertices[2].d == 9
    assert graph.vertices[2].f == 12
    assert graph.vertices[3].d == 4
    assert graph.vertices[3].f == 5
    assert graph.vertices[4].d == 3
    assert graph.vertices[4].f == 6
    assert graph.vertices[5].d == 10
    assert graph.vertices[5].f == 11
    graph.top_sort(recurse=True)
    assert not graph.is_dag
    num_vertices = 6
    graph = DFSGraph(num_vertices, True)
    graph.add_edge(0, 3)
    graph.add_edge(0, 1)
    graph.add_edge(1, 4)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(4, 3)
    graph.dfs(recurse=True)
    graph.top_sort(recurse=True)
    assert graph.is_dag
    num_vertices = 6
    graph = DFSGraph(num_vertices, True)
    graph.add_edge(0, 3)
    graph.add_edge(0, 1)
    graph.add_edge(1, 4)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(4, 3)
    graph.top_sort(recurse=True)
    top_sort = []
    node = graph.top_sort_ll.head
    while node is not None:
        top_sort.append(node.k)
        node = node.next
    assert top_sort == [2, 5, 0, 1, 4, 3]
    num_vertices = 6
    graph = DFSGraph(num_vertices, True)
    graph.add_edge(0, 3)
    graph.add_edge(0, 1)
    graph.add_edge(1, 4)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 1)
    graph.add_edge(4, 3)
    graph.add_edge(5, 5)
    graph.dfs()
    graph.print_path(0, 4)
    for i in range(num_vertices):
        assert graph.vertices[i].c == 2
    assert graph.vertices[0].d == 1
    assert graph.vertices[0].f == 8
    assert graph.vertices[0].d == 1
    assert graph.vertices[0].f == 8
    assert graph.vertices[1].d == 2
    assert graph.vertices[1].f == 7
    assert graph.vertices[2].d == 9
    assert graph.vertices[2].f == 12
    assert graph.vertices[3].d == 4
    assert graph.vertices[3].f == 5
    assert graph.vertices[4].d == 3
    assert graph.vertices[4].f == 6
    assert graph.vertices[5].d == 10
    assert graph.vertices[5].f == 11
    graph.top_sort()
    assert not graph.is_dag
    num_vertices = 6
    graph = DFSGraph(num_vertices, True)
    graph.add_edge(0, 3)
    graph.add_edge(0, 1)
    graph.add_edge(1, 4)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(4, 3)
    graph.dfs()
    graph.top_sort()
    assert graph.is_dag
    num_vertices = 6
    graph = DFSGraph(num_vertices, True)
    graph.add_edge(0, 3)
    graph.add_edge(0, 1)
    graph.add_edge(1, 4)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(4, 3)
    graph.top_sort()
    top_sort = []
    node = graph.top_sort_ll.head
    while node is not None:
        top_sort.append(node.k)
        node = node.next
    assert top_sort == [2, 5, 0, 1, 4, 3]
    num_vertices = 8
    graph = DFSGraph(num_vertices, True)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(1, 5)
    graph.add_edge(2, 3)
    graph.add_edge(2, 6)
    graph.add_edge(3, 2)
    graph.add_edge(3, 7)
    graph.add_edge(4, 0)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.add_edge(6, 5)
    graph.add_edge(6, 7)
    graph.add_edge(7, 7)
    graph.scc()
    assert graph.scc_list == [0, 2, 5, 7]
