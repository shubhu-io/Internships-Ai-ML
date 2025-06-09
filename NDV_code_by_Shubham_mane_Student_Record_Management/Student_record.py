# Student Records Management System (Console App)
students = []

def add_student():
    print("\n=== Add Student ===")
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    year = input("Enter Year: ")
    
    student = {"roll": roll, "name": name, "branch": branch, "year": year}
    students.append(student)
    print(f"Student {name} added successfully!\n")

def view_students():
    print("\n=== Student Records ===")
    if not students:
        print("No records found.\n")
        return
    for i, student in enumerate(students, start=1):
        print(f"{i}. Roll: {student['roll']}, Name: {student['name']}, Branch: {student['branch']}, Year: {student['year']}")
    print()

def search_student():
    print("\n=== Search Student ===")
    roll = input("Enter Roll Number to search: ")
    for student in students:
        if student["roll"] == roll:
            print(f"Found: Roll: {student['roll']}, Name: {student['name']}, Branch: {student['branch']}, Year: {student['year']}\n")
            return
    print("Student not found.\n")

def update_student():
    print("\n=== Update Student ===")
    roll = input("Enter Roll Number to update: ")
    for student in students:
        if student["roll"] == roll:
            print("Leave blank to keep existing value.")
            name = input(f"New Name ({student['name']}): ") or student["name"]
            branch = input(f"New Branch ({student['branch']}): ") or student["branch"]
            year = input(f"New Year ({student['year']}): ") or student["year"]
            student.update({"name": name, "branch": branch, "year": year})
            print("Student record updated successfully.\n")
            return
    print("Student not found.\n")

def delete_student():
    print("\n=== Delete Student ===")
    roll = input("Enter Roll Number to delete: ")
    for i, student in enumerate(students):
        if student["roll"] == roll:
            students.pop(i)
            print("Student record deleted.\n")
            return
    print("Student not found.\n")

def main():
    while True:
        print("======= Student Records Management =======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Roll Number")
        print("4. Update Student Record")
        print("5. Delete Student Record")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting program... Peace out! ✌️")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
