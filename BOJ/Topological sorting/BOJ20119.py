import sys
from collections import deque

input = sys.stdin.readline
receipe = {}
# N : 물약의 종류, M : 레시피의 개수
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [-1] * (N+1)
visited = [False] * (N+1)

for _ in range(M):
    data = list(map(int, input().split()))
    K = data[0]     # 레시피 필요 물약 개수
    X = data[1:-1]  # 필요한 물약 정보
    R = data[-1]    # 만들 수 있는 물약
    for x in X:
        graph[x].append(R)
    indegree[R] = K

#  현재 클레어가 갖고 있는 물약 종류의 수
L = int(input())
# 갖고 있는 물약 종류
lst = list(map(int, input().split()))

q = deque(lst)

cnt = 0
while q:
    x = q.popleft()
    if visited[x]:
        continue
    cnt += 1
    visited[x] = True
    for i in graph[x]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

print(cnt)
for i in range(1, N+1):
    if visited[i]:
        print(i, end=" ")
