def dijkstra(graph, n, start):
    dist = [float('inf')] * n
    visited = [False] * n

    dist[start] = 0

    for _ in range(n):
        # find minimum distance node
        min_dist = float('inf')
        u = -1
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        visited[u] = True

        # update neighbors
        for v in range(n):
            if graph[u][v] != 0 and not visited[v]:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]

    return dist


# 🔹 Input
n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix (0 if no edge):")

graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start = int(input("Enter source vertex: "))

# 🔹 Run
result = dijkstra(graph, n, start)

print("Shortest distances from source:")
for i in range(n):
    print(f"{start} -> {i} = {result[i]}")