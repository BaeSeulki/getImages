# -*- coding: utf-8 -*-
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from getImages import settings


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GetimagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_urls = item['image_urls']
        for image_url in image_urls:
            yield scrapy.Request(image_url)
            # yield scrapy.Request(image_url, meta={'item': item, 'index': item['image_urls'].index(image_url)})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        print("正在下载： ", item['filename'])
        return item

    # def file_path(self, request, response=None, info=None):
    #     item = request.meta['item']
    #     index = request.meta['index']
