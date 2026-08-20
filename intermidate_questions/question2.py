# 2. Move All Zeros to the End

# Question: Move all zeros in a list to the end while maintaining the order of the other elements.

# Answer:

numbers = [0, 1, 0, 3, 12, 0, 5]


result = []
zero_count = 0


for num in numbers:
    if num == 0:
        zero_count += 1
    else:
        result.append(num)


result.extend([0] * zero_count)

print(result)