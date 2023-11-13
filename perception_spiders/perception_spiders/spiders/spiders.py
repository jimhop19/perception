import scrapy

class SpiderPtsSpider(scrapy.Spider):
    name = "spider_pts"
    allowed_domains = ["news.pts.org.tw"]
    
    def start_requests(self):
        yield scrapy.Request(f'https://news.pts.org.tw/search/{self.keyword}')        

    def parse(self, response, **kwargs):
        articles = response.xpath("//ul[@class='list-unstyled search-list relative-news-list-content']/li")

        count = 0
        for article in articles:
            title = article.xpath(".//div/h2/a/text()").get()
            link = article.xpath(".//figure/a/@href").get()
            photo = article.xpath(".//figure/a/div/div/img/@src").get()
            time = article.xpath(".//div/div/time/text()").get().replace(" ","").replace("\n","")
            category = article.xpath(".//div/div/a/text()").get()
            content = article.xpath(".//div/p/text()").get().replace(" ","").replace("\n","")

            yield {
                "title":title,
                "link":link,
                "photo":photo,
                "time":time,
                "category":category,
                "content":content
            }
            count += 1
            if count == 5:
                break    


class SpiderUdnSpider(scrapy.Spider):
    name = "spider_udn"
    allowed_domains = ["udn.com"]

    def start_requests(self):
        yield scrapy.Request(f'https://udn.com/search/word/2/柯')
        print("aaaa")
    
    def parse(self, response, **kwargs):  
        print("bbbb")              
        articles = response.xpath("//div[@class='story-list__news']")
        count = 0    
        print("cccc")
        print(articles)
        for article in articles:            
            photo = article.xpath(".//div[1]/a/picture/img/@src").get()
            link = article.xpath(".//div[1]/a/@href").get()
            title = article.xpath(".//div[2]/h2/a/text()").get()
            content = article.xpath(".//div[2]/p/text()").get()
            time = article.xpath(".//div[2]/div/time/text()").get()
            category = article.xpath(".//div[2]/div/a/text()").get()
            print("dddd")
            yield {
                "title":title,
                "link":link,
                "photo":photo,
                "time":time,
                "category":category,
                "content":content
            }

            count += 1
            if count == 5:
                break

class SpiderLtnSpider(scrapy.Spider):
    name = "spider_ltn"
    allowed_domains = ["search.ltn.com.tw","news.ltn.com.tw"]
    
    def start_requests(self):
        yield scrapy.Request(f'https://search.ltn.com.tw/list?keyword={self.keyword}')        

    def parse(self, response, **kwargs):
        articles = response.xpath("//ul[@class='list boxTitle']/li")
        count = 0
        for article in articles:
            photo = article.xpath(".//a/img/@data-src").get()
            link = article.xpath(".//a/@href").get()
            category = article.xpath(".//div/i/text()").get()          
            title = article.xpath(".//div/a/text()").get()
            content = article.xpath(".//div/p/text()").get()                        
            
            item = {
                    "title": title,
                    "link": link,
                    "photo": photo,                
                    "category": category,
                    "content": content,
                }   
            yield scrapy.Request(url=link,callback=self.parse_time,cb_kwargs={"item":item})   
    
            count += 1
            if count == 5:
                break

    def parse_time(self,response,item):
        item_add_time = item
        item_add_time["time"] =  response.xpath("//span[@class='time']/text()").get()
        yield item_add_time

class SpiderEttodaySpider(scrapy.Spider):
    name = "spider_ettoday"
    allowed_domains = ["www.ettoday.net"]
    
    def start_requests(self):   
        yield scrapy.Request(f"https://www.ettoday.net/news_search/doSearch.php?keywords={self.keyword}&idx=2/")

    def parse(self, response, **kwargs):        
        articles = response.xpath("//div[@class='archive clearfix']")
        count = 0        
        for article in articles:
            photo = article.xpath(".//div[1]/a/img/@src").get()
            link = article.xpath(".//div[1]/a/@href").get()
            category = article.xpath(".//div[2]/p/span[@class='date']/a/text()").get()          
            title = article.xpath(".//div[2]/h2/a/text()").get()
            content = article.xpath(".//div[2]/p/text()").get()
            time = article.xpath(".//div[2]/p/span[@class='date']//text()").getall()[2].replace("/","").replace(")","")
            
            item = {
                    "title": title,
                    "link": link,
                    "photo": photo,                
                    "category": category,
                    "content": content,
                    "time":time
                }   
            yield item
    
            count += 1
            if count == 5:
                break

class SpiderCnaSpider(scrapy.Spider):
    name = "spider_cna"
    allowed_domains = ["cna.com.tw"]
    
    def start_requests(self):
        yield scrapy.Request(f'https://www.cna.com.tw/search/hysearchws.aspx?q={self.keyword}')        

    def parse(self, response, **kwargs):
        articles = response.xpath("//ul[@class='mainList']/li")
        count = 0
        for article in articles:
            link = article.xpath(".//a/@href").get()
            item = {}
            yield scrapy.Request(url=link,callback=self.parse_category_and_content,cb_kwargs={"item":item})   
    
            count += 1
            if count == 5:
                break
    def parse_category_and_content(self,response,item):
        item_add = item
        item_add["category"] = response.xpath("//a[@class='blue']/text()").get()
        item_add["content"] = response.xpath("//div[@class='paragraph']/p[1]/text()").get()
        item_add["title"] = response.xpath("//h1/span/text()").get()
        item_add["time"] = response.xpath("//div[@class='timeBox']/div/span[1]/text()").get()
        item_add["link"] = response.url
        item_add["photo"] = response.xpath(".//div[@class='fullPic']/figure/picture/source/@srcset").get()
        yield item_add

