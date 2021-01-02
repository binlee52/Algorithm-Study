# 3-4
n, k = map(int, input().split())
answer = 0
while n != 1:
    if n % k != 0:
        answer += n % k
        n -= n % k
    else:
        n //= k
        answer += 1

print(answer)