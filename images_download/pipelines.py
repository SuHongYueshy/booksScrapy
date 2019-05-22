# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class ImagesDownloadPipeline(ImagesPipeline):
    #生成下载的图片的Request
    def get_media_requests(self, item, info):
        return [Request(x,meta={"title":item["title"]}) for x in item.get(self.images_urls_field, [])]

    #确定目录以及图片名称
    def file_path(self, request, response=None, info=None):
        image_name = request.url.split("/")[-1]
        title = request.meta["title"]
        return '%s/%s' % (title,image_name)
