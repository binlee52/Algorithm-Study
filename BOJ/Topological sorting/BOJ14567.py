import sys
from collections import deque

input = sys.stdin.readline

# N : 과목의 수, M : 선수 조건의 수
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

# 각 과목을 이수하는 학기
time = [1] * (N+1)
# 선이수 과목 개수 (위상)
indegree = [0] * (N+1)

for _ in range(M):
    # A번 과목이 B번 과목의 선수과목
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

q = deque([])

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

result = time.copy()

while q:
    now = q.popleft()
    for x in graph[now]:
        # result[x] : 지금까지 기록된 최대 이수 학기 수
        # time[x] : 해당 강의만 듣는 학기
        # result[now] : now까지 기록된 최대 이수 학기 수
        result[x] = max(result[x], time[x] + result[now])
        indegree[x] -= 1
        if indegree[x] == 0:
            q.append(x)

for r in result[1:]:
    print(r, end=" ")
