def calculate_assessed_value(county, market_value):
    county = county.lower()

    if county == "cook":
        percent = 0.90
    elif county == "dupage":
        percent = 0.80
    elif county == "mchenry":
        percent = 0.75
    elif county == "kane":
        percent = 0.60
    else:
        percent = 0.70

    assessed_value = market_value * percent
    return assessed_value


total_market = 0
total_assessed = 0

again = "Yes"

while again.lower() == "yes":
    county = input("Enter county: ")
    market_value = float(input("Enter market value: $"))

    assessed = calculate_assessed_value(
        county, market_value
    )

    total_market += market_value
    total_assessed += assessed

    print(f"Market value: ${market_value:,.2f}")
    print(f"Assessed value: ${assessed:,.2f}")

    again = input("Run again? (Yes or No): ")

print(f"Total market value: ${total_market:,.2f}")
print(f"Total assessed value: ${total_assessed:,.2f}")
