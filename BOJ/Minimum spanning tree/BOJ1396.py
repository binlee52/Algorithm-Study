import sys
from collections import deque

input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b




# n : 정점의 개수, m : 간선의 개수
n, m = map(int, input().split())

edges = []
result = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))     # 간선, 정점, 정점

# 간선 정렬
edges.sort()

parent = [i for i in range(n + 1)]
graph = [[] for _ in range(n + 1)]

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        graph[a].append((cost, b))  # 비용, 도착지
        graph[b].append((cost, a))

Q = int(input())

for _ in range(Q):
    x, y = map(int, input().split())
    u = 0      # 최소온도
    visited = [0] * (n + 1)     # 방문 여부 확인

    q = deque([(0, x)])    # 비용, 도착지
    while q:
        dist, now = q.popleft()

        # 방문한 적이 있으면
        if visited[now]:
            continue
        
        # 방문하기까지의 비용
        visited[now] = max(visited[now], dist)
        
        # y에 도착했을 시
        if now == y:
            u = dist

        # i[0] : 비용, i[1] : 도착지
        for i in graph[now]:
            cost = max(i[0], dist)
            q.append((cost, i[1]))

    # x에서 y까지 길이 존재할 때
    visited[x] = 1
    if u:
        v = 0
        for i in visited:
            if 0 < i <= u:
                v += 1
        print(u, v)
    else:
        print(-1)
