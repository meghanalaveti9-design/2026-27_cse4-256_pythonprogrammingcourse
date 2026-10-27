
University Scholarship Allocation – Python Program
1. Aim
To develop a Python program that evaluates scholarship applicants based on subject-wise minimum marks, attendance, and family income. The program ranks eligible students and resolves ties using predefined rules.


3. Algorithm
1. Start the program.
2. Enter the number of scholarship applicants.
3. Enter each applicant's name, marks in three subjects, attendance percentage, and annual family income.
4. Check whether the applicant satisfies all eligibility criteria:
   - Minimum 40 marks in each subject.
   - Attendance of at least 75%.
   - Annual family income not exceeding ₹2,00,000.
5. If all conditions are satisfied, mark the applicant as eligible.
6. Calculate the total marks of each eligible applicant.
7. Rank eligible applicants by total marks in descending order.
8. If two applicants have equal total marks, give priority to the applicant with higher attendance. If attendance is also equal, give priority to the applicant with lower family income.
9. Display the eligible applicants in rank order.
10. Stop the program.
3. Python Code
applicants = []n = int(input("Enter number of applicants: "))for i in range(n):    print("\nApplicant", i + 1)    name = input("Enter name: ")    m1 = int(input("Enter marks in Subject 1: "))    m2 = int(input("Enter marks in Subject 2: "))    m3 = int(input("Enter marks in Subject 3: "))    attendance = float(input("Enter attendance percentage: "))    income = float(input("Enter annual family income: "))    total = m1 + m2 + m3    if (m1 >= 40 and m2 >= 40 and m3 >= 40            and attendance >= 75            and income <= 200000):        applicants.append(            (name, total, attendance, income)        )    else:        print(name, "is not eligible for scholarship.")# Sort by total marks, attendance, and incomeapplicants.sort(key=lambda x: (-x[1], -x[2], x[3]))print("\n--- Scholarship Allocation Results ---")if len(applicants) == 0:    print("No eligible applicants found.")else:



4. Pseudocode
START

INPUT number_of_applicants
CREATE empty list applicants

FOR each applicant:
    INPUT name
    INPUT subject1, subject2, subject3
    INPUT attendance
    INPUT family_income

    total = subject1 + subject2 + subject3

    IF subject1 >= 40 AND subject2 >= 40
       AND subject3 >= 40
       AND attendance >= 75
       AND family_income <= 200000 THEN

        ADD applicant details to applicants
    ELSE
        DISPLAY "Not eligible"
    END IF
END FOR

SORT applicants BY:
    total marks DESCENDING
    attendance DESCENDING
    family income ASCENDING

DISPLAY ranked eligible applicants

STOP


5. Flowchart

flowchart TD
    A([START]) --> B[/Enter applicant details, subject marks, attendance and income/]
    B --> C[Calculate total marks]
    C --> D{Each subject >= 40<br/>Attendance >= 75%<br/>Income <= 200000?}
    D -- Yes --> E[Add applicant to eligible list]
    D -- No --> F[Display Not Eligible]
    E --> G{All applicants processed?}
    F --> G
    G -- No --> B
    G -- Yes --> H[Sort by total marks descending]
    H --> I[Break ties using higher attendance]
    I --> J[If still tied, prefer lower family income]
    J --> K[/Display final scholarship ranking/]
    K --> L([STOP])

