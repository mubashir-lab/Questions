# 19. Count Even and Odd Numbers

# Question: Count how many even and odd numbers exist in a list.

# Answer:

numbers = [10, 15, 22, 31, 44, 57, 60]


even = 0
odd = 0


for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1


print("Even numbers =", even)
print("Odd numbers =", odd)