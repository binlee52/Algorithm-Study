import sys
from collections import deque
input = sys.stdin.readline


# N : 부품 번호
N = int(input())
# M : 완제품 번호
M = int(input())

graph = [[] for _ in range(N+1)]
# 부품을 만드는데 필요한 선행 부품 종류의 개수
indegree = [0] * (N+1)

for _ in range(M):
    # X를 만드는데 Y 부품 K개가 필요
    X, Y, K = map(int, input().split())
    indegree[X] += 1
    graph[Y].append((X, K))     # 부품 Y가 부품 X에 K개 들어감

q = deque([])
base = []
for i in range(1, N+1):
    if indegree[i] == 0:
        # 부품 i는 기본 부품이다.
        q.append(i)
        base.append(i)

base = set(base)    # 빠른 탐색을 위해 set 로 변환
# 각 부품 당 필요한 기본 부품의 개수
total = [[0] * (N+1) for _ in range(N+1)]

while q:
    now = q.popleft()
    for x, k in graph[now]:
        indegree[x] -= 1
        # 기본 부품일 때
        if now in base:
            total[x][now] += k
        # 중간 부품일 때
        else:
            for idx, n in enumerate(total[now]):
                total[x][idx] += n * k

        if indegree[x] == 0:
            q.append(x)

for i, cnt in enumerate(total[N]):
    if cnt != 0:
        print(i, cnt)