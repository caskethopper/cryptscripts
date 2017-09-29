import requests
r = requests.get('https://whattomine.com/coins.json')
print(r.text)
