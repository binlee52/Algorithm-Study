n = int(input())
lst = list(map(int, input().split()))
lst.sort()

s = 0   # x를 보기 전까지 본 수의 합

# 1부터 sum(lst) 까지 모두 만들 수 있다면
# sum(lst)보다 1 큰 값이 만들 수 없는 가장 작은 값이다.
for x in lst:
    # 이전까지 본 수의 합 + 1보다 지금 본 수가 크다면
    # ex) s = 1+2+3 = 6, x=8
    # ex2) s = 1+1+2, x=6
    # s+1 값은 만들 수 없는 숫자이다.
    if s + 1 < x:
        break
    s += x

print(s+1)
