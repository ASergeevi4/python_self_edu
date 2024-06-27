import requests

#  задание
#  1. Отправьте на https://api.binance.com/api/v3/ticker/price запрос БЕЗ аргумента params.
#  2. Изучите структуру ответа, сравните её с ответом в запросе без params.
#  3. Напишите код, который найдёт курс Etherium'а к доллару (ETHUSDT) в полученной из запроса структуре.

#  решение

response_json = requests.get('https://api.binance.com/api/v3/ticker/price').json()

for trade_pair in response_json:
    if trade_pair['symbol'] == 'ETHUSDT':
        print(trade_pair['price'])