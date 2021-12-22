# Repository Library
from clrs.graph_algorithms.elementary_graph_algorithms.dfs import DFS


def test_dfs():
    num_vertices = 6
    graph = DFS(num_vertices, True)
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
    graph = DFS(num_vertices, True)
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
    graph = DFS(num_vertices, True)
    graph.add_edge(0, 3)
    graph.add_edge(0, 1)
    graph.add_edge(1, 4)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(4, 3)
    top_sort = []
    node = graph.top_sort(recurse=True).head
    while node is not None:
        top_sort.append(node.k)
        node = node.next
    assert top_sort == [2, 5, 0, 1, 4, 3]
    num_vertices = 6
    graph = DFS(num_vertices, True)
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
    graph = DFS(num_vertices, True)
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
    graph = DFS(num_vertices, True)
    graph.add_edge(0, 3)
    graph.add_edge(0, 1)
    graph.add_edge(1, 4)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(4, 3)
    top_sort = []
    node = graph.top_sort().head
    while node is not None:
        top_sort.append(node.k)
        node = node.next
    assert top_sort == [2, 5, 0, 1, 4, 3]
    num_vertices = 8
    graph = DFS(num_vertices, True)
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
    assert graph.scc() == [0, 2, 5, 7]
    num_vertices = 8
    graph = DFS(num_vertices, True)
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
    assert graph.scc(recurse=True) == [0, 2, 5, 7]
    num_vertices = 7
    graph = DFS(num_vertices, True)
    graph.add_edge(0, 6)
    graph.add_edge(0, 1)
    graph.add_edge(3, 4)
    graph.add_edge(3, 5)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(2, 0)
    graph.add_edge(2, 5)
    graph.add_edge(6, 2)
    assert graph.get_edge_types() == {
        (0, 1): "Tree/Forward",
        (6, 2): "Cross",
        (1, 2): "Tree/Forward",
        (3, 4): "Tree/Forward",
        (2, 0): "Back",
        (0, 6): "Tree/Forward",
        (2, 3): "Tree/Forward",
        (2, 5): "Tree/Forward",
        (3, 5): "Cross",
    }
    num_vertices = 7
    graph = DFS(num_vertices, False)
    graph.add_edge(0, 6)
    graph.add_edge(0, 1)
    graph.add_edge(3, 4)
    graph.add_edge(3, 5)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(2, 0)
    graph.add_edge(2, 5)
    graph.add_edge(6, 2)
    assert graph.get_edge_types() == {
        (0, 1): "Tree/Forward",
        (6, 2): "Back",
        (1, 2): "Back",
        (3, 4): "Tree/Forward",
        (2, 0): "Back",
        (0, 6): "Tree/Forward",
        (2, 3): "Tree/Forward",
        (2, 5): "Tree/Forward",
        (3, 5): "Back",
    }
