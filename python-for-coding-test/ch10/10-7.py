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


# 0 ~ n 까지 n + 1개의 팀 존재
# n : 팀, m : 연산의 개수
n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    opt, a, b = map(int, input().split())
    # 같은 팀 여부 확인
    if opt:
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a == b:
            print("YES")
        else:
            print("NO")
    else:
        union_parent(parent, a, b)
