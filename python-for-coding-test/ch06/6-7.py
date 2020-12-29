n = int(input())
array = []
for _ in range(n):
    name, score = input().split()
    array.append((name, int(score)))

array = sorted(array, key=lambda x: x[1])

for name, score in array:
    print(name, end=' ')
