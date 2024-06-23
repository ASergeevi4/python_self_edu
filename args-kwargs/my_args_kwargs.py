def add_all(*args):         #example with int
    return sum(args)

values = [1, 2, 3, 4, 5]
addition_values = [6, 7, 8, 9, 10]

# def add_all(*args):       #example with words in list
#     result = []
#     for item in args:
#         if item not in result:
#             result.append(item)
#     return result
# values = ["alex", "samantha"]
addition_values = ["john", "richard"]

print(add_all(*values, *addition_values))
