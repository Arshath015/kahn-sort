from collections import deque

def topological_sort(graph):
    queue = deque([i for i in range(graph.num_vertices) if graph.in_degree[i] == 0])
    sorted_vertices = []
    while queue:
        vertex = queue.popleft()
        sorted_vertices.append(vertex)
        for neighbor in graph.adj_list[vertex]:
            graph.in_degree[neighbor] -= 1
            if graph.in_degree[neighbor] == 0:
                queue.append(neighbor)
    if len(sorted_vertices) != graph.num_vertices:
        raise ValueError('Graph contains a cycle')
    return sorted_vertices