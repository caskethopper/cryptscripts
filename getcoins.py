import requests

r = requests.get('https://www.cryptocompare.com/api/data/coinlist/')
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())
