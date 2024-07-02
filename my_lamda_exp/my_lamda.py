fruit = ["banana", "apple", "cherry", "watermelon"]
random_dict = {"name": "Alex", "fruit": "gooseberry", "major": "python engineer", "age": 34}

filtered_fruit = list(filter(lambda element: len(element) < 6, fruit)) # lambda filter by len of elements
# print(filtered_fruit)
sorted_fruits = sorted(fruit, key=lambda fruit: len(fruit), reverse=True) # lambda sorted by len of elements
# print(sorted_fruits)
shortest_word = min(fruit, key=lambda element: len(element)) # example of max/min function also works with lambda
# print(shortest_word)

random_names = [
    {"name": "Alex", "age": 34},
    {"name": "John", "age": 38},
    {"name": "Dave", "age": 36},
    {"name": "Rick", "age": 35},
]

sorted_rand_names_lambda = sorted(random_names, key=lambda el: (el["age"], el["name"]))
print(sorted_rand_names_lambda)