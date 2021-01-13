nums = input()

result = int(nums[0])
for num in nums[1:]:
    temp_1 = result + int(num)
    temp_2 = result * int(num)
    result = temp_1 if temp_1 > temp_2 else temp_2

print(result)