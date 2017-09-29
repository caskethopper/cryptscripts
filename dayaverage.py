import requests
r1 = requests.get("https://min-api.cryptocompare.com/data/dayAvg?fsym=BTC&tsym=USD&UTCHourDiff=-8&extraParams=your_app_name")
r2 = requests.get("https://min-api.cryptocompare.com/data/dayAvg?fsym=ETH&tsym=GBP&toTs=1487116800&tryConversion=false&extraParams=your_app_name")
r3 = requests.get("https://min-api.cryptocompare.com/data/dayAvg?fsym=ETH&tsym=GBP&toTs=1487116800&avgType=MidHighLow&tryConversion=false&extraParams=your_app_name")
r4 = requests.get("https://min-api.cryptocompare.com/data/dayAvg?fsym=ETH&tsym=GBP&toTs=1487116800&avgType=VolFVolT&tryConversion=false&extraParams=your_app_name")

print(r1.text)
print(r2.text)
print(r3.text)
print(r4.text)
