import sys
from string import ascii_lowercase, ascii_uppercase

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

input = sys.stdin.readline
alphabet = {"0": -1}
for i, x in enumerate(ascii_lowercase + ascii_uppercase):
    alphabet[x] = i+1

# N : 컴퓨터의 개수
N = int(input())

edges = []
answer = 0


for i in range(1, N + 1):
    data = list(map(alphabet.get, list(input().rstrip())))
    answer += sum(data)
    for j in range(1, N+1):
        if data[j-1] != -1:
            edges.append((data[j-1], i, j))

parent = [i for i in range(N+1)]
edges.sort(key=lambda i: i[0])

cnt = 1
for cost, src, dst in edges:
    if find_parent(parent, src) != find_parent(parent, dst):
        union_parent(parent, src, dst)
        answer -= cost
        cnt += 1

parent = [find_parent(parent, x) for x in parent]
if cnt != N:
    print(-1)
else:
    print(answer)
