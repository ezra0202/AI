import heapq

def dijkstra(graph, start):
    # Initialize distances with infinity for all vertices except the start vertex
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0  # Distance from start to itself is 0

    # Initialize priority queue with the start vertex
    priority_queue = [(0, start)]  # (distance, vertex)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip if we have already found a shorter path to the current vertex
        if current_distance > distances[current_vertex]:
            continue

        # Explore neighbors of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Update distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage:
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 3, 'B': 2, 'D': 4},
    'D': {'B': 1, 'C': 4}
}
start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)
print("Shortest distances from vertex", start_vertex + ":")
for vertex, distance in shortest_distances.items():
    print(vertex, "->", distance)


# Another Djkstra's from Itachi This is Easy

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    visited = set()

    while len(visited) < len(graph):
        current_node = None
        for node in graph:
            if node not in visited and (current_node is None or distances[node] < distances[current_node]):
                current_node = node

        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = distances[current_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return distances

graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'C': 3, 'D': 9},
    'C': {'A': 10, 'B': 3, 'D': 8},
    'D': {'B': 9, 'C': 8}
}

start_node = 'A'
distances = dijkstra(graph, start_node)
print("Shortest distances from", start_node, "to each node:", distances)