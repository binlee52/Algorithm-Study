import sys

input = sys.stdin.readline

# N : 마을 수, C : 트럭 용량
N, C = map(int, input().split())
# 박스 정보의 개수
M = int(input())

graph = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    # a : 출발지, b : 도착지, c: 배송량
    a, b, c = map(int, input().split())
    graph[a][b] += c

total = 0
curr = [0] * (N+1)

for dist in range(1, N):
    for now in range(1, N):
        nxt = now + dist

        if nxt <= N:
            flag = True
            min_weight = int(1e9)
            target = now
            for j in range(now, nxt):
                if curr[j] + graph[now][j] >= c:
                    flag = False
                    if min_weight >= C - curr[j]:
                        min_weight = C - curr[j]
                        target = j

            if flag:
                total += graph[now][nxt]
                for t in range(now, nxt):
                    curr[t] += graph[now][nxt]
            # 초과할 때
            else:
                total += min_weight
                for t in range(now, nxt):
                    curr[t] += min_weight


#
# for dist in range(1, N):
#     for now, x in enumerate(graph):
#         for i in x:
#             # 출발지와 목적지의 거리가 dist만큼 차이날 때
#             if now + dist == i[0]:
#                 flag = True
#                 min_weight = int(1e9)
#                 target = now
#                 for j in range(now, i[0]):
#                     # 전부 다 실을 수 없다면
#                     if curr[j] + i[1] > C:
#                         flag = False
#                         if min_weight >= C - curr[j]:
#                             min_weight = C - curr[j]
#                             target = j
#
#                 if flag:
#                     total += i[1]
#                     for t in range(now, i[0]):
#                         curr[t] += i[1]
#                 # 초과할 때
#                 else:
#                     total += min_weight
#                     for t in range(now, target+1):
#                         curr[t] += min_weight
#                 del i


print(total)




