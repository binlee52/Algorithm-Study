import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))     # 비용, 도착지
    graph[b].append((c, a))

distance = [INF] * (N+1)
distance[1] = 0

q = []
heapq.heappush(q, (0, 1))   # (비용, 도착지)

while q:
    dist, now = heapq.heappop(q)
    # now 까지 최단경로로 이동한 것이 아닌 경우
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[0]
        if cost < distance[i[1]]:
            distance[i[1]] = cost
            heapq.heappush(q, (cost, i[1]))

print(distance[N])
