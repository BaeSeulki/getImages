# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GetimagesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    plateNumber = scrapy.Field()
    imageUrl = scrapy.Field()
    filename = scrapy.Field()
