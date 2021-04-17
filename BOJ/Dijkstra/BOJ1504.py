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
distance_sv1 = [INF] * (N+1)
distance_sv2 = [INF] * (N+1)
distance_v1N = [INF] * (N+1)
distance_v2N = [INF] * (N+1)
distance_v1v2 = [INF] * (N+1)
distance_v2v1 = [INF] * (N+1)


def dijkstra(distance, start, end):
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


print(min(dijkstra(distance_sv1, 1, v1) + dijkstra(distance_v1v2, v1, v2) + dijkstra(distance_v2N, v2, N),
          dijkstra(distance_sv2, 1, v2) + dijkstra(distance_v2v1, v2, v1) + dijkstra(distance_v1N, v1, N)))
