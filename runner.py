from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from instaparser1.spiders.instagram import InstagramSpider
from instaparser1 import settings
from pymongo import MongoClient

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(InstagramSpider)
    process.start()
