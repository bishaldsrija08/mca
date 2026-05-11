"""
write the information of students in a file with name "student.txt" where each records should contain roll, name, and marks in five subjects. Display the highest marks of each student.
"""

txt = open("student.txt", "w")
for i in range(1,6):
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = []
    for j in range(1,6):
        mark = float(input(f"Enter marks for subject {j}: "))
        marks.append(mark)
    txt.writelines(f"{roll} {name} {max(marks)}\n")
txt.close()

txt = open("student.txt", "r")

for line in txt:
    print(line.strip())
txt.close()