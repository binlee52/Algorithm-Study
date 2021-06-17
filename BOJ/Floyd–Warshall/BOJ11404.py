import sys

input = sys.stdin.readline
INF = int(1e7)

# 도시의 개수
N = int(input())
# 버스의 개수
M = int(input())

# 거리 초기화
graph = [[INF] * (N+1) for _ in range(N+1)]
for i in range(N+1):
    graph[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    # 경로가 여러가지일 수 있으므로
    graph[a][b] = min(graph[a][b], c)

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
