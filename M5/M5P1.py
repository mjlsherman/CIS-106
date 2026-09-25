quantity = int(input("Enter quantity: "))
if quantity >= 1000:
    unit_price = 3.00
else:
    unit_price = 5.00
extended_price = quantity * unit_price
tax = extended_price * 0.07
total = extended_price + tax
print("Quantity:", quantity)
print("Unit price: $", format(unit_price, ".2f"))
print("Extended price: $", format(extended_price, ".2f"))
print("Tax: $", format(tax, ".2f"))
print("Total: $", format(total, ".2f"))
