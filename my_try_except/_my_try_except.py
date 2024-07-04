import requests, time

# def find_average(*, numbers: list) -> float:
#     return sum(numbers) / len(numbers)

# try:
#     print(find_average(numbers=[]))
# except ZeroDivisionError:
#     print("The list is empty")

try:
    amount_of_requests = int(input("Enter amount of requests (only integers): "))
    min_rate = float(input("Enter minimum rate in range: "))
    max_rate = float(input("Enter maximum rate in range: "))
    good_value = {}
    for i in range(amount_of_requests):
        response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'})
        bitcoin_price = float(response.json()["price"])
        time.sleep(1)
        print(bitcoin_price)
        if bitcoin_price >= min_rate and bitcoin_price <= max_rate:
            good_value[time.ctime()] = bitcoin_price
    print("======", f"Amount in collection is {len(good_value)}", good_value, sep="\n")

except requests.exceptions.ConnectionError as error: # if there no internet or signal lost
    print(f"The problem with {error}")
