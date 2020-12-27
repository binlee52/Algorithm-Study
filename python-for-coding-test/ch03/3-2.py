n, m, k = map(int, input('n, m, k >> ').split())
data = list(map(int, input('data >> ').split()))

data.sort()
result = (k*data[-1]+data[-2])*(m//(k+1))+data[-1]*(m%(k+1))

print(result)
