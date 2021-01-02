from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
q = deque([(0, 0, 1)])   # init location(x, y, 이동거리)
while q:
    x, y, d = q.popleft()
    graph[x][y] = 0     # 방문처리
    # n, m에 도착했을 때
    if x == n-1 and y == m-1:
        answer = d  # 이동거리 저장
        break
    # 사방 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # nx, ny가 범위 안에 존재하고, 해당 위치에 방문하지 않았을 대
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            q.append((nx, ny, d+1))

print(answer)