file = open("employees.txt", "r")

total_bonuses = 0

print("Employee       Salary       Bonus")

for i in range(5):
    name = file.readline().strip()
    salary = float(file.readline())

    if salary >= 100000:
        rate = 0.20
    elif salary >= 50000:
        rate = 0.15
    else:
        rate = 0.10

    bonus = salary * rate
    total_bonuses += bonus

    print(f"{name:<12} ${salary:,.2f}    ${bonus:,.2f}")

file.close()

print()
print(f"Total bonuses paid: ${total_bonuses:,.2f}")
