n = input()
x = list(map(int, n[:len(n)//2]))
y = list(map(int, n[len(n)//2:]))
if sum(x) == sum(y):
    print("LUCKY")
else:
    print("READY")