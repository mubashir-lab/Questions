# 3. Find Missing Number

# Question: A list contains numbers from 1 to n, but one number is missing. Find the missing number.

# Answer:

numbers = [1, 2, 3, 5, 6]


n = 6


expected = n * (n + 1) // 2
actual = sum(numbers)


print("Missing number:", expected - actual)