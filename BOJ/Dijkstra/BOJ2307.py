import sys
import heapq

input = sys.stdin.readline
INF = int(1e12)

# n : 지점의 수, m : 도로의 수
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]


for _ in range(m):
    a, b, t = map(int, input().split())
    # cost, node
    graph[a].append((t, b))
    graph[b].append((t, a))


# v1 : 막을 간선의 출발지, v2 : 막을 간선의 도착지
def dijkstra(v1 = None, v2 = None):
    q = []
    heapq.heappush(q, (0, 1, "1"))       # (cost, node, path)

    # distance
    distance = [INF] * (n + 1)
    distance[1] = 0

    # road
    move = [""] * (n+1)
    move[1] = "1"

    while q:
        dist, now, route = heapq.heappop(q)
        if distance[now] < dist:
            continue

        # i[0] : cost, i[1] : node
        for i in graph[now]:
            cost = dist + i[0]
            path = route + "-" + str(i[1])
            if cost < distance[i[1]] and (now != v1 or i[1] != v2):
                distance[i[1]] = cost
                move[i[1]] = path
                heapq.heappush(q, (cost, i[1], path))

    return distance[n], move[n]


# 어떠한 도로도 막지 않았을 때 시간
fastest, move = dijkstra()
move = list(map(int, move.split('-')))

result = 0

# v1 : 막을 간선의 출발지, v2 : 막을 간선의 도착지
for v1, v2 in zip(move[:-1], move[1:]):
    result = max(result, dijkstra(v1, v2)[0])

if result == INF:
    print(-1)
else:
    print(result - fastest)
