# 30. Student Grade Management

# Question: Create a program that stores student names and marks, calculates their average, and displays their grade.

# Answer:

students = {
    "Ali": [80, 75, 90],
    "Ahmed": [65, 70, 68],
    "Sara": [92, 88, 95]
}


for name, marks in students.items():
    average = sum(marks) / len(marks)


    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"


    print(name)
    print("Average:", average)
    print("Grade:", grade)
    print()