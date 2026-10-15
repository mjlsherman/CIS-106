principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate: "))

print()
print("Year    Beginning Balance    Ending Balance")

balance = principal

for year in range(1, 6):
    beginning = balance
    interest = beginning * rate
    balance = beginning + interest

    print(f"{year:<8}${beginning:,.2f}          ${balance:,.2f}")

total_interest = balance - principal

print()
print(f"Total interest earned: ${total_interest:,.2f}")
