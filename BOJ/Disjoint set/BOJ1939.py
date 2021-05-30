def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent , a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
parent = [i for i in range(M+1)]
graph = []

for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append((C, A, B))

# 공장 입력 받기
x, y = map(int, input().split())

# 다리가 들 수 있는 중량이 큰 것부터 내림차순으로 정렬
graph.sort(key=lambda i: i[0], reverse=True)

for cost, a, b in graph:
    # 다리 연결
    union_parent(parent, a, b)
    # 두 공장이 연결 되었을 때
    if find_parent(parent, x) == find_parent(parent, y):
        # 현재 중량 출력
        print(cost)
        break
