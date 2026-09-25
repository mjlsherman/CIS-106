number_of_books = int(input("Enter number of books: "))
cost_per_book = float(input("Enter cost per book: "))
order_total = number_of_books * cost_per_book
if order_total > 50:
    shipping = 0
else:
    shipping = 25
total = order_total + shipping
print("Order total: $", format(order_total, ".2f"))
print("Shipping charge: $", format(shipping, ".2f"))
print("Total: $", format(total, ".2f"))
