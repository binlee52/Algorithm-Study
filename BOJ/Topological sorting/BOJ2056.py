import sys
from collections import deque

input = sys.stdin.readline

# n : 작업 수
n = int(input())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)      # 위상
time = [0] * (n+1)          # 각 작업만 하는데 소요되는 시간

for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]   # 해당 작업에 걸리는 시간
    
    # 선행관계에 있는 작업이 있다면
    if len(data) > 1:
        indegree[i] = data[1]
        for x in data[2:]:
            graph[x].append(i)

result = time.copy()       # 선수 작업을 포함하여 작업하는데 소요되는 시간


def topology_sort():
    q = deque([])
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for x in graph[now]:
            # result[x] : 현재까지 기록된 x의 선수작업 소요시간 + x 작업 소요시간
            # result[now] : 현재 진행 중인 작업에 대한 소요시간
            # time[x] : x 작업 소요시간
            result[x] = max(result[x], result[now] + time[x])

            indegree[x] -= 1
            if indegree[x] == 0:
                q.append(x)

    return max(result)


print(topology_sort())
