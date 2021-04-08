from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

q = deque([(0, 0)])
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q:
    x, y = q.popleft()
    # 도착했을 때
    if x == n-1 and y == m-1:
        break
    
    # 사방 탐색
    for step in range(4):
        nx = x + dx[step]
        ny = y + dy[step]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 0:
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))

print(graph[n-1][m-1])
