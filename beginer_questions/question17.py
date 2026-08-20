# 17. Find Minimum in a List

# Question: Find the smallest element in a list without using min().

# Answer:

numbers = [12, 45, 7, 89, 23, 56]


smallest = numbers[0]


for num in numbers:
    if num < smallest:
        smallest = num


print("Smallest =", smallest)