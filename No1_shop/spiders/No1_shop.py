from scrapy import Request
from scrapy.spiders import Spider
from No1_shop.items import No1ShopItem#导入Item模块
from selenium import webdriver#导入浏览器引擎模块

class No1_shopSpider(Spider):
    # 定义名称
    name = 'No1_shop'

    # 构造函数
    def __init__(self):
        # 创建PhantomJS的对象driver
        self.driver = webdriver.Chrome()

    # 获取初始Request
    def start_requests(self):
        url = 'https://search.yhd.com/c0-0/kiphone/'

        # 生成请求对象，设置url
        yield Request(url)

    def parse(self, response):
        item = No1ShopItem()
        list_selector = response.xpath()
        for li in list_selector:
            try:
                # 标题
                title = li.xpath(".//a[@class='hd_search_ipt']/text()").extract()
                # 去除空格
                title = title[0].strip(" ")
                # 价格
                price = li.xpath(".//a[@class='proPrice']/text()").extract()
                # 好评率
                comment = li.xpath(".//a[@class='positiveRatio']/text()").extract()
                # 去除文字及空格
                comment = comment.re("(.*?)评论")[0]
                comment = "".join(comment.split())  # 去除空格：&nbsp
                #  店铺名称
                shop = li.xpath(".//a[@class='shop_text']/text()").extract()
                item["title"] = title  # 标题
                item["price"] = price  # 价格
                item["comment"] = comment  # 评论
                item["shop"] = shop  # 店铺名称
                yield item
            except:
                continue

