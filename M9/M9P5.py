def calculate_tuition(credit_hours, district_code):
    if district_code == "I":
        rate = 250
    elif district_code == "O":
        rate = 550
    else:
        return 0

    tuition = credit_hours * rate
    return tuition


total_tuition = 0
again = "yes"

while again.lower() == "yes":
    last_name = input("Enter student last name: ")
    credit_hours = int(input("Enter credit hours: "))
    district_code = input("Enter district code (I or O): ").upper()

    tuition = calculate_tuition(credit_hours, district_code)

    print("Student:", last_name)
    print("Tuition Owed: $", format(tuition, ".2f"))

    total_tuition = total_tuition + tuition

    again = input("Enter yes to continue or no to stop: ")

print("Total Tuition Owed: $", format(total_tuition, ".2f"))
