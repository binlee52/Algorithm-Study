data = input()
alphabets = [x for x in data if ('a' <= x <= 'z' or 'A' <= x <= 'Z')]
nums = [int(x) for x in data if '0' <= x <= '9']
alphabets.sort()
result = ''
for alphabet in alphabets:
    result += alphabet
result += str(sum(nums))
print(result)

