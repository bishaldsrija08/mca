"""
Write a program to take input color of road traffic signal from the user & show the message according to this table:
SIGNAL COLOR        MESSAGE
RED                 Vehicle must stop
YELLOW              Vehicles should get ready to move
GREEN               Vehicles can move now
"""

signal_color = input("Enter the color of the traffic signal (RED, YELLOW, GREEN): ").upper()
if signal_color == "RED":
    print("Vehicle must stop")
elif signal_color == "YELLOW":
    print("Vehicles should get ready to move")
elif signal_color == "GREEN":
    print("Vehicles can move now")
else:
    print("Invalid input. Please enter RED, YELLOW, or GREEN.")
