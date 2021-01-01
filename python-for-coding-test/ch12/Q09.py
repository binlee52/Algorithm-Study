def compress(text, size):
    result = ''     # 압축된 텍스트
    i = 0
    while i < len(text):
        # 문자열의 부분이 중복될 때
        if text[i:i+size] == text[i+size:i+2*size]:
            dup = text[i:i+size]    # 중복되는 부분
            cnt = 1     # init 중복 횟수
            
            # 중복되는 부분이 안 나올 때까지, 혹은 범위를 초과하지 않을 때까지
            while (i < len(text) - size) and text[i:i+size] == text[i+size:i+2*size]:
                i += size       # size 만큼 index 이동
                cnt += 1        # 중복 횟수 더함
            i += size           # 마지막 인덱스 위치(i+2*size)로 이동을 위해 한번 더 더한다.
            result += str(cnt) + dup        # 텍스트 압축하여 생성
        else:
            result += text[i:i+size]
            i += size

    # 압축된 텍스트의 길이를 반환
    return len(result)


def solution(s):
    answer = compress(s, 1)     # 1 단위로 압축했을 때(초기값)

    # 2부터 s 길이의 절반 단위로 문자열 압축
    for i in range(2, len(s)//2+1):
        answer = min(answer, compress(s, i))
    return answer


data = input()
print(solution(data))