import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from spiders.spiders import SpiderLtnAllNewsSpider

scrapy.utils.reactor.install_reactor('twisted.internet.asyncioreactor.AsyncioSelectorReactor')
is_asyncio_reactor_installed = scrapy.utils.reactor.is_asyncio_reactor_installed()
print(f"asyncio_reactor_installed:{is_asyncio_reactor_installed}")
from twisted.internet import reactor

sleep_interval = 30
def crawl_jobs():    
    print("start")
    setting = get_project_settings()
    runner = CrawlerRunner(setting)
    runner.crawl(SpiderLtnAllNewsSpider)    
    return runner.join()

def after_crawl(null):    
    reactor.callLater(sleep_interval, crawl)

def error_handle(e):
    print(e)
    
def crawl():
    d = crawl_jobs()
    d.addCallback(after_crawl)
    d.addErrback(error_handle)

if __name__=="__main__":
    from twisted.internet import reactor  
    crawl()
    reactor.run()

