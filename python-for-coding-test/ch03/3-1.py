# 3-1
coins = [500, 100, 50, 10]
n = int(input())
answer = 0

for coin in coins:
    answer += n // coin
    n = n % coin

print(answer)