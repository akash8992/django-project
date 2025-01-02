# Defining a custom exception
class CustomError(Exception):
    pass

def divide(a, b):
    if b == 0:
        raise CustomError("Cannot divide by zero!")
    return a / b

try:
    result = divide(10, 4)
except CustomError as e:
    print(e)
