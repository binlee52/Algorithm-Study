INF = 10001

n, m = map(int, input().split())
coins = []
d = [INF] * 10001

for i in range(n):
    coins.append(int(input()))
coins = set(coins)

d[0] = 0    # 0원의 경우, 화폐를 하나도 사용하지 않으므로
for i in range(m+1):
    # 모든 동전에 대하여
    for coin in coins:
        # 현재 금액을 동전 중 하나로 뺀다.
        x = i - coin
        # (i-k)원이 0 이상이고, (i-k)원을 만드는 방법이 존재하는 경우
        if x >= 0 and d[x] != INF:
            d[i] = min(d[x] + 1, d[i])


print(d[m]) if d[m] != INF else print(-1)