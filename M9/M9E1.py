def calculate_rewards(points, code):
    if code == "C":
        rewards = points * 2
    elif code == "S":
        rewards = points * 3
    else:
        rewards = points

    return rewards


points = int(input("Enter number of points: "))
code = input("Enter redemption code: ").upper()

rewards = calculate_rewards(points, code)

print("Original Points:", points)
print("Redemption Code:", code)
print("Reward Points:", rewards)
