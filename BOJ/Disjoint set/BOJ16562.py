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


# N : 학생수, M : 친구관계 수, K : 돈
N, M, K = map(int, input().split())

# 최소의 가격으로 모든 사람과 친구과 되기 위해 친구 비용에 따라 정렬
payment = list(map(int, input().split()))
payment = [(i+1, j) for i, j in enumerate(payment)]
payment.sort(key=lambda i: i[1])

# 연결되어있는 노드 확인
parent = [i for i in range(N+1)]

# 친구 정보 읽기
for _ in range(M):
    a, b = map(int, input().split())
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)

total = 0   # 친구비용의 합
user = 0    # 준석

for i, cost in payment:
    # 친구가 아니라면
    if user != find_parent(parent, i):
        union_parent(parent, user, i)
        total += cost

# 예산 초과
if total > K:
    print("Oh no")
else:
    print(total)
