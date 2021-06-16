import sys
import heapq

input = sys.stdin.readline
INF = int(1e10)

# N : 수빈 위치, K : 동생 위치
N, K = map(int, input().split())
MAX = int(1e5)+1
distance = [INF] * MAX

if N == K:
    print(0)
else:
    q = []
    heapq.heappush(q, (0, N))

    while q:
        cost, now = heapq.heappop(q)
        if distance[now] < cost:
            continue
        # if now == K:
        #     break
        if 0 <= now * 2 < MAX:
            if distance[now*2] > cost:
                distance[now*2] = cost
                heapq.heappush(q, (cost, now * 2))
        if 0 <= now + 1 < MAX:
            if distance[now+1] > cost + 1:
                distance[now+1] = cost + 1
                heapq.heappush(q, (cost+1, now+1))
        if 0 <= now - 1 < MAX:
            if distance[now-1] > cost + 1:
                distance[now-1] = cost + 1
                heapq.heappush(q, (cost+1, now-1))

    print(distance[K])