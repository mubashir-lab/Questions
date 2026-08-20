# 4. Find the Largest of Three Numbers

# Question: Write a program to find the largest among three numbers.

# Answer:

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))


if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)