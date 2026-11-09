def calculate_discount(quantity, price, discount_rate):
    total = quantity * price
    discount_amount = total * (discount_rate / 100)
    discounted_price = total - discount_amount
    return discount_amount, discounted_price


def main():
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))
    discount_rate = float(input("Enter discount rate (%): "))

    discount, final_price = calculate_discount(
        quantity, price, discount_rate
    )

    print("Discount amount: $", format(discount, ".2f"))
    print("Discounted price: $", format(final_price, ".2f"))


main()
