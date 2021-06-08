# -*- coding: utf-8 -*-
import scrapy


class SohuSpider(scrapy.Spider):
    name = 'sohu'
    allowed_domains = ['suhu.com']
    start_urls = ['https://www.sohu.com/']

    def parse(self, response):
        # print(response.body.decode("utf-8"))
        href = response.xpath("//a/@href").extract()
        print(href)
