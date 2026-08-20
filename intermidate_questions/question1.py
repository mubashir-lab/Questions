# 1. Find the Second Largest Number Without Sorting

# Question: Given a list of integers, find the second-largest unique number without using sort() or sorted().

# Answer:

numbers = [10, 45, 23, 89, 67, 89, 34]


largest = float("-inf")
second = float("-inf")


for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif largest > num > second:
        second = num


print("Second largest:", second)