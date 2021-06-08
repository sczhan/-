# -*- coding: utf-8 -*-
import scrapy, time
from selenium import webdriver
# from selenium.webdriver.common import action_chains

class TianmaosSpider(scrapy.Spider):
    name = 'tianmaos'
    # allowed_domains = ['tmall.com']
    start_urls = ["https://detail.tmall.com/item.htm?id=555358967936"]

    def __init__(self):
        super(TianmaosSpider, self).__init__()
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        self.driver = webdriver.Chrome(executable_path='F:\wode\kgc\python数据爬取\chromedriver.exe',
                                       chrome_options=options)



    def parse(self, response):
        # options = webdriver.ChromeOptions()
        # options.add_argument("headless")
        # driver = webdriver.Chrome(executable_path='F:\wode\kgc\python数据爬取\chromedriver.exe',
        #                                chrome_options=options)
        # driver.get(response.url)
        # action_chain = action_chains.ActionChains(self.driver)
        # a = self.driver.find_element_by_id("sufei-dialog-close")
        # print(a,  1)
        # action_chain.click(a).perform()
        print(response.body)
        print(response.url)

        detail_price = response.xpath('//span[@class="tm-price"]/text()').extract()
        picture_list = response.xpath('//img[@id="J_ImgBooth"]/@src').extract()
        title = response.xpath('//div[@class="tb-detail-hd"]/h1/text()').extract()
        print(detail_price, picture_list, title)


    def close(self, spider):
        self.driver.quit()
        print("closed spider")
