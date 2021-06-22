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

# N : 사람의 수, M : 파티의 수
N, M = map(int, input().split())
# truth : 진실을 아는 사람
truth = list(map(int, input().split()))[1:]

parent = [i for i in range(N+1)]
graph = []

for _ in range(M):
    # 각 파티 참여자 정보 추가
    data = list(map(int, input().split()))[1:]
    graph.append(data)
    
    # 파티 참여자끼리 결합
    if len(data) > 1:
        for x, y in zip(data[:-1], data[1:]):
            if find_parent(parent, x) != find_parent(parent, y):
                union_parent(parent, x, y)

parent = [find_parent(parent, i) for i in parent]
truth = [find_parent(parent, i) for i in truth]

answer = 0
# 각 파티에 대하여
for data in graph:
    flag = True     # 진실을 아는자가 없다고 가정
    # 파티에 대한 참여자에 대하여
    for x in data:
        # 진실을 아는자가 존재할 때 (진실을 아는 자와 연결되어 있을 때)
        if find_parent(parent, x) in truth:
            flag = False
            break
    # 진실을 아는자가 파티에 존재하지 않을 때
    if flag:
        answer += 1

print(answer)
