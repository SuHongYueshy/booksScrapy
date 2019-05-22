from scrapy.spiders import Spider#爬虫模块
from scrapy import Request#请求模块
import re
from booksScrapy.items import BooksscrapyItem#导入Item类

class booksSpider(Spider):
    name = "books"#爬虫的名称
    #start_urls = ["http://books.toscrape.com/"]

    def start_requests(self):
        url = "http://books.toscrape.com/catalogue/page-1.html"
        yield Request(url,callback=self.parse_books)

    #提取并解析home页的数据
    def parse_books(self,response):
        #数据提取功能
        li_selector = response.xpath("//ol/li")
        for li in li_selector:
            item = BooksscrapyItem()#生成了Item类的对象
            name = li.xpath("article/h3/a/text()").extract_first()
            price = li.xpath("article/div[last()]/p[@class='price_color']/text()").extract()[0]
            main_url = li.xpath("article/div[@class='image_container']/a/@href").extract_first()
            main_url = "http://books.toscrape.com/catalogue/"+main_url
            item["name"] = name#书籍名称
            item["price"] = price#价格
            #发送访问详细页的请求
            yield Request(main_url,callback=self.parse_content,meta={"myitem":item})


        next_url = response.xpath("//li[@class='next']/a/@href").extract()
        if next_url:
            next_url="http://books.toscrape.com/catalogue/page-"+re.sub("\D","",next_url[0])+".html"
            yield Request(next_url,callback=self.parse_books)

    #提取并解析详细页的数据
    def parse_content(self,response):
        content = response.xpath("//article/p/text()").extract_first()
        item = response.meta["myitem"]
        item["content"]=content
        yield item


