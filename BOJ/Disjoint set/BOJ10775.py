import sys

input = sys.stdin.readline

# 가장 많은 비행기를 도킹하려면 도킹 할 수 있는 곳 중 가장 큰 수의 게이트에 도킹해야 한다.
# 같은 번호의 값이 들어오면 가장 큰 값보다 작은 게이트에 비행기가 도킹해야한다.
# 이를 union-find로 구현한다.
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


# G : 게이트의 수
G = int(input())
# P : 비행기의 수
P = int(input())
parent = [i for i in range(G+1)]
cnt = 0

for _ in range(P):
    x = int(input())
    x = find_parent(parent, x)
    if x == 0:
        break
    # 다음에 도킹해야 할 곳을 parent[x]에 설정
    union_parent(parent, x, x-1)
    cnt += 1

print(cnt)
