n = int(input())        # 부품 N개
array = list(map(int, input().split()))     # 부품 번호
m = int(input())        # 찾으려는 부품 개수
x = list(map(int, input().split()))     # 찾으려는 부품 번호

array = set(array)
for target in x:
    if target in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')

