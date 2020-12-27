n, k = map(int, input().split())
result = 0

while True:
    # (N == K 로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)

# heapq를 사용하는 방법 - 더 느리다 ㅠㅠ
# import heapq as hq
#
# heap = []
# result  = 0
# n, k = map(int, input().split())
# hq.heappush(heap, (0, n))   # (우선순위, 값)
#
# while heap:
#     cnt, value = hq.heappop(heap)
#     if value == 1:
#         result = cnt
#         break
#
#     cnt += 1
#     if value % k == 0:
#         hq.heappush(heap, (cnt, value/k))
#     hq.heappush(heap, (cnt, value-1))
# print(result)



