N = int(input())
M = int(input())
graph = [[0] * N for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x, y = -1, 0
cnt = 0
num = N**2
loop = 2 * N
lx, ly = 0, 0
for _ in range(loop//2):
    x += dx[cnt]
    y += dy[cnt]
    graph[x][y] = num
    if num == M:
        lx, ly = x + 1, y + 1
    num -= 1

loop -= 1
cnt += 1
flag = True
while flag:
    for i in range(loop//2):
        x += dx[cnt % 4]
        y += dy[cnt % 4]
        graph[x][y] = num
        if num == M:
            lx, ly = x + 1, y + 1
        num -= 1
        if num < 1:
            flag = False
    cnt += 1
    loop -= 1

for row in graph:
    for x in row:
        print(x, end=" ")
    print()
print(lx, ly)