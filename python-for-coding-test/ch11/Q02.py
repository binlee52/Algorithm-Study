nums = input()
result = int(nums[0])
for num in nums[1:]:
    x = result + int(num)
    y = result * int(num)
    if x > y:
        result = x
    else:
        result = y

print(result)