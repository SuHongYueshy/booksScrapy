# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImagesDownloadItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()#主题
    image_urls = scrapy.Field()#图片url地址
    images = scrapy.Field()#下载后的结果
