import sys
from math import sqrt
INF = int(1e9)

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

data = []
# N : 별의 개수
N = int(input())
for _ in range(N):
    data.append(list(map(float, input().split())))

edges = []
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        d = sqrt((data[i][0]-data[j][0]) ** 2 + (data[i][1]-data[j][1]) **2)
        edges.append((d, (i, j)))

edges.sort(key=lambda i: i[0])

parent = [i for i in range(N)]
answer = 0
for cost, (a, b) in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += cost

print("{:.2f}".format(answer))
