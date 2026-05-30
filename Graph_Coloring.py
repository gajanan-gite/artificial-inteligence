# Graph Coloring

G = [
    [0, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 0]
]

node = "abcdef"

# Map node to index
t_ = {}
for i in range(len(G)):
    t_[node[i]] = i

# Count degree of all nodes
degree = []
for i in range(len(G)):
    degree.append(sum(G[i]))

# Assign available colors
colorDict = {}
for i in range(len(G)):
    colorDict[node[i]] = ["Blue", "Red", "Yellow", "Green"]

sortedNode = []
indeks = []

# Sort nodes based on degree (selection sort logic)
for i in range(len(degree)):
    _max = -1
    idx = -1
    for j in range(len(degree)):
        if j not in indeks:
            if degree[j] > _max:
                _max = degree[j]
                idx = j
    indeks.append(idx)
    sortedNode.append(node[idx])

# Main coloring process
theSolution = {}

for n in sortedNode:
    setTheColor = colorDict[n]
    theSolution[n] = setTheColor[0]

    adjacentNode = G[t_[n]]

    for j in range(len(adjacentNode)):
        if adjacentNode[j] == 1:
            if setTheColor[0] in colorDict[node[j]]:
                colorDict[node[j]].remove(setTheColor[0])

# Print solution
for t, w in sorted(theSolution.items()):
    print("Node", t, "=", w)