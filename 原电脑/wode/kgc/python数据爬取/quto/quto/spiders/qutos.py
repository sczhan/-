# -*- coding: utf-8 -*-
import scrapy
a = 10

class QutosSpider(scrapy.Spider):
    name = 'qutos'
    allowed_domains = ['51job.com']
    start_urls = [
        'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']

    def parse(self, response):
        """招聘名称、职位信息、薪资、职位福利、经验要求、学历要求、公司名称、公司行业、公司性质、公司人数、公司概况）。"""
        job_names = response.xpath('//div[@class="el"]/p/span/a/@title').extract()
        company_names = response.xpath('//div[@class="el"]/span/a/@title').extract()
        addresss = response.xpath('//div[@class="el"]/span[@class="t3"]/text()').extract()
        salarys = response.xpath('//div[@class="el"]/span[@class="t4"]/text()').extract()
        urls = response.xpath('//div[@class="el"]/p/span/a/@href').extract()
        for job_name, company_name, address, salary in zip(job_names, company_names, addresss, salarys):
            print(job_name, company_name, address, salary)
        next_page = response.xpath('//a[@id="rtNext"]/@href').extract_first()
        global a
        # print(response.meta["proxy"], 'spider')
        if a:
            yield scrapy.Request(url=next_page, callback=self.parse)
            a -= 1