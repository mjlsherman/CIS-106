def print_grades(students):
    print("Student Name\tGrade")
    print("----------------------")

    for name, grade in students.items():
        print(f"{name:<15}{grade}")


students = {
    "John": 92,
    "Sarah": 85,
    "Mike": 78,
    "Emily": 96,
    "David": 88
}

print_grades(students)
