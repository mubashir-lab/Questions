# 10. Character Frequency

# Question: Count the frequency of every character in a string.

# Answer:

text = "programming"


frequency = {}


for char in text:
    frequency[char] = frequency.get(char, 0) + 1


print(frequency)