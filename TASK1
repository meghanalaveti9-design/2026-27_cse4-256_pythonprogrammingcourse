subjects = ["Python", "Mathematics", "English", "Physics"]
exam1 = []
exam2 = []

for subject in subjects:
    mark1 = float(input("Enter " + subject + " mark in Exam 1: "))
    mark2 = float(input("Enter " + subject + " mark in Exam 2: "))
    if mark1 < 0 or mark1 > 100 or mark2 < 0 or mark2 > 100:
        print("Invalid marks. Enter marks from 0 to 100.")
        raise SystemExit
    exam1.append(mark1)
    exam2.append(mark2)

print("\nSTUDENT PERFORMANCE REPORT")
total = 0
weak_subjects = []

for i in range(len(subjects)):
    change = exam2[i] - exam1[i]
    total += exam2[i]
    if change > 0:
        trend = "Improved"
    elif change < 0:
        trend = "Declined"
    else:
        trend = "No change"
    print(subjects[i], ":", trend, "(" + str(change) + " marks )")
    if exam2[i] < 40:
        weak_subjects.append(subjects[i])

average = total / len(subjects)
print("Latest average:", round(average, 2))
print("Weak subjects:", weak_subjects if weak_subjects else "None")

if average >= 85:
    print("Performance: Excellent")
elif average >= 70:
    print("Performance: Good")
else:
    print("Performance: Needs Improvement")
