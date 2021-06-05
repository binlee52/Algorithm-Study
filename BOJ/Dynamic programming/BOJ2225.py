N = 40
# [0] : 0, [1] : 1
fibonacci = [(0, 0)] * (N + 1)
fibonacci[0] = (1, 0)
fibonacci[1] = (0, 1)
for i in range(2, N+1):
    fibonacci[i] = (fibonacci[i - 1][0] + fibonacci[i - 2][0], fibonacci[i - 1][1] + fibonacci[i - 2][1])

T = int(input())
for _ in range(T):
    N = int(input())
    print("{} {}".format(fibonacci[N][0], fibonacci[N][1]))
