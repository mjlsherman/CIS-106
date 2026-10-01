quantity = int(input("Enter quantity of widgets: "))
if quantity > 10000:
    price = 10.00
elif quantity >= 5000:
    price = 20.00
else:
    price = 30.00
extended_price = quantity * price
tax_amount = extended_price * 0.07
total = extended_price + tax_amount
print("Quantity:       ", quantity)
print("Price:          $", format(price, ".2f"))
print("Extended Price: $", format(extended_price, ".2f"))
print("Tax Amount:     $", format(tax_amount, ".2f"))
print("Total:          $", format(total, ".2f"))
