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


def cut(parent, x):
    parent[x] = x


# N : 정점의 개수, Q : 질의의 개수
N, Q = map(int, input().split())

parent = [i for i in range(N+1)]

for i in range(1, N):
    a = int(input())
    union_parent(parent, i+1, a)


for i in range(N-1+Q):
    a = list(map(int, input().split()))
    if len(a) == 2:
        x, b = a
        cut(parent, b)

    if len(a) == 3:
        x, c, d = a
        c = find_parent(parent, c)
        d = find_parent(parent, d)
        if c == d:
            print("YES")
        else:
            print("NO")