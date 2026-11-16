def display_forward(names):
    print("Names in forward order:")
    for i in range(len(names)):
        print(names[i])


def display_reverse(names):
    print("\nNames in reverse order:")
    for i in range(len(names) - 1, -1, -1):
        print(names[i])


def main():
    names = ["Smith", "Johnson", "Williams", "Brown",
             "Jones", "Garcia", "Miller", "Davis",
             "Wilson", "Taylor"]

    display_forward(names)
    display_reverse(names)


main()
