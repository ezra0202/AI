graph = { '0' : ['1', '2'],
'1' : ['3','2'],
'2' : ['4'],
'3' : ['4'],
'4' : []
}

visited = []
queue = []

def bfs(visited, graph , node):
    visited.append(node)
    queue.append(node)
    iteration = 1

    while queue:
        popped_ele = queue.pop(0)
        print("Iteration", iteration)
        print('Currently Visited Nodes =',visited)

        for child in graph[popped_ele]:
            if child not in visited:
                visited.append(child)
                queue.append(child)

        iteration +=1

bfs(visited, graph, '0')

print()

for i in visited:
    print(i, end = " ")