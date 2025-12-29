from utils import load_data, save_data
from students import Student

FILENAME = "grades.json"

# Load existing data
raw_data = load_data(FILENAME)
students = {}
for name, grades in raw_data.items():
    s = Student(name)
    s.grades = grades
    students[s.name] = s

# --- Menu Functions ---

def show_menu():
    print("\n--- Student Grade Management System ---")
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Add Grade to Student")
    print("5. Update Student Info")
    print("6. Delete Student")
    print("7. Generate Report")
    print("8. View Statistics")
    print("9. Exit")

def add_student():
    name = input("Enter student full name: ").strip().title()
    if name in students:
        print("Student already exists.")
    else:
        students[name] = Student(name)
        print(f"{name} added successfully.")

def list_students():
    if not students:
        print("No students available.")
    else:
        print("Students:")
        for name in students:
            print(f"- {name}")

def search_student():
    name = input("Enter student full name: ").strip().title()
    student = students.get(name)
    if student:
        print(f"Student: {student.name}")
        print(f"Grades: {student.grades if student.grades else 'No grades yet'}")
        stats = student.statistics()
        if stats:
            print(f"Average: {stats['average']:.2f}, Min: {stats['min']}, Max: {stats['max']}")
    else:
        print("Student not found.")

def add_grade():
    name = input("Enter student full name: ").strip().title()
    student = students.get(name)
    if not student:
        print("Student not found.")
        return
    try:
        grade = float(input("Enter grade (0-100): "))
        if student.add_grade(grade):
            print("Grade added.")
        else:
            print("Grade must be between 0 and 100.")
    except ValueError:
        print("Invalid grade input.")

def update_student():
    name = input("Enter current student name: ").strip().title()
    student = students.get(name)
    if not student:
        print("Student not found.")
        return
    new_name = input("Enter new name: ").strip().title()
    if new_name in students:
        print("A student with this name already exists.")
        return
    student.update_name(new_name)
    students[new_name] = student
    del students[name]
    print(f"Student name updated to {new_name}.")

def delete_student():
    name = input("Enter student full name to delete: ").strip().title()
    if name in students:
        del students[name]
        print(f"{name} has been deleted.")
    else:
        print("Student not found.")

def generate_report():
    if not students:
        print("No students available.")
        return
    print("--- Student Report ---")
    for student in students.values():
        stats = student.statistics()
        grades = student.grades if student.grades else "No grades"
        if stats:
            print(f"{student.name} → Grades: {grades}, Avg: {stats['average']:.2f}, Min: {stats['min']}, Max: {stats['max']}")
        else:
            print(f"{student.name} → Grades: {grades}")

def view_statistics():
    if not students:
        print("No students available.")
        return
    for student in students.values():
        stats = student.statistics()
        if stats:
            print(f"{student.name} → Avg: {stats['average']:.2f}, Min: {stats['min']}, Max: {stats['max']}")
        else:
            print(f"{student.name} → No grades yet.")

def save_and_exit():
    data_to_save = {s.name: s.grades for s in students.values()}
    save_data(FILENAME, data_to_save)
    print("Data saved. Goodbye!")
    exit()

# --- Main Loop ---

while True:
    show_menu()
    choice = input("Choose an option: ").strip()
    options = {
        "1": add_student,
        "2": list_students,
        "3": search_student,
        "4": add_grade,
        "5": update_student,
        "6": delete_student,
        "7": generate_report,
        "8": view_statistics,
        "9": save_and_exit
    }
    action = options.get(choice)
    if action:
        action()
    else:
        print("Invalid option, try again.")
