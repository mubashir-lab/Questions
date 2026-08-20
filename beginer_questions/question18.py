# 18. Calculate Average

# Question: Calculate the average of numbers stored in a list.

# Answer:

numbers = [10, 20, 30, 40, 50]


total = 0


for num in numbers:
    total += num


average = total / len(numbers)


print("Average =", average)