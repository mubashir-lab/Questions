# 9. Reverse a Number

# Question: Write a program to reverse a given integer.

# Answer:

num = int(input("Enter a number: "))


reverse = 0


while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10


print("Reversed =", reverse)