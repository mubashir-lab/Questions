# 5. Find All Pairs With a Given Sum

# Question: Given a list and a target value, find all pairs whose sum equals the target.

# Answer:

numbers = [2, 7, 11, 15, 3, 6]
target = 9


seen = set()


for num in numbers:
    complement = target - num


    if complement in seen:
        print(complement, num)


    seen.add(num)