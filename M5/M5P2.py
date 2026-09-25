item = input("Enter item (A or B): ")
quantity = int(input("Enter quantity: "))
if item == "A":
    unit_price = 10.00
else:
    unit_price = 20.00
extended_price = quantity * unit_price
print("Item:", item)
print("Unit price: $", format(unit_price, ".2f"))
print("Extended price: $", format(extended_price, ".2f"))
