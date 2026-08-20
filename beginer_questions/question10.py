# 10. Check Palindrome Number

# Question: Check whether a number reads the same forward and backward.

# Answer:

num = int(input("Enter a number: "))


original = num
reverse = 0


while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10


if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")