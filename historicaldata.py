import requests

r = requests.get('https://min-api.cryptocompare.com/data/pricehistorical?fsym=BTC&tsyms=USD,EUR&ts=1452680400')
print(r.text)

