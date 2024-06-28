# #       ========== sort with list
# fruit = ["banana", "apple", "cherry", "date"] 
# sorted_fruit = sorted(fruit, reverse=True)  # linear sort
# # print(sorted_fruit)

# def sort_by_len(element: str) -> int:   # funct to indicate lenght element of (list for example)
#     return len(element)

# sorted_fruit = sorted(fruit, key=sort_by_len)
# # print(sorted_fruit)


#       ============ sort by parameters

people = [
    {"name": "Alice", "age": 18},
    {"name": "Jack", "age": 22},
    {"name": "John", "age": 21},
    {"name": "Bruce", "age": 28},
    {"name": "Alex", "age": 34}
]

def sort_by_age(person: dict) -> int: # sort by age (or single 'key')
    return person["age"]

older_people_sorting = sorted(people, key=sort_by_age, reverse=True)
# print(older_people_sorting)

def sort_by_age_name(person: dict) -> tuple[int, str]: # sort by few parameters. Annotation isn't necessary
    return person["age"], person["name"]

sort_more_specific = sorted(people, key=sort_by_age_name)
# print(sort_more_specific)