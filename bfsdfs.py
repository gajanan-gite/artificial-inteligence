# DFS and BFS with user input

# 🔹 Take number of nodes
n = int(input("Enter number of nodes: "))

graph = {}

print("Enter neighbors for each node (space-separated):")
for i in range(1, n + 1):
    neighbours = list(map(int, input(f"Node {i}: ").split()))
    graph[i] = neighbours

# 🔹 DFS
visited = set()

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(neighbour)

# 🔹 BFS
def bfs(start):
    visited_bfs = set()
    queue = [start]

    while queue:
        node = queue.pop(0)

        if node not in visited_bfs:
            print(node, end=" ")
            visited_bfs.add(node)

            for neighbour in graph[node]:
                queue.append(neighbour)

# 🔹 Take start node
start = int(input("Enter starting node: "))

print("\nDFS traversal:")
dfs(start)

print("\nBFS traversal:")
bfs(start)