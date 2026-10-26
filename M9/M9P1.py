def calculate_total(quantity, price):
    total = quantity * price

    if total > 10000:
        total = total * 0.90

    return total


grand_total = 0
again = "yes"

while again.lower() == "yes":
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter unit price: "))

    total = calculate_total(quantity, price)

    print("Quantity:", quantity)
    print("Unit Price: $", format(price, ".2f"))
    print("Extended Price: $", format(total, ".2f"))

    grand_total = grand_total + total

    again = input("Enter yes to continue or no to stop: ")

print("Grand Total: $", format(grand_total, ".2f"))
