class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]
        self.in_degree = [0] * num_vertices
    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.in_degree[v] += 1