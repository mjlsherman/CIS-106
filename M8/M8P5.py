file = open("students.txt", "r")

total_tuition = 0

print("Student       Credits      Tuition")

for i in range(5):
    name = file.readline().strip()
    district = int(file.readline())
    credits = int(file.readline())

    if district == 1:
        rate = 200
    else:
        rate = 500

    tuition = credits * rate
    total_tuition += tuition

    print(f"{name:<13} {credits:<12} ${tuition:,.2f}")

file.close()

print()
print(f"Total tuition owed: ${total_tuition:,.2f}")
