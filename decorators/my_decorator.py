def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happened before funct was called.")
        result = func(*args, **kwargs)
        print("Something after")
        return result
    return wrapper

@my_decorator
def add_numbers(a: int, b: int) -> int:
    print("Adding numbers...")
    return a + b

result = add_numbers(12, 5)
print(result)