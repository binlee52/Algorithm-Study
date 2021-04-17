import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    # a : 출발지, b : 도착지, c : 비용
    a, b, c = map(int, input().split())
    graph[a].append((c, b))     # (비용, 도착지)

start, end = map(int, input().split())

distance = [INF] * (n+1)
distance[start] = 0

q = []
# 비용, 도착지
heapq.heappush(q, (0, start))

while q:
    dist, now = heapq.heappop(q)
    # now까지 최단 경로로 이동한 것이 아닐 때
    if distance[now] < dist:
        continue
    
    # now의 인접 노드들에 대하여
    for i in graph[now]:
        # i[0] : 비용, i[1] : 도착지
        cost = dist + i[0]
        if cost < distance[i[1]]:
            distance[i[1]] = cost
            heapq.heappush(q, (cost, i[1]))

print(distance[end])
