import sys
from collections import deque

input = sys.stdin.readline

# T : 테스트 케이스의 개수
T = int(input())
# n : 팀의 수
for _ in range(T):
    N = int(input())
    # 우선순위
    indegree = [0] * (N+1)

    graph = [[] for _ in range(N+1)]
    data = [None] + list(map(int, input().split()))

    for i in range(1, N):
        for j in range(i+1, N+1):
            graph[data[i]].append(data[j])
            indegree[data[j]] += 1

    # M : 상대등수가 바뀐 것
    M = int(input())
    change = []
    for _ in range(M):
        a, b = map(int, input().split())
        if b in graph[a]:
            change.append((b, a))
        if a in graph[b]:
            change.append((a, b))

    for a, b in change:
        # a가 b보다 앞에 존재해야한다.
        
        # b -> a가 존재한다고 되어있을 때
        if a in graph[b]:
            graph[b].remove(a)
            indegree[a] -= 1
        # a -> b가 존재한다고 되어있지 않을 때
        if b not in graph[a]:
            graph[a].append(b)
            indegree[b] += 1

    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    result = []
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    if len(result) == N:
        for x in result:
            print(x, end=" ")
        print()
    else:
        print("IMPOSSIBLE")