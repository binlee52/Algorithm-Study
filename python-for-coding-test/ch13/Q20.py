from itertools import combinations
import sys

input = sys.stdin.readline
N = int(input())
graph = []
for _ in range(N):
    graph.append((input().split()))

def solution(N, graph):
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

    if not students:
        return False

    hurdles = list(map(''.join, combinations(hurdles, 3)))

    safe = True
    for hurdle in hurdles:
        safe = True
        hurdle = list(map(int, hurdle))
        for sx, sy in students:
            for tx, ty in teachers:
                safe = safe and is_safe(sx, sy, tx, ty, hurdle)
        if safe:
            return True
    return False

def is_safe(sx, sy, tx, ty, hurdle):
    safe = True
    if sx == tx:
        if sx not in hurdle[0::2]:
            safe = False
        else:
            for i in range(3):
                if sx == hurdle[i * 2]:
                    idx = i * 2 + 1
                    if not (sy < hurdle[idx] < ty or ty < hurdle[idx] < sy):
                        safe = False
    if sy == ty:
        if sy not in hurdle[1::2]:
            safe = False
        else:
            for i in range(3):
                if sy == hurdle[i * 2 + 1]:
                    idx = i * 2
                    if not (sx < hurdle[idx] < tx or tx < hurdle[idx] < sx):
                        safe = False
    return safe


safe = solution(N, graph)
print("YES") if safe else print("NO")