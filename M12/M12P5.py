def display_players(names, averages):
    print("Player Batting Averages:")
    for i in range(len(names)):
        print(names[i], "-", averages[i])


def search_player(names, averages):
    again = "yes"

    while again == "yes":
        search_name = input("\nEnter player last name: ")
        found = False

        for i in range(len(names)):
            if names[i].lower() == search_name.lower():
                print("Player:", names[i])
                print("Batting Average:", averages[i])
                found = True

        if found == False:
            print("Name not found")

        again = input("Search again? (yes/no): ").lower()


def main():
    names = []
    averages = []

    file = open("players.txt", "r")

    for i in range(10):
        name = file.readline().strip()
        average = float(file.readline())

        names.append(name)
        averages.append(average)

    file.close()

    display_players(names, averages)
    search_player(names, averages)


main()
