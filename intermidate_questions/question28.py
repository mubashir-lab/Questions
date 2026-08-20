# 28. Convert Decimal to Binary

# Question: Convert a decimal number to binary without using Python's bin() function.

# Answer:

num = int(input("Enter decimal number: "))


if num == 0:
    print("Binary: 0")
else:
    binary = ""


    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num //= 2


    print("Binary:", binary)