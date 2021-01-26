from itertools import combinations
import sys

input = sys.stdin.readline
N = int(input())
graph = []
for _ in range(N):
    graph.append((input().split()))

hurdles = []
teachers = []
students = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'X':
            hurdles.append('{}{}'.format(i, j))
        if graph[i][j] == 'S':
            students.append((i, j))
        if graph[i][j] == 'T':
            teachers.append((i, j))

hurdles = list(map(''.join, combinations(hurdles, 3)))

def is_safe(sx, sy, tx, ty, hurdle):
    safe = True
    if sx == tx:
        if sx not in hurdle[0::2]:
            safe = False
        else:
            for i in range(3):
                if sx == hurdle[i * 2]:
                    idx = i * 2 + 1
                    # 동일한 x 축 좌표에 장애물이 여러개 존재할 수도 있다. 이에 대한 예외 처리가 필요하다.
                    if not (sy < hurdle[idx] < ty or ty < hurdle[idx] < sy):
                        safe = False
    if sy == ty:
        if sy not in hurdle[1::2]:
            safe = False
        # 동일한 y축 좌표상에 장애물이 존재하면
        else:
            # 동일한 y 축 좌표에 장애물이 여러개 존재할 수도 있다. 이에 대한 예외 처리가 필요하다.
            for i in range(3):
                if sy == hurdle[i * 2 + 1]:
                    idx = i * 2
                    # 장애물이 학생과 선생님 사이에 존재하지 않으면
                    if not (sx < hurdle[idx] < tx or tx < hurdle[idx] < sx):
                        safe = False
    return safe


# safe default
safe = True
for hurdle in hurdles:
    # 모든 학생이 안전하다고 가정
    safe = True
    hurdle = list(map(int, hurdle))
    
    # 모든 학생들에 대해
    for sx, sy in students:
        # 모든 선생 고려
        for tx, ty in teachers:
            safe = safe and is_safe(sx, sy, tx, ty, hurdle)
            '''
            # 학생과 선생이 x축 좌표상에서 일직선으로 위치할 때
            if sx == tx:
                # 동일한 x축 좌표상에 장애물이 존재하지 않으면
                if sx not in hurdle[0::2]:
                    # 안전하지 않은 학생이 존재
                    safe = False
                # 동일한 x축 좌표상에 장애물이 존재하면
                else:
                    for i in range(3):
                        if sx == hurdle[i*2]:
                            idx = i * 2 + 1
                            # 동일한 x 축 좌표에 장애물이 여러개 존재할 수도 있다. 이에 대한 예외 처리가 필요하다.
                            if not (sy < hurdle[idx] < ty or ty < hurdle[idx] < sy):
                                safe = False


            # 학생과 선생이 y축 좌표상에서 일직선으로 위치할 때
            if sy == ty:
                if sy not in hurdle[1::2]:
                    safe = False
                # 동일한 y축 좌표상에 장애물이 존재하면
                else:
                    # 동일한 y 축 좌표에 장애물이 여러개 존재할 수도 있다. 이에 대한 예외 처리가 필요하다.
                    for i in range(3):
                        if sy == hurdle[i*2+1]:
                            idx = i * 2
                            # 장애물이 학생과 선생님 사이에 존재하지 않으면
                            if not (sx < hurdle[idx] < tx or tx < hurdle[idx] < sx):
                                safe = False
                '''
    if safe:
        print(hurdle)
        break

print("YES") if safe else print("NO")