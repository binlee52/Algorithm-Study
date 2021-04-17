import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    # x, y : 출발지/도착지, z : 소요시간
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    graph[y].append((x, z))

distance = [INF] * (n+1)
distance[c] = 0
q = []
heapq.heappush(q, (0, c))

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        # now : 출발지, i[0] : 도착지, i[1] : 소요시간
        cost = dist + i[1]
        # 거쳐가는 것이 더 빠르다면 갱신
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

# 시작 노드는 제외
city = [x for x in distance if x != INF]
print(len(city) - 1, max(city))
