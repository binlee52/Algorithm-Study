# 단어의 개수
N = int(input())
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

dic = {}
for alphabet in alphabets:
    dic[alphabet] = 0

for _ in range(N):
    word = input()[::-1]
    for i, ch in enumerate(word):
        dic[ch] += 10 ** i

dic = sorted(dic.items(), key=lambda i: i[1], reverse=True)
result = 0
for i, (key, value) in enumerate(dic[:10]):
    result += (9-i) * value
print(result)

