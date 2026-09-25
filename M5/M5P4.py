part_number = int(input("Enter part number: "))
quantity = int(input("Enter quantity: "))
if part_number == 10:
    unit_price = 1.00
elif part_number == 55:
    unit_price = 3.00
elif part_number == 99:
    unit_price = 2.00
elif part_number == 80:
    unit_price = 5.00
else:
    unit_price = 2.00
extended_price = quantity * unit_price
print("Part number:", part_number)
print("Unit price: $", format(unit_price, ".2f"))
print("Extended price: $", format(extended_price, ".2f"))
