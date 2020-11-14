# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from instaparser1.items import InstaparserItem
from scrapy import Spider
from pymongo import MongoClient

class Instaparser1Pipeline:

    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.instagram
        self.collection = self.mongo_base['insta']

    def process_item(self, item: InstaparserItem, spider: Spider):
        self.collection.insert(item)
        return item



