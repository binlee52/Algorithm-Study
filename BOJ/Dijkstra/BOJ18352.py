import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

# N : 도시의 개수, M : 도로의 개수, K : 거리 정보, X : 출발 도시의 번호
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    # a번 도시 => b번 도시
    a, b = map(int, input().split())
    graph[a].append(b)

# X로부터 목적지까지 거리
distance = [INF] * (N+1)
distance[X] = 0     # 출발도시까지 이동거리는 0

q = []
heapq.heappush(q, (0, X))   # (이동거리, 도착지)

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    # i[0] : 이동거리, i[1] : 도착지
    for i in graph[now]:
        cost = dist + 1
        if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(q, (cost, i))

flag = False
for idx, d in enumerate(distance):
    if d == K:
        flag = True
        print(idx)

if not flag:
    print(-1)
