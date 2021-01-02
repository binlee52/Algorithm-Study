from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


answer = 0

# 모든 노드를 방문한다
for i in range(n):
    for j in range(m):
        # 해당 노드를 방문하지 않았을 때
        if graph[i][j] == 0:
            # 큐 생성
            q = deque([(i, j)])     # init
            # 방문 횟수 ++
            answer += 1
            
            # q가 빌 때까지
            while q:
                x, y = q.popleft()
                graph[x][y] = 1     # 방문 처리
                for step in range(4):       # 사방탐색
                    nx = x + dx[step]
                    ny = y + dy[step]
                    # nx, ny가 범위 안에 있고, 방문하지 않았을 때
                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 1:
                        q.append((nx, ny))      # 큐에 넣는다


print(answer)
