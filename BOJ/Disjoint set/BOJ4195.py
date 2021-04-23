import sys

input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b, number):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # a가 b의 부모임을 전제
    if a != b:
        parent[b] = a
        number[a] += number[b]
        number[b] = number[a]

n = int(input())
for _ in range(n):
    parent = {}
    number = {}
    f = int(input())
    for i in range(f):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1

        union_parent(parent, a, b, number)

        ans = 0
        print(number[find_parent(parent, a)])