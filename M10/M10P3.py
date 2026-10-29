def calculate_door_price(msrp, make, model, electric):
    if electric.lower() == "yes":
        discount = 0.30
    elif make.lower() == "honda" and model.lower() == "accord":
        discount = 0.10
    elif make.lower() == "toyota" and model.lower() == "rav4":
        discount = 0.15
    else:
        discount = 0.05

    discount_amount = msrp * discount
    discounted_price = msrp - discount_amount
    tax = discounted_price * 0.07
    door_price = discounted_price + tax

    return door_price, discount_amount


total_msrp = 0
total_discounts = 0
total_sales = 0

again = "Yes"

while again.lower() == "yes":
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    electric = input("Is it electric? (Yes or No): ")
    msrp = float(input("Enter MSRP: $"))

    price, discount = calculate_door_price(
        msrp, make, model, electric
    )

    total_msrp += msrp
    total_discounts += discount
    total_sales += price

    print(f"Door price: ${price:,.2f}")

    again = input("Run again? (Yes or No): ")

print(f"Total MSRP: ${total_msrp:,.2f}")
print(f"Total discounts: ${total_discounts:,.2f}")
print(f"Total sales prices: ${total_sales:,.2f}")
