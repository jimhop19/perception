# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
# from elasticsearch import Elasticsearch
import json
import requests

class DuplicateTitlePipeline:
    def __init__(self):
        self.titles_seen = set()
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if item["title"] in self.titles_seen:
            raise DropItem(f"Duplicate item found:{item}")
        else:
            self.titles_seen.add(adapter["title"])
            return item

class ElasticSearchPipeline:
    def process_item(self,item,spider):        
        media_name = spider.name.split("_")[1]
        data = item        
        response = requests.post(f"http://localhost:9200/{media_name}/_doc",auth=("elastic","HcgGLEbnRQIHsQggWwhP") ,json=data)
        print(response)
        return item
