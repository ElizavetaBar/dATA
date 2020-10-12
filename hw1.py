import requests
import json
from pprint import pprint


# service = 'https://github.com/ElizavetaBar/Python-bib/pulls'
# req = requests.get(service)
# data = json.loads(req.text)

ow = 'ElizavetaBar'
re = 'Python-bib'
main_link = f'https://github.com/{ow}/{re}/pulls'

# params = {
#   'owner': ow, 'repo': re
# }

response = requests.get(main_link)
#print(response.text)
#
j_data = response.json()
# pprint(j_data)

with open('response.json','w') as f:
    json.dump(j_data,f)

# with open('response.json','w') as f:
#     json.dump(j_data,f)
#
# print(f' Список реквестов пользователя {j_data["owner"]}: {j_data["main"]}')


# main_link = 'http://api.openweathermap.org/data/2.5/weather'
# city = 'Moscow,US'
# params = {
#     'q':city,
#     'appid':'e5e4cd692a72b0b66ea0a6b80255d1c3'
# }
#
# response = requests.get(main_link,params=params)
# # print(response.text)
# j_data = response.json()
# pprint(j_data)
#
# with open('response.json','w') as f:
#     json.dump(j_data,f)
#
# print(f'В городе {j_data["name"]} температура {j_data["main"]["temp"]-273.15} градусов')
#
# https://github.com/