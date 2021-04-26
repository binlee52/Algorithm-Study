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


# n : 행성의 개수
n = int(input())
planets = []

for i in range(n):
    x, y, z = map(int, input().split())
    planets.append((x, y, z, i))    # x, y, z 좌표, node 번호

edges = []

# 각 좌표를 기준으로 정렬
for k in range(3):
    planets.sort(key=lambda x: x[k])
    s = planets[0][-1]      # 시작 노드 번호
    for i in range(1, n):
        t = planets[i][-1]      # 도착 노드 번호
        cost = abs(planets[i][k] - planets[i-1][k])
        edges.append((cost, s, t))      # s에서 t까지 비용 cost가 든다
        s = t

edges.sort()

result = 0
parent = [i for i in range(n+1)]

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
