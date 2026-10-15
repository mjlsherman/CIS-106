tickets = int(input("Enter number of concert tickets: "))
if tickets >= 25:
    price = 50.00
elif tickets >= 10:
    price = 60.00
elif tickets >= 5:
    price = 70.00
else:
    price = 75.00
total_cost = tickets * price
print("Number of Tickets:", tickets)
print("Price Per Ticket: $", format(price, ".2f"))
print("Total Cost:       $", format(total_cost, ".2f"))
