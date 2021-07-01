import sys

input = sys.stdin.readline


# N : 사람의 수
N = int(input())
name_list = list(map(int, input().split()))
info_name = {}
info_num = {}
for idx, name in enumerate(name_list):
    info_num[name] = idx+1
    info_name[idx+1] = name

parent = [i for i in range(N+1)]


