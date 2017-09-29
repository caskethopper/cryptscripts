import requests
r = requests.get('https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=BTC&tsym=USD')

print(r.text)
