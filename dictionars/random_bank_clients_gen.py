import random

def generate_random_name():
    first_names = ["John", "Jane", "Alex", "Chris", "Katie", "Laura", "Mike", "Sarah", "David", "Emily"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
    return random.choice(first_names), random.choice(last_names)

def generate_account_number():
    return str(random.randint(10000000, 99999999))

def generate_email(name, surname):
    domains = ["gmail.com", "ukr.net", "mail.com", "outlook.com"]
    return f"{name.lower()}.{surname.lower()}@{random.choice(domains)}"

def generate_account_balance():
    return round(random.uniform(1000, 100000), 2)

clients = []

for _ in range(50):
    name, surname = generate_random_name()
    client = {
        "name": name,
        "surname": surname,
        "account_balance": generate_account_balance(),
        "account_number": generate_account_number(),
        "email": generate_email(name, surname)
    }
    clients.append(client)

print(client)