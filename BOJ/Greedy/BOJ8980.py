import sys

input = sys.stdin.readline

# N : 마을 수, C : 트럭 용량
N, C = map(int, input().split())
# 박스 정보의 개수
M = int(input())

deliver = []

for _ in range(M):
    # a : 출발지, b : 도착지, c: 배송량
    a, b, c = map(int, input().split())
    deliver.append((a, b, c))

# 도착지를 기준으로 정렬, 도착지가 같다면 출발지를 기준으로 정렬
deliver.sort(key=lambda x: (x[1], x[0]))
capacity = [C] * (N+1)
total = 0

for d in deliver:
    # s : 출발지, t : 도착지, t : 배송량
    s, t, cost = d
    # s~t 사이에서 보낼 수 있는 최대 배송량을 구하기 위해선
    # 남은 배송량 중 최솟값을 구해야한다.
    max_cost = min(capacity[s:t])

    # cost를 전부 다 배송할 수 있다면
    if cost <= max_cost:
        for i in range(s, t):
            capacity[i] -= cost
        total += cost
    # 일부만 배송 가능하거나 배송 불가능하다면
    else:
        total += max_cost
        for i in range(s, t):
            capacity[i] -= max_cost

print(total)