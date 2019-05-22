# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class No1ShopItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()#名称
    price = scrapy.Field()#价格
    comment = scrapy.Field()#好评率
    shop = scrapy.Field()#店铺名称
