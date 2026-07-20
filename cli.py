import argparse
import sys
from core.graph import Graph
from core.topological_sort import topological_sort

def main():
    parser = argparse.ArgumentParser(description='Topological Sort via Kahn's Algorithm')
    parser.add_argument('--vertices', type=int, help='Number of vertices in the graph')
    parser.add_argument('--edges', nargs='+', help='Edges in the graph (u v)')
    args = parser.parse_args()
    graph = Graph(args.vertices)
    for edge in args.edges:
        graph.add_edge(*map(int, edge.split()))
    sorted_vertices = topological_sort(graph)
    print(' '.join(map(str, sorted_vertices)))

def run():
    try:
        main()
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(1)

def cli():
    run()
if __name__ == '__main__':
    cli()