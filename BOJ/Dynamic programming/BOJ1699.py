from math import sqrt
n = int(input())
dp = [0 for i in range(n + 1)]
s = [i * i for i in range(1, int(sqrt(100000)) + 1)]

for i in range(1, n + 1):
    lst = []
    # 제곱 수에 대해 탐색
    for x in s:
        if i < x:
            break
        lst.append(dp[i - x])
    dp[i] = min(lst) + 1

print(dp[n])
