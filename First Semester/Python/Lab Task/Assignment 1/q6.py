"""
Write a program that takes user input day name. If the day is Monday, Tuesday, Wednesday, Thursday or Friday, then show “It’s a week day”. If the day is Saturday then show “It’s weekend”. If the day is  sunday then show “Yay! It’s a holiday”.
"""
day = input("Enter the day name: ").upper()
days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]
if day in days:
    print("It's a week day")
elif day == "SATURDAY":
    print("It's weekend")
elif day == "SUNDAY":
    print("Yay! It's a holiday")
else:
    print("Invalid day name")