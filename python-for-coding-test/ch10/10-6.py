from collections import deque

# v : 노드의 개수, e : 간선의 개수
v, e = map(int, input().split())

# 인접 리스트
graph = [[] for _ in range(v+1)]
# 진입 차수
indegree = [0] * (v+1)

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    # a에서 b로 향하는 방향 그래프이므로 b로 진입하는 간선이 1개 늘어난다.
    indegree[b] += 1

def topology_sort():
    result = []

    q = deque([])
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=" ")


topology_sort()
