# 23. Find Leaders in an Array

# Question: An element is a leader if it is greater than every element to its right. Find all leaders.

# Answer:

numbers = [16, 17, 4, 3, 5, 2]


leaders = []


maximum = numbers[-1]
leaders.append(maximum)


for i in range(len(numbers) - 2, -1, -1):
    if numbers[i] > maximum:
        maximum = numbers[i]
        leaders.append(maximum)


leaders.reverse()


print("Leaders:", leaders)