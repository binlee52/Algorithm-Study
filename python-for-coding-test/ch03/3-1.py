N = int(input(">> "))
coins = [500, 100, 50, 10]
answer = 0
for coin in coins:
    answer += N // coin
    N %= coin
print(answer)