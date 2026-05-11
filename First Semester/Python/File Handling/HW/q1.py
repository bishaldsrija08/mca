"""
write the information of students in a file with name "std.tx" where each records should contain roll, name, and marks in theree subjects. Display the higheset marks of each students.
"""

txt = open("std.txt", "w")
txt.writelines("1 BR 100 90 80\n")
txt.writelines("2 AR 90 80 70\n")
txt.writelines("3 CR 80 70 60\n")
txt.close()

txt = open("std.txt", "r")

for line in txt:
    r, n, m1, m2, m3 = line.split()
    m1 = int(m1)
    m2 = int(m2)
    m3 = int(m3)
    max_marks = max(m1, m2, m3)
    print(f"Roll: {r}, Name: {n}, Highest Marks: {max_marks}")