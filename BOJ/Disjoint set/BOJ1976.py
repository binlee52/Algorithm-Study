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


N = int(input())
M = int(input())

parent = [i for i in range(N+1)]

for i in range(1, N+1):
    x = list(map(int, input().split()))
    for j, c in enumerate(x):
        if c:
            union_parent(parent, i, j+1)

x = list(map(int, input().split()))
x = set([find_parent(parent, i) for i in x])

if len(x) == 1:
    print("YES")
else:
    print("NO")
