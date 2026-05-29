"""
Given the initial deposit, the annual interest rate, and the number of years that you invest your money in an investment account. Calculate the final amount of the investment using math.pow() function.
ammount = deposit(1 + interest_rate) ** years
"""

import math
deposit = float(input("Enter the initial deposit: "))
interest_rate = float(input("Enter the annual interest rate (in decimal): "))
years = int(input("Enter the number of years: "))

final_amount = deposit * math.pow((1+ interest_rate), years)
print(f"The final amount of the investment after {years} years is: {final_amount:.2f}")