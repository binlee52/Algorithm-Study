# https://velog.io/@qweadzs/BOJ-12865-%ED%8F%89%EB%B2%94%ED%95%9C-%EB%B0%B0%EB%82%ADPython

# n : 물품의 수, k : 준수가 버틸 수 있는 무게
n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    item, value = map(int, input().split())
    for j in range(1, k + 1):
        if item > j:  # 현재 아이템의 무게가 현재 채우는 가방의 무게 보다 크면 덮어씀.
            dp[i][j] = dp[i - 1][j]
        else:
            # 현재 아이템을 넣을 수 있다면 전에 쓰던 아이템들과 비교를 해야함.
            # 전에 쓰던 아이템들을 그대로 가져갈 것이냐,
            # 아니면 현재 아이템을 넣어 가방의 무게를 맞출 것이냐
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item] + value)
print(dp[n][k])