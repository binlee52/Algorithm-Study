import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# N : 정점의 개수, E : 간선의 개수
N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    # a, b : 출발지/도착지, c: 거리
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

# 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호
v1, v2 = map(int, input().split())


# 최종 출발지 : 1번 정점, 도착지 : N번 정점
def dijkstra(start, end):
    # 이동거리 리스트
    distance = [INF] * (N+1)
    # 시작점 까지의 거리는 항상 0이다.
    distance[start] = 0
    q = []
    # (비용, 도착지)
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # i[0] : 비용, i[1] : 도착지
        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))
    return distance[end]


# 이동거리
path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)
answer = min(path1, path2)

print(answer if answer < INF else -1)
