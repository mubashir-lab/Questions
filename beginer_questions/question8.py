# 8. Sum of Natural Numbers

# Question: Calculate the sum of the first n natural numbers.

# Answer:

n = int(input("Enter n: "))


total = 0


for i in range(1, n + 1):
    total += i


print("Sum =", total)