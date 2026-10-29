def calculate_ticket(miles):
    if miles >= 30:
        price = 12
    elif miles >= 20:
        price = 10
    elif miles >= 10:
        price = 8
    else:
        price = 5

    return price


total_tickets = 0
again = "Yes"

while again.lower() == "yes":
    last_name = input("Enter last name: ")
    miles = float(input("Enter miles driven: "))

    ticket = calculate_ticket(miles)
    total_tickets += ticket

    print("Driver:", last_name)
    print(f"Ticket price: ${ticket:.2f}")

    again = input("Run again? (Yes or No): ")

print(f"Total ticket prices: ${total_tickets:.2f}")
