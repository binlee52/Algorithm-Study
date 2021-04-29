import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# 정점 : n, 간선 : m
n, m = map(int, input().split())

# 인접 리스트
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # 가중치, 정점
    graph[a].append((c, b))
    graph[b].append((c, a))

s, t = map(int, input().split())

# Dijkstra
q = []
heapq.heappush(q, (0, s))     # cost, location

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue

    # i[0] : cost, i[1] : target
    for i in graph[now]:
        cost = dist + i[0]
        if cost < distance[i[1]]:
            distance[i[1]] = cost
            heapq.heappush(q, (cost, i[1]))

print(distance[t])