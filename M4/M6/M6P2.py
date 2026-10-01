part = input("Enter part number: ")
quantity = int(input("Enter quantity: "))
if part == "10" or part == "55":
    unit_cost = 1.00
elif part == "99":
    unit_cost = 2.00
elif part == "80" or part == "70":
    unit_cost = 3.00
else:
    unit_cost = 5.00
total_cost = quantity * unit_cost
print("Part Number: ", part)
print("Unit Cost:   $", format(unit_cost, ".2f"))
print("Total Cost:  $", format(total_cost, ".2f"))
