n = int(input())
k = list(map(int, input().split()))

# init DP table
d = [0] * 100

# Dynamic Programming(Bottom Up)
d[0] = k[0]
d[1] = max(d[0], d[1])

for i in range(n):
    d[i] = max(d[i-1], d[i-2] + k[i])

print(d[n-1])
