import sys

input = sys.stdin.readline

# t : 테스트의 개수
t = int(input())
for _ in range(t):
    # n : 전화번호의 수
    n = int(input())
    lst = []    # 전화번호 리스트
    for _ in range(n):
        lst.append(input().rstrip())
    lst.sort()
    flag = True
    for x, y in zip(lst[:-1], lst[1:]):
        if x == y[:len(x)]:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")
