import scrapy
import re
from scrapy_playwright.page import PageMethod

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
            time_original = article.xpath(".//div/div/time/text()").get().replace("\n","")
            time = re.search(r'\d.*\d',time_original).group()
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
        yield scrapy.Request(f'https://udn.com/search/word/2/{self.keyword}')        
    
    def parse(self, response, **kwargs):          
        articles = response.xpath("//div[@class='story-list__news']")
        count = 0    
        
        for article in articles:            
            photo = article.xpath(".//div[1]/a/picture/source/@data-srcset").get()
            link = article.xpath(".//div[1]/a/@href").get()
            title = article.xpath(".//div[2]/h2/a/text()").get()
            content = article.xpath(".//div[2]/p/text()").get()
            time = article.xpath(".//div[2]/div/time/text()").get()
            category = article.xpath(".//div[2]/div/a/text()").get()            
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
        item_add_time["time"] =  response.xpath("//span[@class='time']/text()").get().replace("\n    ","").replace("/","-")
        yield item_add_time

class SpiderLtnAllNewsSpider(scrapy.Spider):
    name = "spider_ltn_all"
    allowed_domains = ["search.ltn.com.tw","news.ltn.com.tw"]
    
    def start_requests(self):
        
        yield scrapy.Request("https://news.ltn.com.tw/list/breakingnews/politics", meta=dict(
                playwright=True,
                playwright_include_page=True,
                playwright_page_methods=[
                    (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    (PageMethod("wait_for_timeout",300)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),
                    # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
                    # (PageMethod("wait_for_timeout",200)),                    
                ]
            ),)
        

    async def parse(self, response, **kwargs):
        print(f'this is {response}')
        page = response.meta["playwright_page"]
        await page.close()
        
        articles = response.xpath("//div[@class='whitecon boxTitle']/ul/li")
        
        for article in articles:
            photo = article.xpath(".//a/img/@data-src").get()
            link = article.xpath(".//a/@href").get()
            title = article.xpath(".//a/@title").get()
            
            item = {
                    "title": title,
                    "link": link,
                    "photo": photo,
                }
            print(item)
            yield scrapy.Request(url=link,callback=self.parse_time,cb_kwargs={"item":item})

    def parse_time(self,response,item):
        item_add_time = item
        item_add_time["time"] =  response.xpath("//span[@class='time']/text()").get()
        paragraphs = response.xpath("//div[@class='text boxTitle boxText']/p")
        article = []
        for paragraph in paragraphs:            
            if paragraph.xpath(".//@class").get() == None and paragraph.xpath(".//text()").get() != None:
                article.append(paragraph.xpath(".//text()").get())
        item_add_time["content"] = article        
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
        text= response.xpath("//div[@class='paragraph']/p[1]/text()").get()
        if text != None:
            if re.search("電）",text) != None:                        
                text = text.split("）")[1]
            if re.search("（編輯",text) != None:
                text = text.split("（")[0]
        item_add["content"] = text
        item_add["title"] = response.xpath("//h1/span/text()").get()
        item_add["time"] = response.xpath("//div[@class='timeBox']/div/span[1]/text()").get().replace("/","-")
        item_add["link"] = response.url
        item_add["photo"] = response.xpath(".//div[@class='fullPic']/figure/picture/source/@srcset").get()
        yield item_add


# Below for whole paragraph

# class SpiderPtsSpider(scrapy.Spider):
#     name = "spider_pts"
#     allowed_domains = ["news.pts.org.tw"]
    
#     def start_requests(self):
#         yield scrapy.Request(f'https://news.pts.org.tw/search/{self.keyword}')        

#     def parse(self, response, **kwargs):

#         articles = response.xpath("//ul[@class='list-unstyled search-list relative-news-list-content']/li")

#         count = 0
#         for article in articles:
#             title = article.xpath(".//div/h2/a/text()").get()
#             link = article.xpath(".//figure/a/@href").get()
#             photo = article.xpath(".//figure/a/div/div/img/@src").get()
#             time_original = article.xpath(".//div/div/time/text()").get().replace("\n","")
#             time = re.search(r'\d.*\d',time_original).group()
#             category = article.xpath(".//div/div/a/text()").get()            
            
#             item = {
#                 "title":title,
#                 "link":link,
#                 "photo":photo,
#                 "time":time,
#                 "category":category                
#             }
#             yield scrapy.Request(url=link,callback=self.parse_time,cb_kwargs={"item":item})
#             count += 1
#             if count == 5:
#                 break

            
                

#     def parse_time(self,response,item):
#         item_add_tags_and_article = item
#         tag = []
#         content = []
#         blue_tags = response.xpath("//div[@class='col-lg-8']/ul[@class='list-unstyled tag-list list-flex d-flex']/li")
#         for blue_tag in blue_tags:
#             word = blue_tag.xpath(".//a/text()").get()
#             if word != "...":
#                 tag.append(word)

#         summary = response.xpath("//div[@class='post-article text-align-left']/div/text()").get()
#         content.append(summary)

#         paragraphs = response.xpath("//div[@class='post-article text-align-left']/p")
#         for paragraph in paragraphs:
#             text = paragraph.xpath(".//text()").get()
#             content.append(text)

#         item_add_tags_and_article["tag"] = tag
#         item_add_tags_and_article["content"] = content
        
#         yield item_add_tags_and_article
               


# class SpiderUdnSpider(scrapy.Spider):
#     name = "spider_udn"
#     allowed_domains = ["udn.com"]

#     def start_requests(self):
#         yield scrapy.Request(f'https://udn.com/search/word/2/{self.keyword}')        
    
#     def parse(self, response, **kwargs):          

#         articles = response.xpath("//div[@class='story-list__news']")

#         count = 0
#         for article in articles:            
#             photo = article.xpath(".//div[1]/a/picture/source/@data-srcset").get()
#             link = article.xpath(".//div[1]/a/@href").get()
#             title = article.xpath(".//div[2]/h2/a/text()").get()            
#             time = article.xpath(".//div[2]/div/time/text()").get()
#             category = article.xpath(".//div[2]/div/a/text()").get()            
#             item = {
#                 "title":title,
#                 "link":link,
#                 "photo":photo,
#                 "time":time,
#                 "category":category,                
#             }
#             yield scrapy.Request(url=link,callback=self.parse_time,cb_kwargs={"item":item})
#             count += 1
#             if count == 5:
#                 break  
                        

#     def parse_time(self,response,item):
#         item_add_tags_and_article = item
#         tagArray = []
#         content = []
#         tags = response.xpath("//section[@class='keywords']/a")
#         for tag in tags:
#             word = tag.xpath(".//text()").get()            
#             tagArray.append(word)        

#         paragraphs = response.xpath("//section[@class='article-content__editor ']/p")        
#         for paragraph in paragraphs:            
#             text = paragraph.xpath(".//text()").getall()
#             if text != []:
#                 x="".join(text).replace("\r\n","").replace(" ","")
#                 if re.search("image",x) == None:
#                     if x != "" and len(x) > 1:
#                         content.append(x)


#         item_add_tags_and_article["tag"] = tagArray
#         item_add_tags_and_article["content"] = content
        
#         yield item_add_tags_and_article

            

# class SpiderLtnSpider(scrapy.Spider):
#     name = "spider_ltn"
#     allowed_domains = ["search.ltn.com.tw","news.ltn.com.tw"]
    
#     def start_requests(self):
#         yield scrapy.Request(f'https://search.ltn.com.tw/list?keyword={self.keyword}')        

#     def parse(self, response, **kwargs):        
        
#         articles = response.xpath("//ul[@class='list boxTitle']/li")

#         count = 0      
#         for article in articles:
#             photo = article.xpath(".//a/img/@data-src").get()
#             link = article.xpath(".//a/@href").get()
#             category = article.xpath(".//div/i/text()").get()          
#             title = article.xpath(".//div/a/text()").get()                           
            
#             item = {
#                     "title": title,
#                     "link": link,
#                     "photo": photo,                
#                     "category": category,                    
#                     "tag":[],
#                 }   
#             yield scrapy.Request(url=link,callback=self.parse_time,cb_kwargs={"item":item})
#             count += 1
#             if count == 5:
#                 break
                

#     def parse_time(self,response,item):       
#         item_add_time = item
#         item_add_time["time"] =  response.xpath("//span[@class='time']/text()").get().replace("\n    ","").replace("/","-")
#         paragraphs = response.xpath("//div[@class='text boxTitle boxText']/p")
#         article = []
#         for paragraph in paragraphs:            
#             if paragraph.xpath(".//@class").get() == None and paragraph.xpath(".//text()").get() != None:
#                 text = paragraph.xpath(".//text()").get()                
#                 if re.search("〕",text) == None:
#                     article.append(text)
#                 else:
#                     article.append(text.split("〕")[1])
#         item_add_time["content"] = article        
#         yield item_add_time

# class SpiderLtnAllNewsSpider(scrapy.Spider):
#     name = "spider_ltn_all"
#     allowed_domains = ["search.ltn.com.tw","news.ltn.com.tw"]
    
#     def start_requests(self):
        
#         yield scrapy.Request("https://news.ltn.com.tw/list/breakingnews/politics", meta=dict(
#                 playwright=True,
#                 playwright_include_page=True,
#                 playwright_page_methods=[
#                     (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     (PageMethod("wait_for_timeout",300)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),
#                     # (PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)")),
#                     # (PageMethod("wait_for_timeout",200)),                    
#                 ]
#             ),)
        

#     async def parse(self, response, **kwargs):        
#         page = response.meta["playwright_page"]
#         await page.close()
        
#         articles = response.xpath("//div[@class='whitecon boxTitle']/ul/li")
        
#         for article in articles:
#             photo = article.xpath(".//a/img/@data-src").get()
#             link = article.xpath(".//a/@href").get()
#             title = article.xpath(".//a/@title").get()
            
#             item = {
#                     "title": title,
#                     "link": link,
#                     "photo": photo,
#                 }
            
#             yield scrapy.Request(url=link,callback=self.parse_time,cb_kwargs={"item":item})
            

#     def parse_time(self,response,item):
#         item_add_time = item
#         item_add_time["time"] =  response.xpath("//span[@class='time']/text()").get()
#         paragraphs = response.xpath("//div[@class='text boxTitle boxText']/p")
#         article = []
#         for paragraph in paragraphs:            
#             if paragraph.xpath(".//@class").get() == None and paragraph.xpath(".//text()").get() != None:
#                 text = paragraph.xpath(".//text()").get()                
#                 article.append(text)
#         item_add_time["content"] = article        
#         yield item_add_time

    
# class SpiderEttodaySpider(scrapy.Spider):
#     name = "spider_ettoday"
#     allowed_domains = ["www.ettoday.net"]
    
#     def start_requests(self):   
#         yield scrapy.Request(f"https://www.ettoday.net/news_search/doSearch.php?keywords={self.keyword}&idx=2/")

#     def parse(self, response, **kwargs):

#         articles = response.xpath("//div[@class='archive clearfix']")
#         count = 0           
#         for article in articles:
#             photo = article.xpath(".//div[1]/a/img/@src").get()
#             link = article.xpath(".//div[1]/a/@href").get()
#             category = article.xpath(".//div[2]/p/span[@class='date']/a/text()").get()          
#             title = article.xpath(".//div[2]/h2/a/text()").get()
#             content = article.xpath(".//div[2]/p/text()").get()
#             time = article.xpath(".//div[2]/p/span[@class='date']//text()").getall()[2].replace("/","").replace(")","")
            
#             item = {
#                     "title": title,
#                     "link": link,
#                     "photo": photo,                
#                     "category": category,
#                     "content": content,
#                     "time":time,
#                     "tag":[]
#                 }   
#             yield scrapy.Request(url=link,callback=self.parse_time,cb_kwargs={"item":item})
#             count += 1
#             if count == 5:
#                 break
        
            
#     def parse_time(self,response,item):
#         item_add_content = item        
#         paragraphs = response.xpath("//div[@class='story']/p")
#         article = []
#         for paragraph in paragraphs:            
#             text = paragraph.xpath(".//text()").get()
#             if text != None and re.search("圖／",text) == None:                
#                 article.append(text)                
#         item_add_content["content"] = article[1:]       
#         yield item_add_content 

# class SpiderCnaSpider(scrapy.Spider):
#     name = "spider_cna"
#     allowed_domains = ["cna.com.tw"]
    
#     def start_requests(self):
#         yield scrapy.Request(f'https://www.cna.com.tw/search/hysearchws.aspx?q={self.keyword}')        

#     def parse(self, response, **kwargs):
#         articles = response.xpath("//ul[@class='mainList']/li")

#         count = 0
#         for article in articles:
#             link = article.xpath(".//a/@href").get()
#             item = {}
#             yield scrapy.Request(url=link,callback=self.parse_category_and_content,cb_kwargs={"item":item})
#             count += 1
#             if count == 5:
#                 break
               
#     def parse_category_and_content(self,response,item):
#         item_add = item
#         item_add["category"] = response.xpath("//a[@class='blue']/text()").get()
#         item_add["title"] = response.xpath("//h1/span/text()").get()
#         item_add["time"] = response.xpath("//div[@class='timeBox']/div/span[1]/text()").get().replace("/","-")
#         item_add["link"] = response.url
#         item_add["photo"] = response.xpath("//div[@class='fullPic']/figure/picture/source/@srcset").get()
#         tag = []
#         tag_group =response.xpath("//div[@class='paragraph']/div[1]/div")
#         for tag_tag in tag_group:
#             text = tag_tag.xpath(".//a/text()").get()
#             if text != None:
#                 tag.append(text.replace("#",""))
#         item_add["tag"] = tag
#         article = []
#         paragraphs = response.xpath("//div[@class='paragraph']/p")
#         for paragraph in paragraphs:            
#             text = paragraph.xpath(".//text()").get()            
#             if text != None:
#                 if re.search("電）",text) != None:                        
#                     article.append(text.split("）")[1])
#                 elif re.search("（編輯",text) != None:
#                     article.append(text.split("（")[0])
#                 else:
#                     article.append(text)
#         last_item_index = len(article)-1
#         item_add["content"] = article[:last_item_index]         
        
#         yield item_add

