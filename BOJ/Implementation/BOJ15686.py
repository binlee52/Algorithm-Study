# 굳이 BFS를 사용할 필요 없다. O(1) 시간 안에 치킨가게와의 거리를 구할 수 있다.
import sys
from itertools import combinations

input = sys.stdin.readline

# 치킨 거리 공식
def chicken_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1 - y2)

# N * N 크기 도시, 치킨집 M개
N, M = map(int, input().split())

# 치킨 거리 최소화
graph = []
home = []
chicken = []
for i in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            home.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

# 치킨 가게 조합
combination = list(combinations(chicken, M))
answer = int(1e9)
for case in combination:
    total = 0
    # 각 집에서 최소 치킨거리 계산
    for x, y in home:
        total += min([chicken_distance(x, y, cx, cy) for cx, cy in case])
    # 최솟값 갱신
    if answer > total:
        answer = total
print(answer)
