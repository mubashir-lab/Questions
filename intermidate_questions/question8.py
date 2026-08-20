# 8. Check Anagrams

# Question: Determine whether two strings are anagrams of each other.

# Answer:

text1 = input("Enter first string: ").lower()
text2 = input("Enter second string: ").lower()


if sorted(text1) == sorted(text2):
    print("Anagrams")
else:
    print("Not anagrams")