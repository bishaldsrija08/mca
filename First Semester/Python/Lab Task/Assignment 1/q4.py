"""
Write a program to take “gender” as input from user. If the user is male, give the message: Good Morning Sir. If the user is female, give the message: Good Morning Ma’am.
"""

gender = input("Enter your gender: ")

if gender == "male":
    print("Good Morning Sir.")
elif gender == "female":
    print("Good Morning Ma’am.")
else:
    print("Invalid input. Please enter only male or female.")