# 17. Binary Search

# Question: Implement binary search to find an element in a sorted list.

# Answer:

numbers = [10, 20, 30, 40, 50, 60, 70]
target = 50


left = 0
right = len(numbers) - 1


found = False


while left <= right:
    middle = (left + right) // 2


    if numbers[middle] == target:
        print("Found at index:", middle)
        found = True
        break
    elif numbers[middle] < target:
        left = middle + 1
    else:
        right = middle - 1


if not found:
    print("Not found")