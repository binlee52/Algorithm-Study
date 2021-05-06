import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    ans = 0

    # N : 책 번호, M : 책을 원하는 학부생
    N, M = map(int, input().split())
    # 책을 나눠줄 수 있는지 확인하는 리스트
    book = [False] * (N+1)

    # 사람들이 받고싶어하는 책의 범위를 받는 리스트
    lst = []
    for __ in range(M):
        lst.append(list(map(int, input().split())))
    # 항상 x[0] < x[1]이므로 x[1]을 기준으로 정렬하고, 같으면 x[0]을 기준으로 정렬
    lst.sort(key=lambda x: (x[1], x[0]))

    for s, t in lst:
        # s~t번 책을 살펴본다
        for i in range(s, t+1):
            # 나눠주지 않은 책을 찾으면
            if not book[i]:
                book[i] = True
                ans += 1
                break
    print(ans)
