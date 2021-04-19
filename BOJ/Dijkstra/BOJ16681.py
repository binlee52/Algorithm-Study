import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# N : 지점, M : 경로, D : 체력 소모량, E : 성취감 획득량
N, M, D, E = map(int, input().split())

graph = [[] for _ in range(N+1)]
height = [1] + list(map(int, input().split()))

for _ in range(M):
    # a <=> b : n
    a, b, n = map(int, input().split())
    graph[a].append((n, b))     # (거리, 지점)
    graph[b].append((n, a))     # (거리, 지점)

# 올라갈 때 거리
up_distance = [INF] * (N+1)
up_distance[1] = 0     # start

# 내려갈 때 거리(N에서 올라갈 때 거리)
down_distance = [INF] * (N+1)
down_distance[N] = 0    # finish


def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, 1))      # (거리, 도착지)

    while q:
        dist, now = heapq.heappop(q)
        # 최단거리로 이동한 것이 아니라면
        if distance[now] < dist:
            continue

        # now에서 연결된 지점들에 대하여
        # i[0] : 거리, i[1] : 도착지
        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]] and height[now] < height[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))
# he - Dl

dijkstra(1, up_distance)
dijkstra(N, down_distance)

move = []
# 거쳐가는 지점 2~N-1 까지
for i in range(2, N):
    # 1과 N에서 모두 갈 수 있는 지점 i를 구한다.
    if INF not in (up_distance[i], down_distance[i]):
        move.append((up_distance[i] + down_distance[i], i))     # (이동거리, 거쳐가는 지점)
t = [(height[i[1]], i[1]) for i in move]
result = []
for a, b in zip(t, move):
    result.append((a[0]-2) * E - D * b[0])
print(result)

if result:
    print(max(result))
else:
    print("Impossible")














