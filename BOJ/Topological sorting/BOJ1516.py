import sys
from collections import deque

input = sys.stdin.readline

# 건물 종류의 수
N = int(input())

# i 건물을 짓고 지을 수 있는 건물의 리스트 graph[i]
graph = [[] for _ in range(N+1)]
# i 건물을 짓기 전에 지어야 하는 건물의 리스트 graph2[i]
graph2 = [[] for _ in range(N+1)]
indegree = [0] * (N+1)      # i 건물을 짓기 전에 지어야 하는 남은 건물
distance = [0] * (N+1)      # 비용

for i in range(1, N+1):
    data = list(map(int, input().split()))
    distance[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)
        graph2[i].append(x)

q = deque([])
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            # 이전에 짓는 건물들은 동시에 지을 수 있다는 것을 고려해야 함
            # i 건물을 짓기 위해서 지어야 할 건물들 중 가장 시간이 오래 걸리는 것
            # + 현재 건물을 짓는데 걸리는 시간
            distance[i] += max([distance[j] for j in graph2[i]])
            q.append(i)

for dist in distance[1:]:
    print(dist)