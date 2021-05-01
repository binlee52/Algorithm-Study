import sys
from math import sqrt

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# N : 우주신들의 개수, M : 통로의 개수
N, M = map(int, input().split())
graph = []      # 정점 좌표
for _ in range(N):
    x, y = map(int, input().split())
    graph.append((x, y))

# 간선의 비용을 구한다
edges = []      # 간선 리스트
for i in range(len(graph) - 1):
    for j in range(i + 1, len(graph)):
        # 비용 구하기
        cost = sqrt((graph[i][0] - graph[j][0])**2 + (graph[i][1] - graph[j][1])**2)
        edges.append((cost, i+1, j+1))      # 간선 리스트에 추가, 정점은 1부터 시작

# 각 정점들의 부모
parent = [i for i in range(N+1)]

# 이미 연결되어있는 정점
for _ in range(M):
    x, y = map(int, input().split())
    union_parent(parent, x, y)

edges.sort()    # 비용에 따라 정렬

result = 0      # 총 비용
for edge in edges:
    cost, a, b = edge
    # 연결 되어있지 않으면
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)      # 연결
        result += cost      # 비용 계산

print("{:.2f}".format(result))
