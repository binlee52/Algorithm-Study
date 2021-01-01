from collections import deque
import sys

input = sys.stdin.readline
INF = int(1e9)
# 도시 개수(n), 도로의 개수(m), 거리 정보(k), 출발 도시의 번호(x)
n, m, k, x = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
visited[0] = True

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

q = deque([(x, 0)])
while q:
    now, distance = q.popleft()
    if not visited[now]:
        graph[x][now] = distance
        visited[now] = True
        if distance < 2:
            for i in range(1, n+1):
                if graph[now][i] == 1:
                    q.append((i, distance + 1))

result = []
flag = False
for i in range(1, n+1):
    if graph[x][i] == k:
        print(i)
        flag = True

if not flag:
    print(-1)