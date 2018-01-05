# -*- coding: utf-8 -*-
import requests
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GetimagesPipeline(object):
    def process_item(self, item, spider):
        imagename = item['filename']
        image_url = item['imageUrl']
        image = requests.get(image_url)

        print(imagename)

        with open("/home/zhouyu/PlateImages/" + imagename, 'wb') as f:
            f.write(image.content)

        return item
