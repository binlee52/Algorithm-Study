import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

alphabet = [False] * 26
R, C = map(int, input().split())
visited = [[False]*C for _ in range(R)]
graph = []
for _ in range(R):
    graph.append(input().rstrip())


def dfs(x, y, c):
    global answer
    if answer < c:
        answer = c

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if not alphabet[ord(graph[nx][ny]) - ord('A')] and not visited[nx][ny]:
                visited[nx][ny] = True
                alphabet[ord(graph[nx][ny]) - ord('A')] = True
                dfs(nx, ny, c+1)
                alphabet[ord(graph[nx][ny]) - ord('A')] = False
                visited[nx][ny] = False

answer = 0
alphabet[ord(graph[0][0]) - ord('A')] = True
visited[0][0] = True
dfs(0, 0, 1)
print(answer)
