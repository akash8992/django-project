# Defining a simple decorator
def decorator_function(func):
    def wrapper(*args, **kwargs):
        print("Before function call.")
        result = func(*args, **kwargs)
        print("After function call.")
        return result
    return wrapper

@decorator_function
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Akash")
