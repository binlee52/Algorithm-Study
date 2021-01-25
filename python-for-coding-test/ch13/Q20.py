from itertools import combinations

N = int(input())
graph = []
for _ in range(N):
    graph.append((input().split()))

for i in range(N):
    for j in range(N):
        print(graph[i][j], end=" ")
    print()

items = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'X':
            items.append('{}{}'.format(i, j))
print(list(map(''.join, combinations(items, 3))))