# -*- coding: utf-8 -*-
import scrapy
from getImages import items


class OinbagSpider(scrapy.Spider):
    name = 'oinbag'
    allowed_domains = ['oinbag.com']
    start_urls = ['http://oinbag.com/']
    # website_possible_httpstatus_list = [500, 503, 504, 400, 403, 404, 408]
    # handle_httpstatus_list = [403]

    def parse(self, response):
        # if response.body == "banned":
        #     req = response.request
        #     req.meta["change_proxy"] = True
        #     yield req
        # else:
            contents = response.xpath('//li[@class="event-img-file"]')
            i = 0
            plate_number_before = ""
            for content in contents:
                i += 1
                item = items.GetimagesItem()
                image_url = content.xpath('@path').extract_first()
                plate_number = content.xpath('a/img/@alt').extract_first()

                if plate_number != plate_number_before:
                    i = 1

                item['filename'] = str(plate_number) + '_' + str(i) + '.jpg'
                item['imageUrl'] = image_url

                plate_number_before = plate_number

                yield item



