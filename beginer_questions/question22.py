# 22. Check Palindrome String

# Question: Check whether a string is a palindrome.

# Answer:

text = input("Enter a string: ")


reverse = text[::-1]


if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")