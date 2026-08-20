# 11. Longest Word in a Sentence

# Question: Find the longest word in a sentence.

# Answer:

sentence = "Python programming is interesting"


words = sentence.split()


longest = words[0]


for word in words:
    if len(word) > len(longest):
        longest = word


print("Longest word:", longest)