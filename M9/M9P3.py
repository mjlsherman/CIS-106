def calculate_mpg(miles, gallons):
    if gallons == 0:
        return 0

    mpg = miles / gallons
    return mpg


trip_count = 0
again = "yes"

while again.lower() == "yes":
    city = input("Enter destination city: ")
    miles = float(input("Enter miles traveled: "))
    gallons = float(input("Enter gallons used: "))

    mpg = calculate_mpg(miles, gallons)

    print("Destination:", city)
    print("Miles Per Gallon:", format(mpg, ".2f"))

    trip_count = trip_count + 1

    again = input("Enter yes to continue or no to stop: ")

print("Total Trips Entered:", trip_count)
