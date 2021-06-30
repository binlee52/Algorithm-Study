import sys

INF = int(1e9)
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


# N : 논의 수
N = int(input())
data = []

# 가상의 노드 0과 연결되어있고, 그 비용은 cst라고 가정
for i in range(1, N+1):
    cst = int(input())
    data.append((0, i, cst))

for i in range(1, N+1):
    arr = list(map(int, input().split()))
    for idx, c in enumerate(arr):
        if i != idx + 1:
            # src, dst, cost
            data.append((i, idx+1, c))

data.sort(key=lambda i: i[2])
parent = [i for i in range(N + 1)]

answer = 0

# 모든 노드들은 가상의 노드 0과 연결되어 있어야 함.
for src, dst, cst in data:
    if find_parent(parent, src) != find_parent(parent, dst):
        union_parent(parent, src, dst)
        answer += cst

print(answer)












