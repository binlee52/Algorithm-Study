from collections import deque
import sys

input = sys.stdin.readline
def bfs():
    R, C = map(int, input().split())
    graph = []
    for _ in range(R):
        graph.append(input().rstrip())

    # visited = []
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    answer = 0
    visited = graph[0][0]
    q = deque([(0, 0, 1)])
    while q:
        x, y, cost = q.popleft()
        if answer < cost:
            answer = cost
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] not in visited:
                    visited += graph[nx][ny]
                    q.append((nx, ny, cost + 1))
    return answer

print(bfs())