import requests
import time

url = 'https://api.binance.com/api/v3/ticker/price'

list_of_rates = []

for i in range(5):
    response_eth = requests.get(url, params={'symbol': 'ETHUSDT'})
    price_eth = float(response_eth.json()['price'])
    list_of_rates.append(price_eth)
    time.sleep(1)
print(list_of_rates)