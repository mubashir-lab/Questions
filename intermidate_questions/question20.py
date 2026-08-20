# 20. Merge Two Sorted Lists

# Question: Merge two already-sorted lists into one sorted list without using sort().

# Answer:

a = [1, 4, 7, 10]
b = [2, 3, 6, 8]


result = []
i = 0
j = 0


while i < len(a) and j < len(b):
    if a[i] < b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1


result.extend(a[i:])
result.extend(b[j:])


print(result)