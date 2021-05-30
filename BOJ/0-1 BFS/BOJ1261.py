import heapq

INF = int(1e9)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

M, N = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

distance = [[INF] * M for _ in range(N)]

q = []
heapq.heappush(q, (0, (0, 0)))


def inRange(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True
    return False


distance[0][0] = 0
while q:
    dist, (x, y) = heapq.heappop(q)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        cost = dist + graph[x][y]
        if inRange(nx, ny) and cost < distance[nx][ny]:
            distance[nx][ny] = cost
            heapq.heappush(q, (cost, (nx, ny)))

print(distance[N-1][M-1])

