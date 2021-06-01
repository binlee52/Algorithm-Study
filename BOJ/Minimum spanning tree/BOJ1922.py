import sys
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


N = int(input())    # 컴퓨터의 수
M = int(input())    # 선의 수

parent = [i for i in range(N+1)]
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())     # a, b : 컴퓨터, c : 비용
    edges.append((c, a, b))

# 비용에 따라 정렬
edges.sort()

total_cost = 0
for cost, a, b in edges:
    # cycle 을 형성하지 않을 때
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += cost

print(total_cost)