import heapq
import sys

input = sys.stdin.readline
N = int(input())
q = []
for _ in range(N):
    heapq.heappush(q, int(input()))

answer = 0
while True:
    x = heapq.heappop(q)
    if not q:
        break
    y = heapq.heappop(q)
    answer += (x+y)
    heapq.heappush(q, (x+y))

print(answer)
