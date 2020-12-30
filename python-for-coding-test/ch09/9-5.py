import heapq as hq

# 도시의 개수(n), 통로의 개수(m), 메시지를 보내고자 하는 도시(c)
n, m, c = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    # x : 출발, y: 도착, z: 거리
    graph[x].append((y, z))


def dijkstra(start):
    distance[start] = 0
    q = []
    # 거리, 출발 위치
    hq.heappush(q, (0, start))
    while q:
        dist, now = hq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                hq.heappush(q, (cost, i[0]))


dijkstra(c)
cnt, tm = 0, 0
for x in distance:
    if x != 0 and x != INF:
        cnt += 1
        tm = max(tm, x)

print(cnt, tm)
