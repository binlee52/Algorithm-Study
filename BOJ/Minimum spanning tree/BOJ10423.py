import sys

input = sys.stdin.readline

# N : 도시의 개수, M : 케이블의 수, K : 발전소의 개수
N, M, K = map(int, input().split())
# 발전소 (K 개)
station = list(map(int, input().split()))
parent = [i for i in range(N+1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    global station
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a in station:
        parent[b] = a
    elif b in station:
        parent[a] = b
        return
    elif a < b:
        parent[b] = a
    else:
        parent[a] = b


edges = []
for _ in range(M):
    # u, v: 도시, w : 비용
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort(key=lambda i: i[0])
answer = 0
for w, u, v in edges:
    # 이어진 발전소가 존재할 때
    if find_parent(parent, u) in station and find_parent(parent, v) in station:
        # 무시
        continue

    # 두 도시가 이어지지 않았을 때 (이어진 발전소가 같거나, 없을 때)
    if find_parent(parent, u) != find_parent(parent, v):
        # 연결
        union_parent(parent, u, v)
        answer += w

print(answer)
