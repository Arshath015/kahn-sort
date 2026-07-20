import pytest
from core.graph import Graph
from core.topological_sort import topological_sort

def test_topological_sort():
    graph = Graph(6)
    graph.add_edge(5, 2)
    graph.add_edge(5, 0)
    graph.add_edge(4, 0)
    graph.add_edge(4, 1)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)
    assert topological_sort(graph) == [5, 4, 2, 3, 1, 0]

def test_cyclic_graph():
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 0)
    with pytest.raises(ValueError):
        topological_sort(graph)