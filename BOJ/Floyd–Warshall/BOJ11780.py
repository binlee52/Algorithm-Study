import sys
from itertools import permutations


input = sys.stdin.readline
INF = int(1e9)

# n : 도시, k : 발사 위치
N, K = map(int, input().split())
# Map
graph = [[] for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int, input().split()))

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

arr = [i for i in range(N)]
arr.remove(K)       # 출발지 제거

ans = INF       # 정답

# 순열을 통한 모든 경우의 수 탐색
for lst in permutations(arr, len(arr)):
    sub = graph[K][lst[0]]
    for a, b in zip(lst[:-1], lst[1:]):
        sub += graph[a][b]
    ans = min(ans, sub)

print(ans)
