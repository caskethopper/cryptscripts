import requests
r = requests.get('https://api.cryptonator.com/api/full/btc-usd')
print(r.text)
