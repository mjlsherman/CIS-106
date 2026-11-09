def calculate_total(quantity, unit_price):
    total_price = quantity * unit_price
    tax = total_price * 0.07
    return total_price, tax


def main():
    quantity = int(input("Enter quantity: "))
    unit_price = float(input("Enter unit price: "))

    total, tax = calculate_total(quantity, unit_price)

    print("Total price: $", format(total, ".2f"))
    print("Sales tax: $", format(tax, ".2f"))


main()
