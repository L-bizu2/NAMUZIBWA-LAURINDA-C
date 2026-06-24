print("------STUDENT REGISTRATION------")

def student_info(name,age,course,studentno):
    
    print("------------------------")
    print("Student Name:",name)
    print("Age:",age)
    print("Course:",course)
    print("Student Number:",studentno)

name = input("Enter your name:")
age = int(input("Enter your age:"))
course = input("Enter your course:")
studentno = input("Enter your Student Number:")

student_info(name,age,course,studentno)