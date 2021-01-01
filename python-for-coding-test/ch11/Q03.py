data = input()

count0 = 0 # 모두 0으로 바꾸는 경우
count1 = 0 # 모두 1로 바꾸는 경우
if data[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두번째 원소부터 모든 원소를 확인
for i in range(len(data) -1):
    # 연속하는 원소가 아닐 때 뒤집는다.
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))


