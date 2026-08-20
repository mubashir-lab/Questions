# 24. Find Equilibrium Index

# Question: Find an index where the sum of elements on the left equals the sum of elements on the right.

# Answer:

numbers = [1, 3, 5, 2, 2]


total = sum(numbers)
left_sum = 0


for i in range(len(numbers)):
    total -= numbers[i]


    if left_sum == total:
        print("Equilibrium index:", i)
        break


    left_sum += numbers[i]
else:
    print("No equilibrium index")