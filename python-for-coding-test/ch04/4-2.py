n = int(input())
result = 0

if 0 <= n < 3:
    result = (3600 - 45 * 45) * (n + 1)
elif 3 <= n < 13:
    result = 3600 + (3600 - 45 * 45) * n
elif 13 <= n < 23:
    result = 3600 * 2 + (3600 - 45 * 45) * (n-1)
elif n == 23:
    result = 3600 * 3 + (3600-45*45) * (n-2)


print(result)