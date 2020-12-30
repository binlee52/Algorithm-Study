INF = int(1e9)

# 노드의 번호는 0 ~ n-1 : 총 n개
n = int(input())
m = int(input())

graph = [[INF] * n for _ in range(n)]
for a in range(n):
    for b in range(n):
        if a == b:
            # node의 번호가 0부터 시작하므로
            graph[a-1][b-1] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    # 노드의 번호가 0부터 시작하므로
    graph[a-1][b-1] = c


for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print("INF", end=' ')
        else:
            print(graph[i][j], end=' ')
    print()