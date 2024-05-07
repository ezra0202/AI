def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])
    closed_set = set()
    g = {}
    parents = {}
    g[start_node] = 0
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n == None:
            print('Path does not exist!')
            return None
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found: {}'.format(path))
            return path
        open_set.remove(n)
        closed_set.add(n)
    print('Path does not exist!')
    return None

def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

def heuristic(n):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0,
    }
    return H_dist[n]

Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1),('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
}

aStarAlgo('A', 'G')



#Another Implementation Froom GPT above is from Itachi
import heapq

def astar(graph, start, goal):
    open_list = [(0, start)]  # Priority queue of (f-score, node)
    came_from = {}  # Dictionary to reconstruct the path
    g_score = {node: float('inf') for node in graph}  # Cost from start to node
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}  # Estimated total cost from start to goal through node
    f_score[start] = heuristic(start, goal)

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for neighbor, cost in graph[current]:
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None  # No path found

def heuristic(node, goal):
    # Example heuristic: Euclidean distance between nodes
    x1, y1 = graph[node]
    x2, y2 = graph[goal]
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

graph = {
    'A': (0, 0),
    'B': (1, 2),
    'C': (3, 1),
    'D': (4, 3)
}

# Define edges and their costs
graph_edges = {
    'A': [('B', 10), ('C', 15)],
    'B': [('A', 10), ('D', 12)],
    'C': [('A', 15), ('D', 10)],
    'D': [('B', 12), ('C', 10)]
}

start_node = 'A'
goal_node = 'D'
path = astar(graph_edges, start_node, goal_node)
print("Path from", start_node, "to", goal_node, ":", path)
