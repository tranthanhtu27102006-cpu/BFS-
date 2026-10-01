import collections

def bfs(graph,root):
    visited = {root}
    order = []
    queue = collections.deque([root])

    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for i in graph[vertex]:
            if i not in visited:
                visited.add(i)
                queue.append(i)
    print(order)

if __name__ == "__main__":
    graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B']
}
    print("Ngu Ngok Qua")
    bfs(graph,'A')


    