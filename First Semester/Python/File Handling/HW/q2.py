"""
Take input the information of five students and write it to the file and display the information of the studetns.
"""

txt = open("students.txt", "w")
for i in range(5):
    name = input("Enter the name of the student: ")
    age = input("Enter the age of the student: ")
    grade = input("Enter the grade of the student: ")
    txt.writelines(f"{name} {age} {grade}\n")
txt.close()

txt = open("students.txt", "r")
print(txt.read())