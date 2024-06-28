set_1 = {1, 2, 3, 4, 5, 6}
set_2 = {4, 5, 6, 7, 8}
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 7, 7, 7, 7, 8, 9, 10] # list of numbers

united_set = set_1.union(set_2)
# print(united_set)

# print(set_2.difference(set_1)) # differences between main and compared sets
# print(set_1.intersection(set_2)) # same values

squares_set = {x ** 2 for x in range(1,11)}
# print(squares_set)

unique_numbers_in_numbers = list(set(numbers)) # making list with unique values from list
# print(unique_numbers_in_numbers)