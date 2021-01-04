# INF = int(1e9)
# # 전체 회사의 개수(n), 경로의 개수(m)
# n, m = map(int, input().split())
# graph = [[INF] * n for _ in range(n)]
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a-1][b-1] = 1
#     graph[b-1][a-1] = 1
#
# # 물건 판매 회사(x), 소개팅녀 회사(k)
# x, y = map(int, input().split())
#
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             graph[i][j] = 0
#
# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
#
# if graph[0][y-1] != INF and graph[y-1][x-1] != INF:
#     print(graph[0][y-1] + graph[y-1][x-1])
# else:
#     print(-1)

INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


if graph[1][k] != INF and graph[k][x] != INF:
    print(graph[1][k] + graph[k][x])
else:
    print(-1)
