# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class BooksscrapyPipeline(object):
    # 爬虫开始前执行一次（初始化工作）
    def open_spider(self,spider):
        # 连接MongoDb数据库服务器
        self.db_client = pymongo.MongoClient()
        # 指定操作的数据库
        self.db = self.db_client['scrape']
        # 指定集合（类似MYSQL中的表）
        self.db_collection = self.db['movies']

    def process_item(self,item,spider):
        # 处理数据
       self.db_collection.insert_one(dict(item))
       return item

    # 爬虫全部完成后执行一次（收尾工作）
    def close_spider(self,spider):
        self.db_client.close()



