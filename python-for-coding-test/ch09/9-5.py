import heapq as hq
import sys

INF = int(1e9)
input = sys.stdin.readline

# n(도시의 개수), m(통로의 개수), c(메세지를 보내는 도시)
n, m, c = map(int, input().split())

# c에서부터의 거리
d = [INF] * (n+1)
d[c] = 0

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))      # (목적지, 거리))

q = []      # 우선순위 큐
hq.heappush(q, (0, c))      # (거리, 목적지)
while q:
    dist, now = hq.heappop(q)   # 현재까지 거리, 현재 위치
    # 이미 방문한 적이 있으면
    if d[now] < dist:
        continue    # 아무것도 하지 않는다

    # current[0]: 목적지, current[1]: now에서 current[0] 까지 이동해야할 거리
    for current in graph[now]:
        cost = dist + current[1]
        # current[0]를 거쳐서 가는 경로가
        if cost < d[current[0]]:
            d[current[0]] = cost
            hq.heappush(q, (cost, current[0]))

result = [x for x in d if x != INF and x != 0]
print(len(result), max(result))