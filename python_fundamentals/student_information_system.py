
students = []

def add_student():
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    student = {
        "id": student_id,
        "name": input("Enter Name: "),
        "age": input("Enter Age: "),
        "course": input("Enter Course: ")
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    if not students:
        print("No records found.")
        return

    print("\n===== STUDENT RECORDS =====")

    for student in students:
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        print("-" * 30)


def search_student():
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found:")
            print(student)
            return

    print("Student not found.")


def update_student():
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            student["name"] = input("Enter New Name: ")
            student["age"] = input("Enter New Age: ")
            student["course"] = input("Enter New Course: ")

            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


while True:

    print("\n===== STUDENT INFORMATION SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")