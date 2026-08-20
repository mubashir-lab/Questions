# 13. Word Frequency Counter

# Question: Count how many times each word appears in a sentence.

# Answer:

sentence = "python is easy and python is powerful"


words = sentence.lower().split()


frequency = {}


for word in words:
    frequency[word] = frequency.get(word, 0) + 1


print(frequency)