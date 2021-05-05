def tournament(lst):
    # 리스트 원소가 1개 이하일 때
    if len(lst) <= 1:
        return 0

    # 리스트 원소가 두개 일 때
    if len(lst) == 2:
        return abs(lst[0] - lst[1])
    
    # MAX 값의 인덱스
    idx = lst.index(max(lst))
    if idx == 0:
        val = abs(lst[idx] - lst[idx+1])
    elif idx == len(lst) - 1:
        val = abs(lst[idx-1] - lst[idx])
    else:
        nxt = max(lst[idx-1], lst[idx+1])
        val = abs(nxt - lst[idx])
    
    # MAX 값 삭제
    lst.remove(lst[idx])
    return val + tournament(lst)


n = int(input())
lst = list(map(int, input().split()))
print(tournament(lst))
