import requests

r = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH&tsyms=USD&e=Coinbase&extraParams=your_app_name')

print(r.text)
