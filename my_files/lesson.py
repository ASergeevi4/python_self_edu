import csv

persons = [
    {"name": "Dracula",
    "age": 841,
    "occupation": "vampire"},
    {"name": "Shumacher",
    "age": 57,
    "occupation": "racer"},
    ]

# file = open("files/persons.csv", "a")

# fields = ["name", "age", "occupation"]
# csv_dict_writer = csv.DictWriter(file, fieldnames=fields)
# csv_dict_writer.writerows(persons)

# file.close()

file = open("files/persons.csv", "a")