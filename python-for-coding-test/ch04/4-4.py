n, m = map(int, input().split())
x, y, direction = map(int, input().split())

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽으로 회전
def rotate_left():
    global direction
    if direction == 0:
        direction = 3
    else:
        direction -= 1


array = []      # 지도
visited = []    # 지도에서 방문한 곳을 1로 처리
for i in range(n):
    temp = list(map(int, input().split()))
    array.append(temp)
    visited.append(temp)


visited[x][y] = 1   # 현재 위치 방문 처리
result = 1  # 현재 위치 방문 처리 count
turn_time = 0   # 회전 횟수

while True:
    # 왼쪽 방향으로 회전
    rotate_left()

    # 한 칸 전진
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 정면에 가보지 않은 칸이 존재하고, 육지인 경우
    if visited[nx][ny] == 0 and array[nx][ny] == 0:
        x, y = nx, ny
        visited[nx][ny] = 1
        result += 1
        turn_time = 0
        continue

    # 이미 가본 칸이거나 바다인 경우
    turn_time += 1

    # 네 방향 모두 이미 가본 칸이거나 바다인 경우
    if turn_time == 4:
        turn_time = 0
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 갈 수 없는 경우
        if array[nx][ny] == 1:
            # 움직임을 멈춘다
            break
        # 뒤로 갈 수 있다면 바라보는 방향을 유지한 채 뒤로간다
        else:
            x, y = nx, ny


print(result)



