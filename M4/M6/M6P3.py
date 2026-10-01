principal = float(input("Enter principal amount: "))
years = int(input("Enter years to maturity: "))
if principal > 100000 and years == 5:
    interest_rate = 0.06
elif principal >= 50000 and principal <= 100000 and years == 10:
    interest_rate = 0.05
elif principal >= 50000 and principal <= 100000 and years == 5:
    interest_rate = 0.04
else:
    interest_rate = 0.02
interest_amount = principal * interest_rate
print("Principal:       $", format(principal, ".2f"))
print("Interest Rate:   ", format(interest_rate * 100, ".2f"), "%")
print("Interest Amount: $", format(interest_amount, ".2f"))
