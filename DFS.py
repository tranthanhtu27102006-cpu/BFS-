graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B']
}

def dfs(graph,vertex,visited = None,order = None):
    if visited is None:
        visited = set()
        order = []

    visited.add(vertex)
    order.append(vertex)

    for i in graph[vertex]:
        if i not in visited:
            dfs(graph,i,visited,order)

    return order

print(dfs(graph, 'A')) 