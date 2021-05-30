from collections import deque
from copy import deepcopy

N = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

graph = []
for _ in range(N):
    graph.append(list(input()))

def inRange(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False


def bfs(sx, sy, key=False):
    q = deque([(sx, sy)])
    if key and graph[sx][sy] in ("R", "G"):
        color = ["R", "G"]
    else:
        color = [graph[sx][sy]]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if inRange(nx, ny) and graph[nx][ny] in color:
                graph[nx][ny] = 1
                q.append((nx, ny))


cnt = [0, 0]
init = deepcopy(graph)

for idx, flag in enumerate([False, True]):
    graph = deepcopy(init)
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 1:
                bfs(i, j, key=flag)
                cnt[idx] += 1

print(cnt[0], cnt[1])
