# 두자리씩 나눠서 다이나믹 프로그래밍
# 그 이상의 차이나는 단위끼리는 greedy

# 동전 리스트
array = [1, 10, 25]

# 0~99원을 만드는데 필요한 coin 개수
d = [101] * 100
d[0] = 0

# 모든 coin 종류에 대하여 검사
for i in range(len(array)):
    # array[i] : 현재 보고있는 coin
    for j in range(array[i], 100):
        d[j] = min(d[j], d[j - array[i]] + 1)

T = int(input())
for _ in range(T):
    m = int(input())
    ans = 0

    while m:
        # 두자리씩 끊어서 확인
        ans += d[m % 100]
        m //= 100
    print(ans)
