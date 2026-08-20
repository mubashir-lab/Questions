# 6. Rotate a List

# Question: Rotate a list to the right by k positions.

# Answer:

numbers = [1, 2, 3, 4, 5]
k = 2


k = k % len(numbers)


result = numbers[-k:] + numbers[:-k]


print(result)