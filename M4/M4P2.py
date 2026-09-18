purchase_price = float(input("Enter purchase price per share: $"))
current_price = float(input("Enter current price per share: $"))
quantity = int(input("Enter number of shares: "))
gain_loss = (current_price - purchase_price) * quantity
print("Total gain or loss: $", format(gain_loss, ".2f"))
