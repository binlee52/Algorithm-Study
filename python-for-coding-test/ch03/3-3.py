# 3-3
n, m = map(int, input().split())
answer = int(1e-9)
for _ in range(n):
    data = list(map(int, input().split()))
    answer = max(answer, min(data))

print(answer)