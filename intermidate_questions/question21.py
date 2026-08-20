# 21. Find Intersection of Two Lists

# Question: Find the common elements between two lists without duplicate results.

# Answer:

a = [1, 2, 3, 4, 5]
b = [3, 4, 4, 5, 6]


result = []


for num in a:
    if num in b and num not in result:
        result.append(num)


print(result)