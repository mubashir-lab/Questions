# 27. Bubble Sort

# Question: Sort a list in ascending order using Bubble Sort.

# Answer:

numbers = [64, 34, 25, 12, 22, 11, 90]


for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


print("Sorted list:", numbers)