"""
Write a program using for loop that will iterate from 1 to 20. For each iteration, it will check if the current number is even or odd, and report that to the screen (e.g."2 is even").
1 is Odd
2 is Even
3 is Odd
4 is Even
5 is Odd
and so on.
"""

for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} is Even")
    else:
        print(f"{i} is Odd")