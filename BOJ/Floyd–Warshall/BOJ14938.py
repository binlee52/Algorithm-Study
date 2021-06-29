import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

# N : 지역의 개수, M : 수색범위, R : 길의 개수
N, M, R = map(int, input().split())
# T : 아이템의 수
T = [0] + list(map(int, input().split()))

graph = [[INF] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    graph[i][i] = 0
for _ in range(R):
    # A, B : 지역의 번호, L : 길의 길이
    A, B, L = map(int, input().split())
    graph[A][B] = L
    graph[B][A] = L

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = 0
for i in range(1, N+1):
    result = sum([T[j] for j in range(1, N+1) if graph[i][j] <= M])
    if answer < result:
        answer = result

print(answer)
