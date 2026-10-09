count = 0

answer = input("Do you want to enter a student? (Yes/No): ")

while answer == "Yes" or answer == "yes":

    last_name = input("Enter student's last name: ")
    exam1 = float(input("Enter first exam score: "))
    exam2 = float(input("Enter second exam score: "))

    average = (exam1 + exam2) / 2

    print("Student:", last_name)
    print("Average exam score:", format(average, ".2f"))

    count = count + 1

    answer = input("Do you want to enter another student? (Yes/No): ")

print("Total number of students:", count)
