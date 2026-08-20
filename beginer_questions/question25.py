# 25. Find Second Largest Number

# Question: Find the second-largest unique number in a list.

# Answer:

numbers = [10, 25, 45, 30, 45, 20]


unique = list(set(numbers))
unique.sort()


if len(unique) >= 2:
    print("Second largest =", unique[-2])
else:
    print("No second largest number")