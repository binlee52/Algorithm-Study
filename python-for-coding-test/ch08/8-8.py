n, m = map(int, input().split())
INF = int(1e9)
array = []
d = [INF] * (100000+1)

for i in range(n):
    array.append(int(input()))

# 0원의 경우, 화폐를 하나도 사용하지 않으므로
d[0] = 0

for i in range(m+1):
    # 모든 동전에 대하여
    for x in array:
        # (i-x)원이 0 이상인 경우
        if i >= x:
            # i-x 원을 만들 수 없으면 갱신 x
            d[i] = min(d[i-x] + 1, d[i])

print(d[m]) if d[m] != INF else print(-1)
