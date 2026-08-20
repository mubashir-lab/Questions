# 27. Find GCD of Two Numbers

# Question: Find the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm.

# Answer:

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


while b != 0:
    a, b = b, a % b


print("GCD:", a)