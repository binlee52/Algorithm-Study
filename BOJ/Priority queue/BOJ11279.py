import heapq
import sys

input = sys.stdin.readline
q = []
N = int(input())
for _ in range(N):
    X = int(input())
    if X:
        heapq.heappush(q, -X)
    else:
        if q:
            print(-heapq.heappop(q))
        else:
            print(0)