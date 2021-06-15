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

# N : 행성의 수
N = int(input())

parent = [i for i in range(N+1)]
edges = []

for i in range(N):
    # 비용 리스트
    data = list(map(int, input().split()))
    for j, cost in enumerate(data):
        # 1부터 시작하므로 인덱스에 1씩 더해준다
        edges.append((i+1, j+1, cost))

edges.sort(key=lambda i: i[2])      # cost를 기준으로 정렬

answer = 0
for a, b, c in edges:
    # 같을 때는 무시
    if a == b:
        continue
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += c
print(answer)
