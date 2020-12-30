INF = int(1e9)
# 전체 회사의 개수(n), 경로의 개수(m)
n, m = map(int, input().split())
graph = [[INF] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

# 물건 판매 회사(x), 소개팅녀 회사(k)
x, y = map(int, input().split())

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

if graph[0][y-1] != INF and graph[y-1][x-1] != INF:
    print(graph[0][y-1] + graph[y-1][x-1])
else:
    print(-1)
