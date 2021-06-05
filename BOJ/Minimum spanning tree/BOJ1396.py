import sys
from collections import deque
import copy

INF = int(1e12)
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

result = 0

graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

graph.sort()
graph = deque(graph)

Q = int(input())
for _ in range(Q):
    tmp = 0
    q = copy.deepcopy(graph)
    parent = [i for i in range(n+1)]
    x, y = map(int, input().split())

    u = INF
    while q:
        c, a, b = q.popleft()

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)

        if find_parent(parent, x) == find_parent(parent, y):
            u = c
            break

    if u != INF:
        v = len([find_parent(parent, i) for i in parent if find_parent(parent, i) == find_parent(parent, x)])
        print(u, v)
    else:
        print(-1)