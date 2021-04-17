import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline
# v : 정점의 개수, e : 간선의 개수
v, e = map(int, input().split())
# k : 시작점
k = int(input())
# 간선 연결 정보
graph = [[] for _ in range(v+1)]
for _ in range(e):
    # a에서 b로 가는 가중치 c
    a, b, c = map(int, input().split())
    graph[a].append((c, b))     # 이동거리, 도착지 순서로 graph에 삽입

# 각 정점으로의 거리
distance = [INF] * (v+1)
distance[k] = 0
# 우선순위 큐
q = []
heapq.heappush(q, (0, k))

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    # now를 거쳐서 갈 수 있는 정점들에 대해

    for i in graph[now]:
        cost = dist + i[0]
        # now 를 걸쳐서 i[1] 로 가는 것이 distance 에 저장된 길이 보다 짧을 때
        if cost < distance[i[1]]:
            distance[i[1]] = cost
            heapq.heappush(q, (cost, i[1]))

for i in range(1, v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
