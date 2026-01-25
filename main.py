
from functions import add_student, display_students,search_student,update_placement,delete_student

students = []  

while True:
    print("\n--- Placement Management ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Placement")
    print("5. Delete Student")
    print("6. Exit")


    choice = input("Enter choice: ")
    if choice == '1':
        add_student(students)
    elif choice == '2':
        display_students(students)

    elif choice == '3':
        roll = input("Enter roll to search: ")
        search_student(students, roll)

    elif choice == '4':
        roll = input("Enter roll to update placement: ")
        update_placement(students, roll)

    elif choice == '5':  
        roll = input("Enter roll to delete: ")
        delete_student(students, roll)

