# -*- coding: utf-8 -*-
import scrapy


class HomeworkSpiderSpider(scrapy.Spider):
    name = 'homework_spider'
    allowed_domains = ['www.sohu.com']
    # start_urls = ['http://www.sohu.com/']

    def parse(self, response):
        print("爬虫启动成功")

    def start_requests(self):
        yield scrapy.Request(url="http://www.sohu.com/", callback=self.parse)
        # yield scrapy.FormRequest()