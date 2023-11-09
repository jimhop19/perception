from typing import Iterable
import scrapy
import json
from scrapy.crawler import CrawlerProcess
from scrapy.http import Request
from scrapy.utils.project import get_project_settings
import multiprocessing

class SpiderPtsSpider(scrapy.Spider):
    name = "spider_pts"
    allowed_domains = ["news.pts.org.tw"]
    # start_urls = ["https://news.pts.org.tw/search/藍白"]

    # def __init__(self, *args, **kwargs):
    #     super(SpiderPtsSpider, self).__init__(*args, **kwargs)        
    #     # self.start_urls = f'https://news.pts.org.tw/search/{keyword}'        
    #     self.results = []
    def start_requests(self):
        yield scrapy.Request(f'https://news.pts.org.tw/search/{self.keyword}')
        # self.results = []

    def parse(self, response, **kwargs):
        articles = response.xpath("//ul[@class='list-unstyled search-list relative-news-list-content']/li")

        # count = 0
        for article in articles:
            title = article.xpath(".//div/h2/a/text()").get()
            yield {
                "name":title
            }
            # title = article.xpath(".//div/h2/a/text()").get()
            # self.results.append({'title': title})
            # count += 1
            # if count == 5:
            #     break

    # def closed(self, reason):
    #     # Write the results to a JSON file
    #     print (self.results)
    #     return self.results
    #     # with open('pts.json', 'w', encoding='utf-8') as file:
    #     #     json.dump(self.results, file, ensure_ascii=False, indent=4)
    #     # return self.results


class SpiderUdnSpider(scrapy.Spider):
    name = "spider_udn"
    allowed_domains = ["udn.com"]
    start_urls = ["https://udn.com/search/word/2/藍白"]
    def __init__(self, *args, **kwargs):
        super(SpiderUdnSpider, self).__init__(*args, **kwargs)
        # self.start_urls = [f"https://udn.com/search/word/2/{keyword}"]
        self.results = []

    def parse(self, response):
        articles = response.xpath("//div[@class='story-list__news']/div[2]")
        count = 0
        for article in articles:
            title = article.xpath(".//h2/a/text()").get()
            self.results.append({'title': title})
            count += 1
            if count == 5:
                break

    def closed(self, reason):        
        # Write the results to a JSON file
        print (self.results)
        # with open('udn.json', 'w', encoding='utf-8') as file:
        #     json.dump(self.results, file, ensure_ascii=False, indent=4)

# settings = get_project_settings()
# process = CrawlerProcess(settings)
# process.crawl(SpiderPtsSpider)
# process.crawl(SpiderUdnSpider)
# process.start()