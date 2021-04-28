from collections import deque

# N : 강의의 수
N = int(input())

graph = [[] for _ in range(N+1)]
time = [0] * (N+1)
indegree = [0] * (N+1)

for i in range(1, N + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]       # 시간
    # 각 라인의 마지막은 -1
    # x는 선수 강의
    for x in data[1:-1]:
        graph[x].append(i)      # x에서 i로 향하는 간선이 추가
        indegree[i] += 1        # i로 들어오는 간선이 1개 증가


def topology_sort():
    # 알고리즘 실행 결과
    result = time.copy()
    q = deque([])
    
    # 선수과목이 없는 과목 삽입
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[now] + time[i], result[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, N+1):
        print(result[i])


topology_sort()
