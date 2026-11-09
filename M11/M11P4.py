def calculate_bowling(score1, score2, score3, handicap):
    average = (score1 + score2 + score3) / 3
    average_with_handicap = average + handicap
    return average, average_with_handicap


def main():
    last_name = input("Enter bowler's last name: ")
    score1 = int(input("Enter game 1 score: "))
    score2 = int(input("Enter game 2 score: "))
    score3 = int(input("Enter game 3 score: "))
    handicap = int(input("Enter handicap: "))

    average, adjusted_average = calculate_bowling(
        score1, score2, score3, handicap
    )

    print("Bowler:", last_name)
    print("Average score:", format(average, ".2f"))
    print("Average with handicap:", format(adjusted_average, ".2f"))


main()
