# Task 1: BFS and DFS

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Breadth First Search (BFS)
print("BFS Traversal:")
queue = ['A']

while queue:
    node = queue.pop(0)
    print(node, end=" ")
    queue = queue + graph[node]

print()

# Depth First Search (DFS)
print("DFS Traversal:")
stack = ['A']

while stack:
    node = stack.pop()
    print(node, end=" ")
    stack = stack + graph[node]

print()
