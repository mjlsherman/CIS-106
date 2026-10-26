def calculate_pay(job_code, hours):
    if job_code == "L":
        rate = 25
    elif job_code == "A":
        rate = 30
    elif job_code == "J":
        rate = 50
    else:
        return 0

    if hours > 40:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * rate * 1.5
        gross_pay = regular_pay + overtime_pay
    else:
        gross_pay = hours * rate

    return gross_pay


total_gross_pay = 0
again = "yes"

while again.lower() == "yes":
    last_name = input("Enter employee last name: ")
    job_code = input("Enter job code (L, A, J): ").upper()
    hours = float(input("Enter hours worked: "))

    gross_pay = calculate_pay(job_code, hours)

    print("Employee:", last_name)
    print("Gross Pay: $", format(gross_pay, ".2f"))

    total_gross_pay = total_gross_pay + gross_pay

    again = input("Enter yes to continue or no to stop: ")

print("Total Gross Pay: $", format(total_gross_pay, ".2f"))
