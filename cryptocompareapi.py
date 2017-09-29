import requests
r=requests.get('https://min-api.cryptocompare.com/')

print(r.text)
