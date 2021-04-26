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


# n : 학교 수, m : 도로의 수
n, m = map(int, input().split())
parent = [i for i in range(n+1)]
sex = [None] + input().split()

edges = []

for _ in range(m):
    u, v, d = map(int, input().split())
    # 성별이 다를 때 edges에 추가
    if sex[u] != sex[v]:
        edges.append((d, u, v))     # 비용, 정점1, 정점2

edges.sort()

result = 0
for edge in edges:
    d, u, v = edge
    if find_parent(parent, u) != find_parent(parent, v):
        result += d
        union_parent(parent, u, v)

# parent만 추출 (인덱스 0 제외)
parent = set([find_parent(parent, i) for i in parent][1:])

if len(parent) != 1:
    print(-1)
else:
    print(result)
