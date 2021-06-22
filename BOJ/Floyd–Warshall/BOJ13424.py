import sys

input = sys.stdin.readline
INF = int(1e9)
# N : 방의 개수, M : 비밀통로의 개수, K : 모임에 참여하는 친구
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    distance = [[INF]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        distance[i][i] = 0

    for _ in range(M):
        a, b, c = map(int, input().split())
        distance[a][b] = c
        distance[b][a] = c

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                distance[i][j] = min(distance[i][k] + distance[k][j], distance[i][j])

    K = int(input())
    friend = list(map(int, input().split()))

    min_value = INF
    min_idx = 0
    for i in range(1, N+1):
        dist = sum([distance[i][f] for f in friend])
        if dist < min_value:
            min_value = dist
            min_idx = i

    print(min_idx)