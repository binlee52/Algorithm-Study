from collections import deque

q = deque([])

N, K = map(int, input().split())
for x in range(1, N+1):
    q.append(x)

i = 1
result = []
while q:
    if K > i:
        i += 1
        q.append(q.popleft())
    else:
        i = 1
        result.append(q.popleft())

result = [str(i) for i in result]
print("<{}>".format(', '.join(result)))