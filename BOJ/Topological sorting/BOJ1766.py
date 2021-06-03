import heapq
import sys

input = sys.stdin.readline
# N : 문제의 수, M : 정보의 개수
N, M = map(int, input().split())

indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    # A -> B
    A, B = map(int, input().split())
    graph[A].append(B)  # 인접 노드
    indegree[B] += 1    # 선행조건

# 가능한 쉬운 문제부터 풀어야하므로 heapq 사용
q = []

for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)

while q:
    now = heapq.heappop(q)
    print(now, end=" ")

    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(q, i)
