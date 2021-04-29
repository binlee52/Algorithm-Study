import sys
from collections import deque

input = sys.stdin.readline

# n : 가수의 수, m : 보조 pd의 수
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)


for _ in range(m):
    data = list(map(int, input().split()))
    for a, b in zip(data[1:-1], data[2:]):
        graph[a].append(b)
        indegree[b] += 1

result = []
q = deque([])

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)
    for x in graph[now]:
        indegree[x] -= 1
        if indegree[x] == 0:
            q.append(x)


# 사이클이 발생했을 경우
if len(result) != n:
    print(0)
else:
    for x in result:
        print(x)
