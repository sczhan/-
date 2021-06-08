# -*- coding: utf-8 -*-
import scrapy
from 原电脑.wode.kgc.python数据爬取.qcwy_sp.qcwy_sp.items import QcwySpItem
import datetime
from pybloom_live import BloomFilter
import os

class QcwySpSpiderSpider(scrapy.Spider):
    name = 'qcwy_sp_spider'
    # allowed_domains = ['example.com']
    start_urls = [
    # 关键字: 数据分析
    'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=',
    # 关键字: 数据挖掘
    "https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E6%258C%2596%25E6%258E%2598,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=",
    # # 关键字: 算法
    "https://search.51job.com/list/000000,000000,0000,00,9,99,%25E7%25AE%2597%25E6%25B3%2595,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=",
    # # 关键字: 机器学习
    "https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%259C%25BA%25E5%2599%25A8%25E5%25AD%25A6%25E4%25B9%25A0,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=",
    # # 关键字: 深度学习
    "https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%25B7%25B1%25E5%25BA%25A6%25E5%25AD%25A6%25E4%25B9%25A0,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=",
    # # 关键字: 人工智能
    "https://search.51job.com/list/000000,000000,0000,00,9,99,%25E4%25BA%25BA%25E5%25B7%25A5%25E6%2599%25BA%25E8%2583%25BD,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    ]

    start_url_tags = ["数据分析",
                      "数据挖掘", "算法", "机器学习", "深度学习", "人工智能",
                      ]

    def __init__(self):
        self.url_filter = None
        self.url_filter_file = None
        self.record_data = datetime.datetime.now().strftime("%Y-%m-%d")

    def start_requests(self):
        for index in range(len(self.start_urls)):
            url = self.start_urls[index]
            tag = self.start_url_tags[index]
            yield scrapy.Request(url, callback=self.parse, meta={"tag": tag}, dont_filter=True)


    def parse(self, response):
        tag = response.meta["tag"]
        items = response.xpath('//div[@class="el"]/p')
        # next_page_url = response.xpath('//ul/li[@class="bk"]/a/@href').extract()[1]
        next_page_url = response.xpath('//a[@id="rtNext"]/@href').extract_first()
        # print(len(items))
        for item in items:
            url = item.xpath("./span/a/@href").extract_first()
            # print(url)
            title = item.xpath("./span/a/text()").extract_first()
            if tag == "算法" and not ("算法" in title):
                continue
            if not self.is_url_in_bloom_filter(tag+url):
                yield scrapy.Request(url, callback=self.datail_parse, meta={"tag": tag}, dont_filter=True)
        # print(next_page_url)
        if not next_page_url is None:
            yield scrapy.Request(next_page_url, callback=self.parse, meta={"tag": tag}, dont_filter=True)

        # print(len(items))

    def datail_parse(self, response):

        """
        :param response:
        :return:
        """
        self.save_tag_url_to_file(response.meta["tag"] + response.url)
        item = QcwySpItem()
        item["job_tag"] = response.meta["tag"]
        item["job_url"] = response.url
        item["job_name"] = response.xpath('//div[@class="cn"]/h1/text()').extract_first()
        item["record_data"] = self.record_data

        # item["job_info"] = "".join(response.xpath('//div[@class="bmsg job_msg inbox"]//text()').extract()).strip()
        job_infos = response.xpath('//div[@class="bmsg job_msg inbox"]//text()').extract()
        job_info = []
        for i in job_infos:
            job_info.append(str(i).strip("\n").strip())
        item["job_info"] = "".join(job_info).strip()
        item["jon_salary"] = response.xpath('//div[@class="cn"]/strong/text()').extract_first()
        item["job_welfare"] = "|".join(response.xpath('//p[@class="msg ltype"]/text()').extract()).strip()
        job_exp_require = response.xpath('//p[@class="msg ltype"]/text()').extract()
        # job_edu_require = response.xpath('//p[@class="msg ltype"]/text()').extract()[2].strip()
        if job_exp_require is []:
            item["job_exp_require"] = "none"
            item["job_edu_require"] = "none"
            item["job_country"] = "none"
        else:
            item["job_country"] = job_exp_require[0].strip()
            item["job_exp_require"] = job_exp_require[1].strip()
            item["job_edu_require"] = job_exp_require[2].strip()
        item["company_name"] = response.xpath('//a[@class="com_name himg"]/p/text()').extract_first()
        item["company_industry"] = response.xpath('//span[@class="i_flag"]/../text()').extract_first()
        item["company_people"] = response.xpath('//span[@class="i_people"]/../text()').extract_first()
        item["company_location"] = response.xpath('//p[@class="msg ltype"]/text()[1]').extract_first().strip()
        company_overviews = response.xpath('//div[@class="tmsg inbox"]/text()').extract()
        company_overview = []
        for i in company_overviews:
            company_overview.append(str(i).strip("\n").strip())

        item["company_overview"] = "".join(company_overview).strip()
        item["company_financing_stage"] = response.xpath('//a[@class="com_name himg"]/p/text()').extract()
        yield item

    def get_filter(self):
        if self.url_filter is None:
            self.url_filter = BloomFilter(100000, 0.01)
            # url_filter.txt
            if os.path.exists("./url_filter.txt"):
                self.url_filter_file = open("./url_filter.txt", "a+")
                self.url_filter_file.seek(0)
                for line in self.url_filter_file.readlines():
                    self.url_filter.add(line.strip("\n"))
            else:
                # print(1)
                self.url_filter_file = open("./url_filter.txt", "a+")

        return self.url_filter


    def is_url_in_bloom_filter(self, tag_url):
        result = self.get_filter().add(tag_url)
        return result


    def save_tag_url_to_file(self, tag_url):
        self.url_filter_file.write(tag_url + "\n")
        self.url_filter_file.flush()


    def closed(self, reason):
        self.url_filter_file.close()
        del self.url_filter
