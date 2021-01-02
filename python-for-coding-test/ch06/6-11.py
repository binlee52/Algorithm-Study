n = int(input())
data = []
for _ in range(n):
    name, score = input().split()
    score = int(score)
    data.append((name, score))

data.sort(key=lambda x: x[1])

for student, _ in data:
    print(student, end=' ')