import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(graph, N, s):
    q = []
    distance = [INF] * (N+1)
    distance[s] = 0
    heapq.heappush(q, (0, s))
    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))

    distance = [d for d in distance[1:] if d != INF]
    # 감염 컴퓨터 개수, 걸리는 시간
    return len(distance), max(distance)


T = int(input())
for _ in range(T):
    # N : 컴퓨터 개수, D : 의존성 개수, C : 해킹당한 컴퓨터 번호
    N, D, C = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(D):
        # 컴퓨터 A가 컴퓨터 B에 의존,
        # 컴퓨터 B가 감염되면 S 초후에 A 감염
        A, B, S = map(int, input().split())
        graph[B].append((S, A))
    cnt, tm = dijkstra(graph, N, C)

    print(cnt, tm)
