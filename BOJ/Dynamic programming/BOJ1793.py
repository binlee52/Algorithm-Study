dp = [1, 1]
for i in range(2, 251):
    dp.append(dp[i-2]*2+dp[i-1])

while True:
    try:
        n = int(input())
    except:
        break
    print(dp[n])