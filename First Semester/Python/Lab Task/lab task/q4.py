class Student:
    def __init__(self, faculty, subjects):
        self.faculty = faculty
        self.subjects = subjects

student1 = Student(
    "MCA",
    {
        "Python": 80,
        "Database": 75,
        "Operating System": 82
    }
)

student2 = Student(
    "MCA",
    {
        "Python": 85,
        "Database": 88,
        "Operating System": 79
    }
)

print("Student 1")
print("Faculty:", student1.faculty)
print("Subjects:", student1.subjects)

print("\nStudent 2")
print("Faculty:", student2.faculty)
print("Subjects:", student2.subjects)