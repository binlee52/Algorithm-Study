import sys
from collections import deque

input = sys.stdin.readline


def moveable(graph, x, y):
    # 벽이 아닐 때
    if graph[x][y] != 1:
        return True
    return False

# 청소할 수 있나
def cleanable(graph, x, y):
    return moveable(graph, x, y) and graph[x][y] == 0

def rotate_left(direction):
    return (direction - 1) % 4

def clean(graph, x, y, d):
    # graph가 1일 때 벽, 2일 때 청소 완료
    answer = 0
    # 북, 동, 남, 서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while True:
        # 청소할 수 있다면
        if graph[x][y] == 0:
            graph[x][y] = 2
            answer += 1

        flag = False    # init
        # 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색
        for _ in range(4):
            d = rotate_left(d)  # 왼쪽으로 회전
            nx = x + dx[d]
            ny = y + dy[d]
            # 청소 가능하다면
            if cleanable(graph, nx, ny):
                # 회전 후 한칸 전진 후 청소
                x, y = nx, ny
                flag = True
                break

        # 4방향 모두 청소한 경우
        if not flag:
            # 뒤로 한칸 후진
            nx = x - dx[d]
            ny = y - dy[d]
            # 뒤로 이동 가능할 때
            if moveable(graph, nx, ny):
                x, y = nx, ny
            # 뒤가 막혔을 때
            else:
                return answer


graph = []
# N : 세로, M : 가로
N, M = map(int, input().split())
# (r, c) : 로봇 청소기 좌표, d : 방향
r, c, d = map(int, input().split())
# graph : 지도
for _ in range(N):
    graph.append(list(map(int, input().split())))
print(clean(graph, r, c, d))


