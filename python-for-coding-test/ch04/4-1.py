n = int(input())
data = [[False] * (n+1) for _ in range(n+1)]
move = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

x, y = 1, 1
actions = input().split()
for action in actions:
    nx = x + move[action][0]
    ny = y + move[action][1]
    if 1 <= nx <= n and 1 <= ny <= n:
        x, y = nx, ny

print(x ,y)
