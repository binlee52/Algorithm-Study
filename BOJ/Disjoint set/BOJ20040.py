import sys

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


input = sys.stdin.readline

# n : 점의 개수, M : 진행된 차례의 수
n, m = map(int, input().split())
parent = [i for i in range(n+1)]

cycle = (False, 0)
for i in range(m):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = (True, i+1)
        break
    else:
        union_parent(parent, a, b)

if cycle[0]:
    print(cycle[1])
else:
    print(0)
