
total_pay = 0
count = 0

answer = input("Do you want to enter an employee? (Yes/No): ")

while answer == "Yes" or answer == "yes":

    last_name = input("Enter employee's last name: ")
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter hourly pay rate: "))

    if hours > 40:
        overtime = hours - 40
        gross_pay = (40 * rate) + (overtime * rate * 1.5)
    else:
        gross_pay = hours * rate

    print("Employee:", last_name)
    print("Gross pay: $", format(gross_pay, ".2f"))

    total_pay = total_pay + gross_pay
    count = count + 1

    answer = input("Do you want to enter another employee? (Yes/No): ")

print("Total gross pay: $", format(total_pay, ".2f"))
print("Number of employees:", count)

if count > 0:
    average_pay = total_pay / count
    print("Average pay: $", format(average_pay, ".2f"))
