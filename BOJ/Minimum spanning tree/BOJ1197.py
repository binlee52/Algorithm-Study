import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent ,a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# v : 정점의 개수, e : 간선의 개수
v, e = map(int, input().split())

# init
edges = []
result = 0
parent = [i for i in range(v+1)]

for _ in range(e):
    # a, b : 정점, c : 가중치
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[-1])

for edge in edges:
    x, y, cost = edge
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += cost

print(result)
