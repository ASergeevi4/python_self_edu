# def add_all(*args):         #example with int. Can be used with lines 4-5
#     return sum(args)

# values = [1, 2, 3, 4, 5]
# addition_values = [6, 7, 8, 9, 10]

# # def add_all(*args):       #example with words in list. Can be used with lines 14-15
# #     result = []
# #     for item in args:
# #         if item not in result:
# #             result.append(item)
# #     return result

# # values = ["alex", "samantha"]
# # addition_values = ["john", "richard"]

# print(add_all(*values, *addition_values))

# def introduce(**kwargs):
#     for key, value in kwargs.items(): #instead items() method can be used with values(), key() and others
#         print(key, value)

person = {
    "name": "Alex",
    "surname": "Alexov",
    "major": "Python engineer",
    "married": True
}

# introduce(**person, city="Dnipro")

def add_all_types(x: int, y: int, *args, value: int = 66, **kwargs):
    print(x + y)
    print(args)
    print(value)
    print(kwargs)

add_all_types(1, 2, 3, 4, 5, 74, value=97, **person)