from collections import deque
from itertools import permutations


def solution(expression):
    # 사용하는 연산자
    op = ["*", "+", "-"]
    lst = list(permutations(op, 3))  # 연산자 순열
    prec = []  # 연산자 순열 우선순위 리스트

    for x in lst:
        # 각 순열에 대한 우선순위 (딕셔너리 타입)
        dict = {}
        for i, y in enumerate(x):
            dict[y] = i
        prec.append(dict)

    answer = 0
    for p in prec:
        expr = infixToPostfix(p, expression)
        answer = max(answer, calculate(expr))
    return answer


def infixToPostfix(prec, expression):
    # 중위 표현식 -> 후위 표현식
    number = ""
    exp = []
    stack = deque([])
    for ch in expression:
        if ch.isdigit():  # 숫자 일 때
            number += ch
        else:  # 연산자 일 때
            # 리스트에 지금까지 읽은 숫자 넣기
            exp.append(int(number))
            number = ""

            # 스택이 비어있을 때
            if not stack:
                stack.append(ch)  # 연산자를 스택에 넣는다.
            else:  # 스택이 비어있지 않을 때
                while stack:
                    # 스택 top의 연산자 우선 순위가 더 높으면 꺼낸다.
                    if prec[stack[-1]] >= prec[ch]:
                        exp.append(stack.pop())
                    # 스택 top의 연산자 우선 순위가 낮으면 반복문 종료
                    else:
                        break
                # 읽은 연산자를 스택에 넣는다.
                stack.append(ch)
    # 숫자를 스택에 넣는다.
    exp.append(int(number))
    # 스택이 비어있지 않을 때
    while stack:
        # 스택에서 하나씩 pop 하며 연산자를 리스트에 삽입
        exp.append(stack.pop())
    return exp


def calculate(expression):
    # 후위 표현식 계산
    stack = deque([])
    for n in expression:
        if n == "+":
            n2 = stack.pop()
            n1 = stack.pop()
            stack.append(n1 + n2)
        elif n == "-":
            n2 = stack.pop()
            n1 = stack.pop()
            stack.append(n1 - n2)
        elif n == "*":
            n2 = stack.pop()
            n1 = stack.pop()
            stack.append(n1 * n2)
        else:
            stack.append(n)
    # 절댓값 반환
    return abs(stack.pop())
