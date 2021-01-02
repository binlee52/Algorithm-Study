row = ['1', '2', '3', '4', '5', '6', '7', '8']
col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

y, x = list(input())
x = row.index(x)
y = col.index(y)
answer = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < 8 and 0 <= ny < 8:
        answer += 1
print(answer)
