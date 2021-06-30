import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# N : 컴퓨터 개수, M : 회선 정보 개수
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))     # dist, now
    graph[B].append((C, A))

def dijkstra():
    start = 1
    distance = [INF] * (N+1)
    distance[start] = 0
    path = [0 for _ in range(N+1)]
    q = [(0, start)]    # dist, now
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                path[i[1]] = now
                heapq.heappush(q, (cost, i[1]))
    return path


path = dijkstra()
print(N-1)
for i in range(2, N+1):
    print(i, path[i])
