# 6. Calculate Factorial

# Question: Write a program to calculate the factorial of a number.

# Answer:

num = int(input("Enter a number: "))


factorial = 1


for i in range(1, num + 1):
    factorial *= i


print("Factorial =", factorial)