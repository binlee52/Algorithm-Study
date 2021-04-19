import heapq
import sys

input = sys.stdin.readline
# 도시의 개수(100,000) * 경로의 최대길이(100,000) = 1e12
INF = int(1e13)

# N : 지점, M : 경로, D : 체력 소모량, E : 성취감 획득량
N, M, D, E = map(int, input().split())

graph = [[] for _ in range(N+1)]
height = [None] + list(map(int, input().split()))

for _ in range(M):
    # a <=> b : n
    a, b, n = map(int, input().split())
    graph[a].append((n, b))     # (거리, 지점)
    graph[b].append((n, a))     # (거리, 지점)


def dijkstra(start):
    distance = [INF] * (N+1)
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))      # (거리, 도착지)
    while q:
        dist, now = heapq.heappop(q)
        # 최단거리로 이동한 것이 아니라면
        if distance[now] < dist:
            continue

        # now에서 연결된 지점들에 대하여
        # i[0] : 거리, i[1] : 도착지
        for i in graph[now]:
            cost = dist + i[0]
            # 기록된 도착지까지의 최단거리보다 이동거리가 짧아야 한다.
            # 도착지의 높이가 현재 높이보다 높아야한다.
            if cost < distance[i[1]] and height[now] < height[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))
    return distance


up_distance = dijkstra(1)
down_distance = dijkstra(N)

lst = []
# 거쳐가는 지점 2~N-1 까지
for i in range(2, N):
    # # 1과 N에서 모두 갈 수 있는 지점 i를 구한다.
    if up_distance[i] != INF and down_distance[i] != INF:
        lst.append(height[i] * E - (up_distance[i] + down_distance[i]) * D)

print(max(lst) if lst else "Impossible")