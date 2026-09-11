
last_name = input("Enter your last name: ")
midterm_score = float(input("Enter your midterm exam score: "))
final_score = float(input("Enter your final exam score: "))
total_exam_points = (midterm_score * 0.40) + (final_score * 0.60)
print("Student last name:", last_name)
print("Total exam points:", format(total_exam_points, ".2f"))
