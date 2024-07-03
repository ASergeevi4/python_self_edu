import requests, time, datetime

# def find_average(*, numbers: list) -> float:
#     return sum(numbers) / len(numbers)

# try:
#     print(find_average(numbers=[]))
# except ZeroDivisionError:
#     print("The list is empty")

try:

    good_value = {}
    for i in range(10):
        response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'})
        bitcoin_price = float(response.json()["price"])
        time.sleep(1)
        print(bitcoin_price)
        if bitcoin_price >= 62092.01:
            good_value.append(bitcoin_price)
            time_of_best.append(datetime.datetime.now())
    print(len(good_value), good_value, time_of_best)
except requests.exceptions.ConnectionError as error: # if there no internet or signal lost
    print(f"The problem with {error}")