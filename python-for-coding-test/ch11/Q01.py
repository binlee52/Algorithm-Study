n = int(input())
x = list(map(int, input().split()))

x.sort()
result = 0
temp = 0

for i in x:
    if temp == 0:
        temp = i
    else:
        temp -= 1
    if temp == 0:
        result += 1

print(result)