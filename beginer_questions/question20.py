# 20. Remove Duplicates

# Question: Remove duplicate values from a list.

# Answer:

numbers = [1, 2, 2, 3, 4, 4, 5, 5]


unique = []


for num in numbers:
    if num not in unique:
        unique.append(num)


print("Without duplicates:", unique)