# 3-2
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)
first, second = data[0], data[1]
answer = (first * k + second) * (m // (k+1)) + (m % (k+1)) * first

print(answer)