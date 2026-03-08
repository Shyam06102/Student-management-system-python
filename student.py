import sqlite3

# Connect to database

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Create table

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER,
course TEXT
)
""")

conn.commit()

# Add student data

def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter course: ")

    cursor.execute("INSERT INTO students(name, age, course) VALUES(?,?,?)",(name,age,course))
    conn.commit()
    print("Student added successfully")

# View students data

def view_students():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    for row in data:
        print(row)

# Update student data
def update_student():
    id = int(input("Enter student ID: "))
    name = input("Enter new name: ")
    age = input("Enter student age: ")
    course = input("Enter course: ")

    cursor.execute("UPDATE students SET name=? WHERE id=?", (name,id))
    conn.commit()
    print("Student updated successfully")

# Delete student data

def delete_student():
    id = int(input("Enter student ID to delete: "))

    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    print("Student Deleted successfully")

while True:
    print("\nStudent Management System")
    print("1 Add Student")
    print("2 View Student")
    print("3 Update Student")
    print("4 Delete Student")
    print("5 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        break

conn.close()
