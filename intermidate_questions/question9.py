# 9. First Non-Repeating Character

# Question: Find the first character in a string that occurs only once.

# Answer:

text = "aabbcdd"


frequency = {}


for char in text:
    frequency[char] = frequency.get(char, 0) + 1


for char in text:
    if frequency[char] == 1:
        print("First non-repeating character:", char)
        break
else:
    print("No non-repeating character")