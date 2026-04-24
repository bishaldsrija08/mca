def myfunc(n):
    return lambda a : a * n

result = myfunc(2) # result is now a lambda function that multiplies its input by 2
print(result(11)) # passing 11 to the lambda function will return 22, since it multiplies 11 by 2.