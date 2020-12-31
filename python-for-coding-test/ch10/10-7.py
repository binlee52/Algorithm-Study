def find_parent(graph, x):
    if graph[x] != x:
        graph[x] = find_parent(graph, graph[x])
    return graph[x]


def check_parent(graph, x, y):
    if find_parent(graph, x) == find_parent(graph, y):
        return True
    return False


def union_parent(graph, x, y):
    x = find_parent(graph, x)
    y = find_parent(graph, y)
    if x > y:
        graph[x] = y
    else:
        graph[y] = x


n, m = map(int, input().split())
graph = [i for i in range(n+1)]
for _ in range(m):
    mod, a, b = map(int, input().split())
    if mod == 0:
        union_parent(graph, a, b)
    elif mod == 1:
        if check_parent(graph, a, b):
            print("YES")
        else:
            print("NO")
    print(graph)
