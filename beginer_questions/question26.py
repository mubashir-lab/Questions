# 26. Linear Search

# Question: Search for a given value in a list using linear search.

# Answer:

numbers = [10, 20, 30, 40, 50]


target = int(input("Enter value to search: "))


found = False


for i in range(len(numbers)):
    if numbers[i] == target:
        print("Found at index", i)
        found = True
        break


if not found:
    print("Value not found")