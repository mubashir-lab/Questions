# 7. Find Maximum Consecutive Ones

# Question: Given a binary list, find the maximum number of consecutive 1s.

# Answer:

numbers = [1, 1, 0, 1, 1, 1, 0, 1]


current = 0
maximum = 0


for num in numbers:
    if num == 1:
        current += 1
        maximum = max(maximum, current)
    else:
        current = 0


print("Maximum consecutive ones:", maximum)