# Write a function that take start and end number as inputs & display counting in your screen. (use time.sleep(sec) to take a pause while counting)
import time

def counting(start, end):
    for i in range(start, end + 1):
        print(i)
        time.sleep(1)

counting(1, 10)