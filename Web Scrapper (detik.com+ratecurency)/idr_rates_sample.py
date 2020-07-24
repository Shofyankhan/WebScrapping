import requests
import json

#json_data = requests.get('http://floatrates.com/daily/idr.json')

json_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":6.9209556253048e-5,"date":"Sat, 11 Jul 2020 00:00:01 GMT","inverseRate":14448.871718578},"eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":6.1343191208715e-5,"date":"Sat, 11 Jul 2020 00:00:01 GMT","inverseRate":16301.727710865}}

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])