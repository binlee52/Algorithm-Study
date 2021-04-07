n = int(input())
actions = input().split()
move = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
x, y = 1, 1
for action in actions:
    nx = x + move[action][0]
    ny = y + move[action][1]

    if 0 < nx <= n and 0 < ny <= n:
        x, y = nx, ny

print(x, y)

