# -*- coding: utf-8 -*-
import scrapy
from getImages import items


class OinbagSpider(scrapy.Spider):
    name = 'oinbag'
    allowed_domains = ['oinbag.com']
    start_urls = ['http://oinbag.com/']

    def parse(self, response):
        contents = response.xpath('//li[@class="event-img-file"]//a')
        i = 0
        for content in contents:
            i += 1
            item = items.GetimagesItem()
            image_url = content.xpath('@href').extract_first()
            plate_number = content.xpath('img/@alt').extract_first()

            item['filename'] = str(plate_number) + '_' + str(i) + '.jpg'
            item['imageUrl'] = image_url
            # item['plateNumber'] = plate_number

            yield item



