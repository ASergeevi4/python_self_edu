# ============ 

def is_even(n: int) -> bool: # function to identify even numbers
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = list(filter(is_even, numbers)) # list covering and sequence are NECESSARY and important
# print(filtered_numbers)

def is_older(person: dict) -> bool: # funct to identify and filter by key
    return person["age"] > 21

people = [
    {"name": "Alice", "age": 18},
    {"name": "Jack", "age": 22},
    {"name": "John", "age": 21},
    {"name": "Bruce", "age": 28},
    {"name": "Alex", "age": 34}
]

filtered_by_age = list(filter(is_older, people)) # list covering and sequence are NECESSARY and important
print(filtered_by_age)