def calculate_scores(score1, score2, score3):
    total = score1 + score2 + score3
    average = total / 3
    return total, average


def main():
    last_name = input("Enter student's last name: ")
    score1 = float(input("Enter exam 1 score: "))
    score2 = float(input("Enter exam 2 score: "))
    score3 = float(input("Enter exam 3 score: "))

    total, average = calculate_scores(
        score1, score2, score3
    )

    print("Student:", last_name)
    print("Total points:", format(total, ".2f"))
    print("Average score:", format(average, ".2f"))


main()
