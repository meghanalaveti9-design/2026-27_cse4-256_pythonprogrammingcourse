

applicants = []

n = int(input("Enter number of applicants: "))

for i in range(n):
    print("\nApplicant", i + 1)

    name = input("Enter name: ")
    m1 = int(input("Enter marks in Subject 1: "))
    m2 = int(input("Enter marks in Subject 2: "))
    m3 = int(input("Enter marks in Subject 3: "))
    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    total = m1 + m2 + m3

    if (m1 >= 40 and m2 >= 40 and m3 >= 40
            and attendance >= 75
            and income <= 200000):

        applicants.append(
            (name, total, attendance, income)
        )

    else:
        print(name, "is not eligible for scholarship.")
applicants.sort(key=lambda x: (-x[1], -x[2], x[3]))

print("\n--- Scholarship Allocation Results ---")

if len(applicants) == 0:
    print("No eligible applicants found.")
else:
    for rank, student in enumerate(applicants, start=1):
        print("Rank:", rank)
        print("Name:", student[0])
        print("Total Marks:", student[1])
        print("Attendance:", student[2], "%")
        print("Family Income: Rs.", student[3])
        print("------------------------")
