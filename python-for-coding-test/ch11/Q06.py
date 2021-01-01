def move(length, idx):
    idx += 1
    if idx >= length:
        idx -= length
    return idx


def solution(food_times, k):
    answer = 0
    length = len(food_times)
    if sum(food_times) <= k:
        return -1

    for _ in range(k):
        while food_times[answer] == 0:
            answer = move(length, answer)
        food_times[answer] -= 1

    answer = move(length, answer) + 1
    return answer

print(solution([3, 1, 2], 5))