def graph_coloring(graph, n):
    result = [-1] * n  # Store color of each vertex
    result[0] = 0  # Assign the first color to the first vertex

    # Assign colors to remaining vertices
    for i in range(1, n):
        neighbour_colors = set(result[n] for n in graph[i])
        color = 0
        while color in neighbour_colors:
            color += 1
        result[i] = color

    # Print the result
    print("Vertex\tColor")
    for u in range(n):
        print(f"{u}\t{result[u]}")

    # Print the total number of colors used
    print("Minimum number of colors required:", max(result) + 1)


def main():
    num_edges = int(input("Enter the number of edges: "))
    print("Enter each edge as two space-separated integers (e.g., '0 1'):")

    edges = []
    max_vertex = -1

    for _ in range(num_edges):
        u, v = map(int, input().split())
        edges.append((u, v))
        max_vertex = max(max_vertex, u, v)

    n = max_vertex + 1  # Total number of vertices
    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Perform graph coloring
    graph_coloring(graph, n)


if __name__ == "__main__":
    main()
