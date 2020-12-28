from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7, 8],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * len(graph)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    visited[v] = True
    q = deque([v])
    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


dfs(graph, 1, visited)

# init
print()
visited = [False] * len(graph)

bfs(graph, 1, visited)