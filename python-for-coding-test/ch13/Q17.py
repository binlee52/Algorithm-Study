from collections import deque
import sys


input = sys.stdin.readline
N, K = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
S, X, Y = map(int, input().split())

q = []
for i in range(N):
    for j in range(N):
        if data[i][j] != 0:
            q.append((data[i][j], i, j, 0))
q.sort()
q = deque(q)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    virus, x, y, time = q.popleft()
    if time == S:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if data[nx][ny] == 0:
                data[nx][ny] = virus
                q.append((data[nx][ny], nx, ny, time+1))


print(data[X-1][Y-1])