import math


def wall_area(length, width, height):
    return 2 * length * height + 2 * width * height


def ceiling_area(length, width):
    return length * width


def gallons_needed(area):
    return math.ceil(area / 50)


again = "Yes"

while again.lower() == "yes":
    length = float(input("Enter room length: "))
    width = float(input("Enter room width: "))
    height = float(input("Enter room height: "))

    walls = wall_area(length, width, height)
    wall_gallons = gallons_needed(walls)

    ceiling = ceiling_area(length, width)
    ceiling_gallons = gallons_needed(ceiling)

    print(f"Wall area: {walls:.2f} square feet")
    print("Wall paint gallons:", wall_gallons)

    print(f"Ceiling area: {ceiling:.2f} square feet")
    print("Ceiling paint gallons:", ceiling_gallons)

    again = input("Run again? (Yes or No): ")
