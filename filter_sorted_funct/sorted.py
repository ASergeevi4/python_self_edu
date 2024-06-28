#       ========== sort with list
fruit = ['banana', 'apple', 'cherry', 'date'] 
sorted_fruit = sorted(fruit, reverse=True)  # linear sort
# print(sorted_fruit)

def sort_by_len(element: str) -> int:   # funct to indicate lenght element of (list for example)
    return len(element)

sorted_fruit = sorted(fruit, key=sort_by_len)
# print(sorted_fruit)


#       ============
