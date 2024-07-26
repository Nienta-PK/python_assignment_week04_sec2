grades = [55, 70, 65, 40, 90, 85, 50, 77]
passed_with_bonus = [round(score*1.05,2) for score in grades if score>=60 ]
print(passed_with_bonus)