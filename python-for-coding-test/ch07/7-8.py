n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

start = 0
end = array[-1]

result = 0      # 절단기의 max 길이
while start <= end:
    mid = (start + end) // 2        # 절단기의 길이
    total = 0       # 손님이 가질 떡의 양
    for x in array:
        if x > mid:
            total += x - mid

    # 손님이 가질 떡의 양이 부족할 때
    if total < m:
        end = mid - 1
    else:
        result = mid        # 절단기의 최대길이 저장
        start = mid + 1

print(result)
