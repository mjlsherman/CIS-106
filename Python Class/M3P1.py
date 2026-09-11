stock_symbol = input("Enter the stock ticker symbol: ")
number_of_shares = int(input("Enter the number of shares: "))
cost_per_share = float(input("Enter the cost per share: "))
amount_invested = number_of_shares * cost_per_share
print("Stock:", stock_symbol)
print("Amount invested: $", format(amount_invested, ".2f"))
