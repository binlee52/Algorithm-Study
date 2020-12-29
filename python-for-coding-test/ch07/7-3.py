# 이진 탐색 코드(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
        else:
            return mid
    return None


n, target = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
result = binary_search(array, target, 0, len(array)-1)

if result:
    print(result + 1)
else:
    print("{}이 존재하지 않습니다.".format(target))