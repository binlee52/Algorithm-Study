steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
col = ['1', '2', '3', '4', '5', '6', '7', '8']

input_data = input()
x = row.index(input_data[0])
y = col.index(input_data[1])
result = 0

for step in steps:
    if 0 <= x + step[0] < 8 and 0 <= y + step[1] < 8:
        result += 1

print(result)