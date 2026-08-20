# 15. Sum of Digits

# Question: Find the sum of all digits of a number.

# Answer:

num = int(input("Enter a number: "))
num = abs(num)


total = 0


while num > 0:
    total += num % 10
    num //= 10


print("Sum of digits =", total)