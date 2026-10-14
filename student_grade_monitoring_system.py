grades = [97, 69, 67, 65, 87]

while True:
    print("STUDENT GRADE MONITORING SYSTEM")
    print("----------------------------------------")
    print("[1] View Grades")
    print("[2] Add Grade")
    print("[3] Classify Grades")
    print("[4] Generate Summary")
    print("[5] Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("STUDENT GRADES")
        print("----------------")
        for i, grade in enumerate(grades, start=1):
            print(f"Student {i}: {grade}")

    elif choice == "2":
        try:
            new_grade = int(input("Enter grade (0-100): "))

            if 0 <= new_grade <= 100:
                grades.append(new_grade)
                print("Grade added successfully!")
            else:
                print("Invalid grade. Enter a value from 0 to 100.")

        except ValueError:
            print("Invalid input. Please enter a valid character.")

    elif choice == "3":
        print("CLASSIFIED GRADES")
        print("-------------------")

        for grade in grades:
            if grade >= 90:
                status = "EXCELLENT"
            elif grade >= 75:
                status = "PASSED"
            else:
                status = "FAILED"

            print(f"{grade:g} : {status}")

    elif choice == "4":
        if not grades:
            print("No grades available.")
            continue

        total = sum(grades)
        count = len(grades)
        average = total / count
        minimum = min(grades)
        maximum = max(grades)

        excellent = sum(1 for g in grades if g >= 90)
        passed = sum(1 for g in grades if 75 <= g < 90)
        failed = sum(1 for g in grades if g < 75)

        print("GRADE SUMMARY")
        print("------------------")
        print(f"Number of grades : {count}")
        print(f"Total grades     : {total:g}")
        print(f"Average grade    : {average:.2f}")
        print(f"Lowest grade     : {minimum:g}")
        print(f"Highest grade    : {maximum:g}")

        print(f"EXCELLENT: {excellent} ({excellent/count*100:.2f}%)")
        print(f"PASSED   : {passed} ({passed/count*100:.2f}%)")
        print(f"FAILED   : {failed} ({failed/count*100:.2f}%)")

        if failed > 0:
            overall = "NEEDS IMPROVEMENT"
        elif passed > 0:
            overall = "SATISFACTORY"
        else:
            overall = "EXCELLENT"

        print(f"Overall Status: {overall}")

    elif choice == "5":
        print("Thank you for using the Student Grade Monitoring System.")
        break

    else:
        print("Invalid choice. Please try again.")