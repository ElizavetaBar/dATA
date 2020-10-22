from pprint import pprint
from lxml import html
import requests
from pymongo import MongoClient
client = MongoClient('127.0.0.1', 27017)
db2_mongo = client['News']
newsmo = db2_mongo.newsmo



header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

# mail ru news
main_link_mail = 'https://news.mail.ru'
response_mail = requests.get(main_link_mail,headers=header)
dom = html.fromstring(response_mail.text)


# mail ru news получаем источник и дату

names = dom.xpath("//li//a[contains(@class, 'list__text')]/text() | //span/span[contains(@class, 'topnews')]/text()")
links = dom.xpath("//li//a[contains(@class, 'list__text')]/@href | //div/a[contains(@class, 'topnews')]/@href")

data_n = []
source = []
for link in links:
    response2 = requests.get(link, headers=header)
    dom2 = html.fromstring(response2.text)
    data_ns = dom2.xpath("//span[contains(@class, 'note__text')]/text()")
    data_n.append(data_ns)
    source_ns = dom2.xpath("//span[contains(@class, 'breadcrumbs__item')]//a/span[contains(@class, 'link__text')]/text()")
    source.append(source_ns)

mail_news = {}
mail_news['name'] = names
mail_news['link'] = links
mail_news['date'] = data_n
mail_news['source'] = source


newsmo.insert_one({'name': names, 'link': links, 'date': data_n, 'source': source})
print(mail_news)

