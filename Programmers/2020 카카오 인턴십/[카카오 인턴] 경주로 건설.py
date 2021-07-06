import sys
from collections import deque


def solution(board):
    answer = min(bfs(board, 1), bfs(board, 2))
    return answer


def bfs(graph, d):
    N = len(graph)
    INF = sys.maxsize
    distance = [[INF] * N for _ in range(N)]
    distance[0][0] = 0

    q = deque([(0, 0, 0, d)])
    # 북동남서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while q:
        dist, x, y, d = q.popleft()
        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 다음 것에서 바라보는 방향
            # 범위 안일 때
            if 0 <= nx < N and 0 <= ny < N and not graph[nx][ny]:
                # 도로로 연결이 가능할 때
                cost = dist + 100 if i == d else dist + 600
                # 현재까지의 최소비용보다 작다면
                if distance[nx][ny] > cost:
                    distance[nx][ny] = cost
                    q.append((cost, nx, ny, i))
    return distance[-1][-1]