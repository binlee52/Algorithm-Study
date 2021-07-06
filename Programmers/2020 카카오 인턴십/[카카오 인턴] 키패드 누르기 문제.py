def solution(numbers, hand):
    answer = ''
    left = (1, 4, 7)
    right = (3, 6, 9)
    lp = "*"
    rp = "#"

    for number in numbers:
        if number in left:
            answer += "L"
            lp = number
        elif number in right:
            answer += "R"
            rp = number
        else:
            if distance(lp, number) < distance(rp, number):
                answer += "L"
                lp = number
            elif distance(lp, number) > distance(rp, number):
                answer += "R"
                rp = number
            else:
                if hand == "right":
                    answer += "R"
                    rp = number
                else:
                    answer += "L"
                    lp = number

    return answer


def location(number):
    if number == 0:
        return (3, 1)
    elif number == "*":
        return (3, 0)
    elif number == "#":
        return (3, 2)
    else:
        x = (number - 1) // 3
        y = (number - 1) % 3
        return (x, y)


def distance(x, y):
    p = location(x)
    np = location(y)
    return abs(p[0] - np[0]) + abs(p[1] - np[1])