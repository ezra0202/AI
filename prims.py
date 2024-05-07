import heapq

def prim(graph, start):
    visited = set()  # Set to keep track of visited vertices
    minimum_spanning_tree = []  # List to store the edges of the minimum spanning tree
    priority_queue = [(0, start, start)]  # Priority queue to keep track of candidate edges

    while priority_queue:
        weight, parent, vertex = heapq.heappop(priority_queue)

        if vertex not in visited:
            visited.add(vertex)
            if vertex != start:  # Skip adding the edge from the start vertex
                minimum_spanning_tree.append((parent, vertex, weight))

            # Add edges from the newly visited vertex to the priority queue
            for neighbor, edge_weight in graph[vertex].items():
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (edge_weight, vertex, neighbor))

    return minimum_spanning_tree

# Example usage:
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 3, 'B': 2, 'D': 4},
    'D': {'B': 1, 'C': 4}
}
start_vertex = 'A'
minimum_spanning_tree = prim(graph, start_vertex)
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge)


# Another Frm Itachi
INF = 9999999
V = 5
G = [[0, 19, 5, 0, 0],
     [19, 0, 5, 9, 2],
     [5, 5, 0, 1, 6],
     [0, 9, 1, 0, 1],
     [0, 2, 6, 1, 0]]

selected = [0, 0, 0, 0, 0]
no_edge = 0
selected[0] = True
print("Edge : Weight\n")
sumx = 0

while no_edge < V - 1:
    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if (not selected[j]) and G[i][j]:
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
    sumx += G[x][y]
    print(sumx)
    selected[y] = True
    no_edge += 1