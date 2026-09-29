# STUDENT RECORD MANAGEMENT SYSTEM

students = []


def calculate_result(math, science, english):

    total = math + science + english
    percentage = total / 3

    if math < 35 or science < 35 or english < 35:
        grade = "F"
        status = "Fail"

    elif percentage >= 90:
        grade = "A+"
        status = "Pass"

    elif percentage >= 80:
        grade = "A"
        status = "Pass"

    elif percentage >= 70:
        grade = "B"
        status = "Pass"

    elif percentage >= 60:
        grade = "C"
        status = "Pass"

    elif percentage >= 50:
        grade = "D"
        status = "Pass"

    else:
        grade = "E"
        status = "Pass"

    return total, percentage, grade, status



def add_student():

    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    class_name = input("Enter Class: ")

    math = int(input("Enter Math Marks: "))
    science = int(input("Enter Science Marks: "))
    english = int(input("Enter English Marks: "))

    total, percentage, grade, status = calculate_result(
        math, science, english
    )

    student = [
        roll,
        name,
        class_name,
        math,
        science,
        english,
        total,
        percentage,
        grade,
        status
    ]

    students.append(student)

    print("\nStudent added successfully!")


# Function to display students
def show_students():

    if len(students) == 0:
        print("\nNo student records found.")
        return

    print("\n---------- STUDENT RECORDS ----------")

    for student in students:

        print("\nRoll Number :", student[0])
        print("Name        :", student[1])
        print("Class       :", student[2])
        print("Math        :", student[3])
        print("Science     :", student[4])
        print("English     :", student[5])
        print("Total       :", student[6])
        print("Percentage  :", round(student[7], 2), "%")
        print("Grade       :", student[8])
        print("Status      :", student[9])


# Function to search student
def search_student():

    roll = input("Enter Roll Number to search: ")

    found = False

    for student in students:

        if student[0] == roll:

            print("\nStudent Found!")
            print("Roll Number :", student[0])
            print("Name        :", student[1])
            print("Class       :", student[2])
            print("Math        :", student[3])
            print("Science     :", student[4])
            print("English     :", student[5])
            print("Total       :", student[6])
            print("Percentage  :", round(student[7], 2), "%")
            print("Grade       :", student[8])
            print("Status      :", student[9])

            found = True
            break

    if found == False:
        print("\nStudent not found.")


# Function to delete student
def delete_student():

    roll = input("Enter Roll Number to delete: ")

    found = False

    for student in students:

        if student[0] == roll:

            students.remove(student)

            print("\nStudent deleted successfully.")

            found = True
            break

    if found == False:
        print("\nStudent not found.")


# Main program

print("*" * 60)
print("       CSE PROJECT - VITYARTHI")
print("   STUDENT RECORD MANAGEMENT SYSTEM")
print("*" * 60)

print("NAME : YASH JHA")
print("REG NO. : 26BCE11517")
print("PROFESSOR : PRADEEP KUMAR MISHRA")
print("SLOT : B11+B12+B13+C14+E11+E12")

while True:

    print("\n")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("\nThank you for using Vityarthi.")
        break

    else:
        print("\nInvalid choice. Please try again.")