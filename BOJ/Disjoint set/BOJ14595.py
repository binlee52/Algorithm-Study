import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x, y):
    # 맨 앞 방의 속한 그룹을 알아낸다.
    a = find_parent(parent, x)
    # 맨 뒤부터 차례대로 앞까지 그룹을 변경한다.
    for i in range(y, x, -1):
        # 이미 같은 그룹이거나, 그룹 번호가 맨 앞 방의 그룹 번호보다 작은 방이 나오면 종료
        if parent[i] <= a:
            return
        parent[i] = a


# N : 동아리 방의 개수
N = int(input())

parent = [i for i in range(N+1)]

# M : 행동 횟수
M = int(input())

data = []
for _ in range(M):
    X, Y = map(int, input().split())
    data.append((X, Y))

# 앞쪽 벽부터 차례대로 부수도록 정렬
data.sort(key=lambda i:(i[0], i[1]))
for X, Y in data:
    if find_parent(parent, X) != find_parent(parent, Y):
        union_parent(parent, X, Y)

print(len(set(parent[1:])))