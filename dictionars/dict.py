person = {
    "name": "Alex",
    "surname": "Alexov",
    "age": 33,
}
person["major"] = "Engineer"

additional_info_person = {
    "age": 34,
    "children": 3,
    "hobby": "coding"
}

person.update(additional_info_person)
person = person | additional_info_person

print(person)