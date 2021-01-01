from math import factorial

n, m = map(int, input().split())
data = list(map(int, input().split()))
count = [0] * 11

# 무게별 공의의 개수 count
for x in data:
    count[x] += 1

result = factorial(n)//(factorial(2) * factorial(n-2))
# 2개 이상 갖고 있는 것을 dup list로 이동
for c in count:
    if c > 1:
        result -= factorial(c) // (factorial(c) * factorial(c-2))

print(result)