# 16. Find Maximum in a List

# Question: Find the largest element in a list without using max().

# Answer:

numbers = [12, 45, 7, 89, 23, 56]


largest = numbers[0]


for num in numbers:
    if num > largest:
        largest = num


print("Largest =", largest)