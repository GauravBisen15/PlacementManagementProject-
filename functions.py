from student import Student

def add_student(student_list):
    name=input("Enter name : ")
    roll=input("Enter roll no : ")
    branch=input("Enter branch : ")
    cgpa=float(input("Enter cgpa :"))
    student=Student(name,roll,branch,cgpa)
    student_list.append(student)
    print("Student added successfully!")

def display_students(student_list):
    if not student_list:
        print("No student found!")
        return
    print("Roll | Name | Branch | CGPA | Status ")
    print("-"*40)
    for s in student_list:
        print(s) 

def search_student(student_list, roll):
    for s in student_list:
        if s.roll == roll:
            print("Student found:")
            print(s)
            return s
    print("Student not found!")
    return None

def update_placement(student_list, roll):
    student = search_student(student_list, roll)
    if student:
        student.placed = True
        print(f"{student.name} marked as Placed!")

def delete_student(student_list, roll):
    student = search_student(student_list, roll)
    if student:
        student_list.remove(student)
        print(f"{student.name} removed from records!")

