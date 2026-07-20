# Topological Sort via Kahn's Algorithm: Analysis

In this document, we provide an analysis of the time and space complexity of the topological sort algorithm implemented in this project.

## Time Complexity
The time complexity of the algorithm is O(V + E), where V is the number of vertices and E is the number of edges in the graph. This is because the algorithm visits each vertex and edge once during the construction of the adjacency list and the performance of the topological sort.

## Space Complexity
The space complexity of the algorithm is O(V + E), where V is the number of vertices and E is the number of edges in the graph. This is because the algorithm stores the adjacency list and the sorted list of vertices in memory.