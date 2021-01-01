n = int(input())
x = list(map(int, input().split()))
x.sort(reverse=True)
result = 0
idx = 0
for i in x:
    if idx == 0:
        idx = i
    idx -= 1
    if idx == 0:
        result += 1

print(result)