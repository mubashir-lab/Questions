# 14. Check Balanced Parentheses

# Question: Determine whether parentheses in a string are balanced.

# Answer:

expression = input("Enter expression: ")


balance = 0


for char in expression:
    if char == "(":
        balance += 1
    elif char == ")":
        balance -= 1


    if balance < 0:
        break


if balance == 0:
    print("Balanced")
else:
    print("Not balanced")