
last_name = input("Enter last name: ")
dependents = int(input("Enter number of dependents: "))
gross_income = float(input("Enter gross income: "))
adjusted_gross_income = gross_income - (dependents * 12000)
if adjusted_gross_income > 50000:
    tax_rate = 0.20
else:
    tax_rate = 0.10
income_tax = adjusted_gross_income * tax_rate
if income_tax < 100:
    income_tax = 100
print("Last name:", last_name)
print("Gross income: $", format(gross_income, ".2f"))
print("Number of dependents:", dependents)
print("Adjusted gross income: $", format(adjusted_gross_income, ".2f"))
print("Income tax: $", format(income_tax, ".2f"))
