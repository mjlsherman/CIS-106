def calculate_average(grades):
    return sum(grades) / len(grades)


def print_grades(students):
    print("Student Name\tAverage")
    print("--------------------------")

    for name, grades in students.items():
        average = calculate_average(grades)
        print(f"{name:<15}{average:.2f}")

    print("\nClass Averages:")

    for i in range(3):
        total = 0

        for grades in students.values():
            total += grades[i]

        class_average = total / len(students)
        print(f"Grade {i + 1}: {class_average:.2f}")


students = {
    "John": [90, 85, 95],
    "Sarah": [88, 92, 84],
    "Mike": [75, 80, 85],
    "Emily": [95, 98, 92],
    "David": [82, 88, 90]
}

print_grades(students)
