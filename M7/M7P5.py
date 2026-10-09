total_discounts = 0

answer = input("Do you want to enter an order? (Yes/No): ")

while answer == "Yes" or answer == "yes":

    quantity = int(input("Enter quantity: "))
    price = float(input("Enter item price: "))

    extended_price = quantity * price

    if extended_price > 10000:
        discount_percent = 0.25
    else:
        discount_percent = 0.10

    discount_amount = extended_price * discount_percent
    total = extended_price - discount_amount

    print("Extended price: $", format(extended_price, ".2f"))
    print("Discount amount: $", format(discount_amount, ".2f"))
    print("Total after discount: $", format(total, ".2f"))

    total_discounts = total_discounts + discount_amount

    answer = input("Do you want to enter another order? (Yes/No): ")

print("Sum of all discounts: $", format(total_discounts, ".2f"))
