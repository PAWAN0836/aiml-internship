import numpy as np


students = [
    {"name": "Rahul", "marks": 80},
    {"name": "Priya", "marks": 75},
    {"name": "Aman", "marks": 90},
    {"name": "Sneha", "marks": 85}
]


def calculate_average(students):
    marks = [student["marks"] for student in students]
    return sum(marks) / len(marks)


# Extract marks
marks = [student["marks"] for student in students]

# NumPy mean
mean_marks = np.mean(marks)

# Function average
average_marks = calculate_average(students)


print("===== STUDENT DATA =====")
print(f"{'Name':<15}{'Marks':<10}")
print("-" * 25)

for student in students:
    print(f"{student['name']:<15}{student['marks']:<10}")

print("-" * 25)

print("Average Marks :", average_marks)
print("NumPy Mean    :", mean_marks)