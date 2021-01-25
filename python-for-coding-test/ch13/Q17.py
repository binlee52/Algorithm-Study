import heapq as hq
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
S, X, Y = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = []

for _ in range(S):
    for i in range(N):
        for j in range(N):
            if data[i][j] != 0:
                hq.heappush(q, (data[i][j], i, j))
    while q:
        virus, x, y = hq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if data[nx][ny] == 0:
                    data[nx][ny] = virus
    print("graph")
    for row in data:
        for col in row:
            print(col, end=' ')
        print()

print(data[X-1][Y-1])