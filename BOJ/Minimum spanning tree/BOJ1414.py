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


for i in range(N):
    data = list(map(alphabet.get, list(input().rstrip())))
    answer += sum(data)
    for j in range(N):
        if data[j] != -1:
            if i != j:
                edges.append((data[j], i, j))

parent = [i for i in range(N)]
edges.sort(key=lambda i: i[0])

cnt = 1
for cost, src, dst in edges:
    if find_parent(parent, src) != find_parent(parent, dst):
        union_parent(parent, src, dst)
        answer -= cost
        cnt += 1

if cnt != N:
    print(-1)
else:
    print(answer)
