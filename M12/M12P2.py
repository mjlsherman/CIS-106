def display_forward(names, scores):
    print("Forward Order:")
    for i in range(len(names)):
        print(names[i], "-", scores[i])


def display_reverse(names, scores):
    print("\nReverse Order:")
    for i in range(len(names) - 1, -1, -1):
        print(names[i], "-", scores[i])


def main():
    names = ["Smith", "Johnson", "Williams", "Brown",
             "Jones", "Garcia", "Miller", "Davis",
             "Wilson", "Taylor"]

    scores = [85, 92, 78, 95, 88, 73, 90, 82, 97, 80]

    display_forward(names, scores)
    display_reverse(names, scores)


main()
