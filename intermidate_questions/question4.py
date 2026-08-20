# 4. Find Duplicate Number

# Question: Find the duplicate value in a list containing numbers where one value appears more than once.

# Answer:

numbers = [1, 3, 4, 2, 2]


seen = set()


for num in numbers:
    if num in seen:
        print("Duplicate:", num)
        break
    seen.add(num)