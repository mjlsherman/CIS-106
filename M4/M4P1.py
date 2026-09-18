exam1 = float(input("Enter first exam score: "))
exam2 = float(input("Enter second exam score: "))
weighted_exam1 = exam1 * 0.60
weighted_exam2 = exam2 * 0.40
total_score = weighted_exam1 + weighted_exam2
print("Final weighted score:", format(total_score, ".2f"))
