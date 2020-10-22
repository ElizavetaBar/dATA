from pprint import pprint
from lxml import html
import requests
from pymongo import MongoClient
client = MongoClient('127.0.0.1', 27017)
db2_mongo = client['News']
newsmo = db2_mongo.newsmo

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}


main_link = 'https://lenta.ru'
response = requests.get(main_link,headers=header)
dom = html.fromstring(response.text)

names = dom.xpath("//time[@class='g-time']/../..")
dates = dom.xpath("//time[@class='g-time'")
source = []
links = dom.xpath("//time[@class='g-time']/../../@href")

lenta_news = {}
lenta_news['name'] = names
lenta_news['link'] = links
lenta_news['date'] = dates
lenta_news['source'] = source


newsmo.insert_one({'name': names, 'link': links, 'date': dates, 'source': source})