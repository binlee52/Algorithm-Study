import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

# N : 마을, 학생 수, M : 단방향 도로
N, M, X = map(int, input().split())

graph1 = [[] for _ in range(N+1)]
graph2 = [[] for _ in range(N+1)]

for _ in range(M):
    # 출발지, 도착지, 비용
    a, b, c = map(int, input().split())
    # 출발지 -> X
    graph1[b].append((c, a))    # 소요시간, 도착지
    # X -> 도착지
    graph2[a].append((c, b))    # 소요시간, 도착지


def dijkstra(graph, start):
    distance = [INF] * (N+1)
    distance[start] = 0
    q = []
    # 비용, 도착지
    heapq.heappush(q, (0, X))

    while q:
        dist, now = heapq.heappop(q)
        # 최단거리가 아닐 때
        if distance[now] < dist:
            continue

        # graph2의 인접 노드들에 대해
        # i[0] : 비용, i[1] : 도착지
        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))
    return distance


result = [x + y for x, y in zip(dijkstra(graph1, X), dijkstra(graph2, X))][1:]
result = max(result)
print(result)

