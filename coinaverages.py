import requests
r = requests.get('https://min-api.cryptocompare.com/data/generateAvg?fsym=BTC&tsym=USD&markets=Coinbase,Bitfinex')
print(r.text)
