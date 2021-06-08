# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver

class ExampleSpider(scrapy.Spider):
    name = 'jd'
    # allowed_domains = ['example.com']
    start_urls = ['https://item.jd.com/100011495854.html']
    def __init__(self):
        super(ExampleSpider, self).__init__()
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        self.driver = webdriver.Chrome(executable_path='F:\wode\kgc\python数据爬取\chromedriver.exe', chrome_options=options)

    def parse(self, response):
        # print(response.body)
        detail_price = response.xpath('//span[@class="p-price"]/span[2]/text()').extract()
        picture_list = response.xpath('//div[@class="sku-name"]/img/@src').extract()
        title = response.xpath('//div[@class="sku-name"]/text()').extract()
        print(detail_price, picture_list, title)


    def close(self, spider):
        self.driver.quit()
        print("closed spider")
