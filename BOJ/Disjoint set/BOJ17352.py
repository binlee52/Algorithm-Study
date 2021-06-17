import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b =find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 섬의 개수
N = int(input())
parent = [i for i in range(N+1)]
for _ in range(N-2):
    a, b = map(int, input().split())
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)


# 최상위 노드(root 노드만 출력)
parent = [find_parent(parent, x) for x in parent]
for x in set(parent[1:]):
    print(x, end=" ")
