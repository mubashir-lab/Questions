# 21. Reverse a String

# Question: Reverse a string without using a built-in reverse function.

# Answer:

text = input("Enter a string: ")


reverse = ""


for char in text:
    reverse = char + reverse


print("Reversed:", reverse)