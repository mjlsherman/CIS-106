def find_highest(names, scores):
    high_var = 0
    high_name = ""

    for i in range(len(scores)):
        if scores[i] > high_var:
            high_var = scores[i]
            high_name = names[i]

    print("Highest Score:", high_var)
    print("Student:", high_name)


def find_lowest(names, scores):
    low_var = 999
    low_name = ""

    for i in range(len(scores)):
        if scores[i] < low_var:
            low_var = scores[i]
            low_name = names[i]

    print("Lowest Score:", low_var)
    print("Student:", low_name)


def main():
    names = ["Smith", "Johnson", "Williams", "Brown",
             "Jones", "Garcia", "Miller", "Davis",
             "Wilson", "Taylor"]

    scores = [85, 92, 78, 95, 88, 73, 90, 82, 97, 80]

    find_highest(names, scores)
    print()
    find_lowest(names, scores)


main()
