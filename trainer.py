# import random
# import json
# import requests
# import time

# my_string = "Hello, world!"
# fruits = ["apple", "banana", "melon", "fig", "grape"]
# 
# file_nammes = ["video.mp4", "audio.mp3", "document.txt", "image.jpg"]
# numbers_list = [5, 3, 2, 4, 1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# straight_numbers = [1, 2, 3, 4, 5]
# new_list = []
# person_john_dict = {"name": "John", "age": 41, "city": "Toronto", "married": False}
# person_alex_dict = {"name": "Alex", "age": 34, "city": "Dnipro", "married": True, "job": "programmer"}
# additional_info_alex = {"motofan": "yes", "have a car": True, "hobbie": "fishing"}

# people = [
#     {"name": "Alice", "age": 40, "occupation": "housewife"},
#     {"name": "Russell", "age": 64, "occupation": "worker"},
#     {"name": "Steve", "age": 34, "occupation": "zoo-worker"},
#     {"name": "Tiana", "age": 12, "occupation": "student"},
#     {"name": "Arina", "age": 12, "occupation": "musician"}
# ]

# sorted_by_age = sorted(people, key=sort_by_age_name)
# print(sorted_by_age)

# people_2 = [
#     {"name": "Mattew", "age": 41, "occupation": "goalkeeper"},
#     {"name": "Jannet", "age": 12, "occupation": "student"},
#     {"name": "Paul", "age": 35, "occupation": "driver"},
#     {"name": "Monika", "age": 24, "occupation": "vet"},
#     {"name": "Renau", "age": 19, "occupation": "dancer"}
# ]

# person = {"name": "Alice", "age": 40, "occupation": "housewife"}
# other_person = {"country": "USA", "grade": "High"}
# book = {
#     "title": "1984",
#     "author": "George Orwell",
#     "isbn": "978-0451524935",
#     "uuid": "a0eevc99-9c0b-4ef8-bb6d-66bb9bd380a11"
# }

# =============== REQUESTS =============
# url = 'https://api.binance.com/api/v3/ticker/price'
# response = requests.get(url=url, params={'symbol': 'BTCUSDT'})
# how_often = int(input('How many times make a request?: '))
# bitcoin_prices = []
# for i in range(how_often):
#     response = requests.get(url, params={'symbol': 'BTCUSDT'})
#     price = float(response.json()['price'])
#     bitcoin_prices.append(price)
#     time.sleep(1)
# print(bitcoin_prices)
# print(max(bitcoin_prices))
# print(min(bitcoin_prices))
# =============== REQUESTS =============

# url = 'https://jsonplaceholder.typicode.com/users'
# response = requests.get(url)
# content = response.json()
# names_list = []
# for i in content[1:2]:
#     for adress in i['address']:
#         if adress['city'][0] == 'S':
#             names_list.append(i['name'])
# print(names_list)

# students = ["Matthew", "Alice", "Andrew", "Steve", "Aaron", "Mag"]

# list_of_nums = list()
# for i in range(int(input())):
#     new_input = input()
#     list_of_nums.append(set(new_input))
# d = list_of_nums[0]
# for i in range(1, len(list_of_nums)):
#     d &= list_of_nums[i]
# print(*sorted(d))

num1, num2 = set(input()), set(input())
print('YES' if num1.issuperset(num2) else 'NO')