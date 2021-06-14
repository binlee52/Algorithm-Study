N = int(input())
dp = [0 for _ in range(N+1)]
for i in range(1, N+1):
    if i % 2 == 0:
        dp[i] = (i//2)**2 + 2 * dp[i//2]
    else:
        dp[i] = i//2 * (i//2 + 1) + dp[i//2] + dp[i//2 + 1]
print(dp[N])