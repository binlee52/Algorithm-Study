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


# # 재귀함수 (내가한거)
# def binary_search(array, target, start, end, max_height):
#     if start > end:
#         return max_height
#
#     height = (start + end) // 2     # 절단기 높이
#     length = 0  # 손님에게 주는 떡의 길이
#     for a in array:
#         piece = a - height
#         if piece > 0:
#             length += piece
#
#     # 조건을 만족할 시
#     if length > target:
#         return binary_search(array, target, height + 1, end, height)
#     elif length < target:
#         return binary_search(array, target, start, height - 1, max_height)
#     else:
#         return height
#
#

# print(binary_search(array, m, 0, array[-1], 0))