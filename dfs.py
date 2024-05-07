nodes = {'0' : ['2','3'],
    '1' : ['0'],
    '2' : ['3','4'],
    '3' : [],
    '4' : []
}

visited = []
stack = []

def dfs (visited, nodes, node):
    visited.append(node)
    stack.append(node)
    iteration = 0

    while stack:
        popped_ele = stack.pop()
        print("Iteration", iteration)
        print('Currently Visited Nodes =',visited)

        for child in nodes[popped_ele]:
            if child not in visited:
                visited.append(child)
                stack.append(child)

                iteration +=1

dfs(visited, nodes, '1')

print()

for i in visited:
    print(i, end = " ")