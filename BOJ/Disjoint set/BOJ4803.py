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


case = 0
while True:
    N, M = map(int, input().split())

    if N == 0 and M == 0:
        break

    parent = [i for i in range(N+1)]
    case += 1
    cycle = []
    
    for _ in range(M):
        A, B = map(int, input().split())
        # cycle이 발생하는 트리를 cycle list에 삽입
        if find_parent(parent, A) == find_parent(parent, B):
            cycle.append(A)
        else:
            union_parent(parent, A, B)
    
    # cycle이 발생한 트리의 개수를 추출
    cycle = len(set([find_parent(parent, i) for i in cycle]))
    # 트리의 개수를 모두 추출(cycle 있는 것 포함)
    parent = [find_parent(parent, i) for i in parent[1:]]

    cnt = len(set(parent))
    cnt -= cycle

    if cnt > 1:
        print("Case {}: A forest of {} trees.".format(case, cnt))
    elif cnt == 1:
        print("Case {}: There is one tree.".format(case, cnt))
    else:
        print("Case {}: No trees.".format(case))
