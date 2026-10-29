def calculate_forecast(month, sales):
    if month in [1, 2, 3]:
        percent = 0.10
    elif month in [4, 5, 6]:
        percent = 0.15
    elif month in [7, 8, 9]:
        percent = 0.20
    else:
        percent = 0.25

    forecast = sales * (1 + percent)
    return forecast


again = "Yes"

while again.lower() == "yes":
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    sales = float(input("Enter last month's sales: $"))
    month = int(input("Enter month number (1-12): "))

    if 1 <= month <= 12:
        forecast = calculate_forecast(month, sales)

        print("Car:", make, model)
        print(f"Next month's forecast: ${forecast:,.2f}")
    else:
        print("Invalid month.")

    again = input("Run again? (Yes or No): ")
