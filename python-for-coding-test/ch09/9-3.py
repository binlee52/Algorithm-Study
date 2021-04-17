import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수 및 간선의 개수 입력 받기
n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현)을 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n+1):
    graph[i][i] = 0


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c


# 점화식에 따라 플로이드 워셜 알고리즘 수행
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print('INF', end=' ')
        else:
            print(graph[i][j], end=' ')
    print()