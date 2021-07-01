import heapq
import sys

INF = int(1e15)
input = sys.stdin.readline

# N : 도시의 수, M : 도로의 수, K : 포장할 도로의 수
N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
src, dst = 1, N

for _ in range(M):
    # A, B : 도시, C : 연결 비용
    A, B, C = map(int, input().split())
    graph[A].append((C, B))
    graph[B].append((C, A))


def dijkstra():
    distance = [[INF] * (K+1) for _ in range(N + 1)]
    distance[src][0] = 0
    q = [(0, src, 0)]
    while q:
        dist, now, cnt = heapq.heappop(q)
        # dist가 now까지 이동하는 최소 거리가 아닐 때
        if distance[now][cnt] < dist:
            continue
        # i[0] : 비용, i[1] : 도시
        for i in graph[now]:
            cost = dist + i[0]
            # 도로를 포장하지 않을 때
            if cost < distance[i[1]][cnt]:
                distance[i[1]][cnt] = cost
                heapq.heappush(q, (cost, i[1], cnt))
            
            # 도로를 포장할 때
            if cnt < K and dist < distance[i[1]][cnt+1]:
                distance[i[1]][cnt+1] = dist
                heapq.heappush(q, (dist, i[1], cnt+1))

    return min(distance[dst])


print(dijkstra())
