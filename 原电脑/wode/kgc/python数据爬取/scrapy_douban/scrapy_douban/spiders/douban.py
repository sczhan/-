# -*- coding: utf-8 -*-
import scrapy, re, redis
from kgc.python数据爬取.scrapy_douban.scrapy_douban.items import ScrapyDoubanItem
from scrapy_redis.spiders import RedisSpider

class DoubanSpider(RedisSpider):
    name = 'douban'
    # allowed_domains = ['douban.com']
    # start_urls = ['https://movie.douban.com/top250']
    redis_key = "douban:start_urls"
    # pre_url = "https://movie.douban.com"

    def parse(self, response):
        # print(response.status)
        # print(response.body.decode("utf-8"))
        # title = response.xpath('//ol[@class="grid_view"]/li//div[@class="hd"]/a/span[1]/text()').extract()
        titles = response.css(".hd > a >span:nth-child(1)::text").extract()
        ranks = response.css(".pic > em::text").extract()
        abstracts = []
        abs = response.xpath('//div[@class="info"]/div[@class="bd"]')
        for ab in abs:
            a = ab.xpath('p[@class="quote"]/span[@class="inq"]/text()').extract()
            if a == []:
                a = None
            else:
                a = a[0]
            abstracts.append(a)
        # print(abstracts, len(abstracts))
        detail_pages = response.css(".hd > a::attr(href)").extract()
        print(len(detail_pages), detail_pages)
        for ind, detail_page in enumerate(detail_pages):
            # print(detail_page, title, abstract, rank)
            abstract_detail = abstracts[ind]
            title_detail = titles[ind]
            rank_detail = ranks[ind]
            yield scrapy.Request(url=detail_page, callback=self.parse_detail, meta={"abstract_detail": abstract_detail,
                                                                                    "title_detail": title_detail,
                                                                                    "rank_detail": rank_detail})
        # print(abstract, detail_pages)
        next_page = response.css(".next > a::attr(href)").extract_first()
        base_url = "https://movie.douban.com/top250"
        # print(next_page)
        # if next_page:
        # #     print(next_page)
        #     yield scrapy.Request(url=base_url + next_page, callback=self.parse)

        # print(len(title), title)


    def parse_detail(self, response):
        score = response.xpath('//div[@class="rating_self clearfix"]/strong/text()').extract()[0]
        print(score)
        abstract_detail = response.meta["abstract_detail"]
        title_detail = response.meta["title_detail"]
        rank_detail = response.meta["rank_detail"]
        # print(abstract_detail, score)
        describe = response.xpath('//span[@property="v:summary"]/text()').extract_first()
        describe = str(describe).strip("\n").strip("'                                    \u3000\u3000'").strip("'\u3000\u3000").strip("\n")
        describe = re.sub('[""]', "'", str(describe))


        # print(describe)
        # number = re.findall("[0-9]+", describe)
        # print(number)
        # letter = re.findall("[a-zA-Z]+", describe)
        # print(letter)
        # print(describe)
        item = ScrapyDoubanItem()
        item["rank_detail"] = rank_detail
        item["title_detail"] = title_detail
        item["score"] = score
        item["abstract_detail"] = abstract_detail
        item["describe"] = describe
        # print(item)
        yield item
        # print(item)