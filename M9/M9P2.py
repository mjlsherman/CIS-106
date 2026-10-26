def calculate_average(hits, at_bats):
    if at_bats == 0:
        return 0

    average = hits / at_bats
    return average


player_count = 0
again = "yes"

while again.lower() == "yes":
    last_name = input("Enter player's last name: ")
    hits = int(input("Enter number of hits: "))
    at_bats = int(input("Enter number of at bats: "))

    average = calculate_average(hits, at_bats)

    print("Player:", last_name)
    print("Batting Average:", format(average, ".3f"))

    player_count = player_count + 1

    again = input("Enter yes to continue or no to stop: ")

print("Total Players Entered:", player_count)
