# 12. Remove Duplicate Characters

# Question: Remove duplicate characters from a string while maintaining their original order.

# Answer:

text = "programming"


result = ""


for char in text:
    if char not in result:
        result += char


print(result)