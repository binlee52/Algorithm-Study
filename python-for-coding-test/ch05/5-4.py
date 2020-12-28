from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


def bfs():
    # D, U, R, L 방향으로 이동
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # init location (init_x, init_y, cnt)
    q = deque([(0, 0, 1)])

    while q:
        x, y, cnt = q.popleft()
        graph[x][y] = 0     # 방문

        # 출구에 도착
        if x == n-1 and y == m-1:
            return cnt

        # 4 방향에 대하여 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 공간을 벗어나지 않았을 때
            if 0 <= nx < n and 0 <= ny < m:
                # 괴물이 없을 때 or 방문하지 않았을 때
                if graph[nx][ny] == 1:
                    q.append((nx, ny, cnt + 1))

    return -1    # 탐색 실패


print(bfs())
