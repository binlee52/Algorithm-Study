import sys

input = sys.stdin.readline

gear = [[]]
for _ in range(4):
    gear.append(input().rstrip())
# K : 회전 횟수
K = int(input())

# 현재 톱니바퀴의 왼쪽 톱니바퀴가 회전할 수 있는가?
def is_left_rotatable(n):
    if n <= 1:
        return False
    if gear[n-1][2] != gear[n][-2]:
        return True
    return False


# 현재 톱니바퀴의 오른쪽 톱니바퀴가 회전할 수 있는가?
def is_right_rotatable(n):
    if n >= 4:
        return False
    if gear[n][2] != gear[n+1][-2]:
        return True
    return False


# 현재 톱니바퀴를 회전
def rotate(n, clock=1):
    # 시계방향으로 회전
    if clock == 1:
        gear[n] = gear[n][-1] + gear[n][:-1]
    # 반시계 방향으로 회전
    elif clock == -1:
        gear[n] = gear[n][1:] + gear[n][0]
    else:
        raise Exception("Unexpected clock direction")

# 최종 점수 계산
def score():
    return int(gear[1][0]) + int(gear[2][0]) * 2 + int(gear[3][0]) * 4 + int(gear[4][0]) * 8

# 재귀적으로 왼쪽 톱니바퀴 회전
def rotate_left(n, d):
    # 왼쪽 톱니바퀴가 회전할 수 있으면
    if is_left_rotatable(n):
        # 재귀호출(방향 전환)
        rotate_left(n-1, -d)
        # 왼쪽 톱니바퀴 회전
        rotate(n-1, d)
    # 왼쪽 톱니바퀴를 회전할 수 없으면 아무것도 하지 않음

# 재귀적으로 오른쪽 톱니바퀴 회전
def rotate_right(n, d):
    # 오른쪽 톱니바퀴가 회전할 수 있으면
    if is_right_rotatable(n):
        # 재귀호출(방향 전환)
        rotate_right(n+1, -d)
        # 오른쪽 톱니바퀴 회전
        rotate(n+1, d)

# 톱니바퀴 돌리기
def simulate(n, d):
    rotate_left(n, -d)
    rotate_right(n, -d)
    rotate(n, d)


for _ in range(K):
    n, d = map(int, input().split())
    # 왼쪽 친구가 회전 가능하면
    simulate(n, d)

print(score())
