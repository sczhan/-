# -*- coding: utf-8 -*-
import scrapy, re
from 原电脑.wode.kgc.python数据爬取.qcwy.qcwy.items import QcwyItem
a = 2


class QcwySpiderSpider(scrapy.Spider):
    name = 'qcwy_spider'
    allowed_domains = ['51job.com']
    start_urls = [
    'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=',
   "https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E6%258C%2596%25E6%258E%2598,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=",
   "https://search.51job.com/list/000000,000000,0000,00,9,99,%25E7%25AE%2597%25E6%25B3%2595,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=",
   "https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%259C%25BA%25E5%2599%25A8%25E5%25AD%25A6%25E4%25B9%25A0,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=",
   "https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%25B7%25B1%25E5%25BA%25A6%25E5%25AD%25A6%25E4%25B9%25A0,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=",
   "https://search.51job.com/list/000000,000000,0000,00,9,99,%25E4%25BA%25BA%25E5%25B7%25A5%25E6%2599%25BA%25E8%2583%25BD,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="]

    def parse(self, response):
        """招聘名称、职位信息、薪资、职位福利、经验要求、学历要求、公司名称、公司行业、公司性质、公司人数、公司概况）。"""
        job_names = response.xpath('//div[@class="el"]/p/span/a/@title').extract()
        company_names = response.xpath('//div[@class="el"]/span/a/@title').extract()
        addresss = response.xpath('//div[@class="el"]/span[@class="t3"]/text()').extract()
        salarys = response.xpath('//div[@class="el"]/span[@class="t4"]/text()').extract()
        urls = response.xpath('//div[@class="el"]/p/span/a/@href').extract()
        # for job_name, company_name, address, salary in zip(job_names, company_names, addresss, salarys):
        #     # print(job_name, company_name, address, salary)
        print(len(job_names), job_names)
        for ind, url in enumerate(urls):
            job_name_detail = job_names[ind]
            yield scrapy.Request(url, callback=self.parse_response, meta={"job_name_detail": job_name_detail})
        next_page = response.xpath('//a[@id="rtNext"]/@href').extract_first()
        global a
        if a:
            yield scrapy.Request(url=next_page, callback=self.parse)
            a -= 1


    def parse_response(self, response):
        name = response.xpath('//div[@class="cn"]/h1/text()').extract()
        x1 = response.xpath('//div[@class="bmsg job_msg inbox"]/text()').extract()
        x2 = response.xpath('//div[@class="bmsg job_msg inbox"]//p/text()').extract()
        x3 = response.xpath('//div[@class="bmsg job_msg inbox"]/div/text()').extract()
        x4 = response.xpath('//div[@class="bmsg job_msg inbox"]//p/span/text()').extract()
        x5 = response.xpath('//td[@class="font13"]/text()').extract()
        if x1:
            xinxi = x1
            if x2:
                xinxi = x1 + x2
                if x3:
                    xinxi = x1 + x2 + x3
                    if x4:
                        xinxi = x1 + x2 + x3 + x4
        else:
            xinxi = x5
        x = str(xinxi).strip("['',").strip("']").split("\\r\\n        ")
        p = re.compile(r"([0-9\u4e00-\u9fa5、。；（），：]+)")
        xinxi = p.findall(str(x))
        xinzi = response.xpath('//div[@class="cn"]/strong/text()').extract()
        fuli = response.xpath('//div[@class="t1"]//span/text()').extract()
        if fuli == []:
            fuli = "none"
        jinyan = response.xpath('//p[@class="msg ltype"]/span[2]/text()').extract()
        if jinyan == ['|']:
            j = response.xpath('//p[@class="msg ltype"]/@title').extract()
            j = str(j).strip("['").strip("']").split("\\xa0\\xa0|\\xa0\\xa0")
            jinyan = j[1]
        xueli = response.xpath('//p[@class="msg ltype"]/span[3]/text()').extract()
        if xueli == ['|']:
           xueli = j[2]
        gsname = response.xpath('//div[@class="com_msg"]/a/p/text()').extract()
        hangye = response.xpath('//div[@class="com_tag"]/p[3]/a/text()').extract()
        xingzhi = response.xpath('//div[@class="com_tag"]/p[1]/@title').extract()
        renshu = response.xpath('//div[@class="com_tag"]/p[2]/@title').extract()
        gaikuang = response.xpath('//div[@class="tmsg inbox"]/text()').extract()
        gaikuang = re.sub('[""]', "'", str(gaikuang))
        # url = response.meta["url"]
        # job_name = response.meta["job_name"]
        # print(job_name, url)
        # print(name, xinxi, xinzi, fuli, jinyan, xueli, gsname, hangye, xingzhi, renshu, gaikuang)
        job_name = response.meta["job_name_detail"]
        item = QcwyItem()
        item["job_name"] = job_name
        item["xinxi"] = xinxi
        item["xinzi"] = xinzi
        item["fuli"] = fuli
        item["jinyan"] = jinyan
        item["xueli"] = xueli
        item["gsname"] = gsname
        item["hangye"] = hangye
        item["xingzhi"] = xingzhi
        item["renshu"] = renshu
        item["gaikuang"] = gaikuang
        yield item
