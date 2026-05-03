import json
import numpy as np
import matplotlib.pyplot as plt

try:
    with open("ogrenciler.json", "r") as file:
        students = json.load(file)
except FileNotFoundError:
    students = {}

def save():
    with open("ogrenciler.json", "w") as file:
        json.dump(students, file, indent=4)

while True:
    print("\n===== Student Performance System =====")
    print("1) Add Student")
    print("2) Add Grade")
    print("3) List Students")
    print("4) Detailed Analysis")
    print("5) Top Student")
    print("6) Exit")
    print("7) Delete Student")
    print("8) Show Chart")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")

        if name in students:
            print("A student with this name is already registered.")
        else:
            students[name] = []
            save()
            print(f"Student named {name} has been successfully added.")

    elif choice == "2":
        name = input("Enter the name of the student to add a grade: ")

        if name in students:
            try:
                grade = int(input("Enter grade (0-100): "))

                if 0 <= grade <= 100:
                    students[name].append(grade)
                    save()
                    print(f"Grade has been successfully added for {name}.")
                else:
                    print("Grade must be between 0 and 100.")

            except:
                print("Invalid input. Please enter a numeric value.")
        else:
            print("No student found with the given name.")

    elif choice == "3":
        if len(students) == 0:
            print("There are no students registered in the system.")
        else:
            print("\n--- Student List ---")
            for name, grades in students.items():
                print(f"{name} -> Grades: {grades}")

    elif choice == "4":
        if len(students) == 0:
            print("No data available for analysis.")
        else:
            print("\n--- Detailed Analysis Results ---")

            all_grades = []

            for name, grades in students.items():
                if len(grades) == 0:
                    print(f"{name} -> No grades entered yet.")
                else:
                    average = np.mean(grades)
                    highest = np.max(grades)
                    lowest = np.min(grades)
                    std = np.std(grades)

                    status = "Passed" if average >= 50 else "Failed"

                    print(f"{name} -> Average: {round(average,2)} | Highest: {highest} | Lowest: {lowest} | Std: {round(std,2)} | Status: {status}")

                    all_grades.extend(grades)

            if len(all_grades) > 0:
                overall_average = np.mean(all_grades)
                print(f"\nClass Average: {round(overall_average,2)}")

    elif choice == "5":
        best = ""
        highest_avg = 0

        for name, grades in students.items():
            if len(grades) > 0:
                average = np.mean(grades)

                if average > highest_avg:
                    highest_avg = average
                    best = name

        if best == "":
            print("Not enough data to evaluate.")
        else:
            print("\n--- Top Student ---")
            print(f"Student: {best}")
            print(f"Average: {round(highest_avg,2)}")

    elif choice == "6":
        print("Exited.")
        break

    elif choice == "7":
        name = input("Enter the name of the student to delete: ")

        if name in students:
            del students[name]
            save()
            print(f"Student named {name} has been deleted from the system.")
        else:
            print("No student found with the given name.")

    elif choice == "8":
        names = []
        averages = []

        for name, grades in students.items():
            if len(grades) > 0:
                names.append(name)
                averages.append(np.mean(grades))

        if len(names) == 0:
            print("Not enough data to create a chart.")
        else:
            plt.figure()
            plt.bar(names, averages)
            plt.title("Student Average Grades")
            plt.xlabel("Students")
            plt.ylabel("Average")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

    else:
        print("Invalid choice. Please select one of the options from the menu.")
