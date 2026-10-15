file = open("orders.txt", "r")

total_price = 0
order_count = 0

print("Item         Quantity    Price    Extended Price")

for i in range(5):
    item = file.readline().strip()
    quantity = int(file.readline())
    price = float(file.readline())

    extended_price = quantity * price

    total_price += extended_price
    order_count += 1

    print(f"{item:<12} {quantity:<11} ${price:,.2f}    ${extended_price:,.2f}")

file.close()

average_order = total_price / order_count

print()
print(f"Total extended price: ${total_price:,.2f}")
print(f"Number of orders: {order_count}")
print(f"Average order: ${average_order:,.2f}")
