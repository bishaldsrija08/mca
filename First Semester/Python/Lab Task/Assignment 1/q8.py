""""
Write a program to take input the marks obtained in three subjects & total marks. Compute & show the resulting percentage on your page. Take percentage & compute grade as per following table:

Percentage                          Grade           Remarks
Greater than or equal to 80         A-one           Excellent
Greater than or equal to70          A               Good
Greater than or equal to 60         B               You need to improve
Less than 60                         Fail            Sorry
"""

marks1 = float(input("Enter marks obtained in subject 1: "))
marks2 = float(input("Enter marks obtained in subject 2: "))
marks3 = float(input("Enter marks obtained in subject 3: "))

total_marks = float(input("Enter total marks: "))

total_obtained = marks1 + marks2 + marks3
percentage = (total_obtained / total_marks) * 100
print(f"Total Marks Obtained: {total_obtained}")
print(f"Percentage: {percentage:.2f}%")

if percentage >= 80:
    print("Grade: A-one")
    print("Remarks: Excellent")
elif percentage >= 70:
    print("Grade: A")
    print("Remarks: Good")
elif percentage >= 60:
    print("Grade: B")
    print("Remarks: You need to improve")
else:
    print("Grade: Fail")
    print("Remarks: Sorry")