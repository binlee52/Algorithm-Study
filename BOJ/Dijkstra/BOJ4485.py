import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

def in_range(x, y):
    global N
    if 0 <= x < N and 0 <= y < N:
        return True
    return False


def dijkstra(graph):
    global N
    distance = [[INF] * N for _ in range(N)]
    distance[0][0] = graph[0][0]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    q = []
    heapq.heappush(q, (graph[0][0], (0, 0)))   # (비용, 도착지)

    while q:
        dist, (x, y) = heapq.heappop(q)
        # now 까지 최단경로로 이동한 것이 아닌 경우
        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if in_range(nx, ny):
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, (nx, ny)))

    return distance[N-1][N-1]


cnt = 1
while True:
    N = int(input())
    if N == 0:
        break
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    print("Problem {}: {}".format(cnt, dijkstra(graph)))
    cnt += 1