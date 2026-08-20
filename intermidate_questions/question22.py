# 22. Maximum Subarray Sum

# Question: Find the contiguous subarray having the maximum sum.

# Answer:

numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


current = numbers[0]
maximum = numbers[0]


for num in numbers[1:]:
    current = max(num, current + num)
    maximum = max(maximum, current)


print("Maximum subarray sum:", maximum)