G = int(input())        # 게이트의 수
P = int(input())        # 비행기의 수

# 게이트 사용 여부
gate = [False] * (G+1)

lst = []

for i in range(P):
    lst.append((int(input()), i))       # 입력받은 값, 입력받은 순서

lst.sort(key=lambda i: i[0])
last = 0

now = 1         # 비어있는 가장 앞 게이트
lost = int(1e9)
for x, y in lst:
    # 도킹할 수 없는 비행기가 존재할 때
    if lost < y < last:
        break

    # x가 게이트를 찾았는지 확인
    flag = False
    for i in range(now, x+1):
        if not gate[i]:
            gate[i] = True
            now += 1
            flag = True
            last = max(last, y)
            break

    # 게이트를 찾지 못했을 때, 잃어버린 가장 앞 값 갱신
    if not flag and lost > y:
        lost = y


ans = len([x for x in gate if x])
print(ans)
