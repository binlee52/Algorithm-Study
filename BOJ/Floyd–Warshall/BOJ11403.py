import sys

input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 모든 경유지에 대하여
for k in range(n):  # 경유지
    for i in range(n):  # 출발지
        for j in range(n):  # 도착지
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1


for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()
