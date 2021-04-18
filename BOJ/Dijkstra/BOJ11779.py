import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# 도시의 개수
n = int(input())
# 버스의 개수
m = int(input())

# Adj Matrix
graph = [[] for _ in range(n+1)]

for _ in range(m):
    # a : 출발지, b : 도착지, c : 버스 비용
    a, b, c = map(int, input().split())
    graph[a].append((c, b))     # (비용, 도착지)

# start : 출발점, end : 도착점
start, end = map(int, input().split())

# 거리 초기화
# [거리, 이동경로]
distance = [[INF, '']] * (n+1)
distance[start] = [0, str(start)]

q = []
heapq.heappush(q, (0, start, str(start)))   # (비용, 도착지, 이동경로)

while q:
    dist, now, path = heapq.heappop(q)
    # now 까지 최단 경로로 이동한 것이 아닐 때
    if distance[now][0] < dist:
        continue

    # now 와 인접한 노드에 대하여
    # i[0] : 비용, i[1] : 도착지
    for i in graph[now]:
        cost = dist + i[0]
        route = path + ' ' + str(i[1])
        if cost < distance[i[1]][0]:
            distance[i[1]] = [cost, route]
            heapq.heappush(q, (cost, i[1], route))

print(distance[end][0])
print(len(distance[end][1].split()))
print(distance[end][1])
