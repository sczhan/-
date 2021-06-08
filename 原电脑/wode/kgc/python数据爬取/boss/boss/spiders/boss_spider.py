# -*- coding: utf-8 -*-
import scrapy
import requests
from fake_useragent import UserAgent
from scrapy.selector import Selector
import time, re
from selenium import webdriver


class BossSpiderSpider(scrapy.Spider):
    name = 'boss_spider'
    # allowed_domains = ['zhipin.com']
    start_urls = ["https://www.zhipin.com/job_detail/?query=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0&city=100010000&industry=&position=",
        # "https://www.zhipin.com/job_detail/?query=机器学习&city=100010000&industry=&position=",
                  "https://www.zhipin.com/job_detail/?query=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&city=100010000&industry=&position=",
                  # "https://www.zhipin.com/job_detail/?query=深度学习&city=100010000&industry=&position=",
                  "https://www.zhipin.com/job_detail/?query=%E5%9B%BE%E5%83%8F%E7%AE%97%E6%B3%95&city=100010000&industry=&position=",
                  # "https://www.zhipin.com/job_detail/?query=图像算法&city=100010000&industry=&position=",
                  "https://www.zhipin.com/job_detail/?query=%E5%9B%BE%E5%83%8F%E5%A4%84%E7%90%86&city=100010000&industry=&position=",
                  # "https://www.zhipin.com/job_detail/?query=图像处理&city=100010000&industry=&position=",
                  "https://www.zhipin.com/job_detail/?query=%E8%AF%AD%E9%9F%B3%E8%AF%86%E5%88%AB&city=100010000&industry=&position="
                  # "https://www.zhipin.com/job_detail/?query=语音识别&city=100010000&industry=&position=",
                  # "https://www.zhipin.com/job_detail/?query=图像识别&city=100010000&industry=&position=",
                  # "https://www.zhipin.com/job_detail/?query=算法研究员&city=100010000&industry=&position=",
                  # "https://www.zhipin.com/job_detail/?query=数据挖掘&city=100010000&industry=&position=",
                  # "https://www.zhipin.com/job_detail/?query=数据分析师&city=100010000&industry=&position=",
                ]
    print(len(start_urls))
    start_url_tag = ["机器学习", "深度学习", "图像算法", "图像处理", "语音识别"]
    fake_start_url = "http://example.com/"
    headers = {
        "authority": "www.zhipin.com",
        "method": "GET",
        "path": "/job_detail/?query=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0&city=100010000&industry=&position=",
        "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        # "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
         "cookie": "_uab_collina=159071905074371533234384; __zp__pub__=; lastCity=100010000; __c=1592189159; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1592113817,1592114026,1592114034,1592189159; __l=l=%2Fwww.zhipin.com%2Fjob_detail%2F%3Fquery%3D%25E8%25AF%25AD%25E9%259F%25B3%25E8%25AF%2586%25E5%2588%25AB%26city%3D100010000%26industry%3D%26position%3D&r=&friend_source=0&friend_source=0; __a=15264055.1590719051.1592113817.1592189159.203.6.25.94; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1592206847; __zp_stoken__=8302aI2NkGiUDYEkYeEhManV7YmsBY3lRHXwzb0B6YUJZGWYoOj5mWW9oXxUXU1QWPC49OwYGd0cXA0JACVFMcjEsARtWfkY1AR0IOTIONmgISV9wRQIaJRoafWMsOwkMfhd4RHsAdk1aTT4%3D",
        "referer": "https://www.zhipin.com/web/common/security-check.html?seed=KQ0%2FXRObskKCU8m1xH2xdJwZcrW7K8ll3m%2FqNa0pZAs%3D&name=cbb40b57&ts=1591954290962&callbackUrl=%2Fjob_detail%2F%3Fquery%3D%25E6%259C%25BA%25E5%2599%25A8%25E5%25AD%25A6%25E4%25B9%25A0%26city%3D100010000%26industry%3D%26position%3D&srcReferer=https%3A%2F%2Fwww.zhipin.com%2F",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
    }


    def __init__(self):
        self.thisip = None

    def start_requests(self):
        yield scrapy.Request(self.fake_start_url, callback=self.parse)


    def parse(self, response):
        # print(response.body.decode("utf-8"))
        # print(response.text)
        # print(response.status)

        is_last_page = False
        while not is_last_page:
            # lists = response.xpath('//div[@class="job-title"]/span/a/@href').extract()
            # # print(list)
            # list_page_selector = self.get_page_selector(list_url)
            # if lists == []:
            #     pass
            # else:
                for index in range(len(self.start_urls)):
                    list_url = self.start_urls[index]
                    tag = self.start_url_tag[index]
                    # detail_selector = self.get_page_selector(list)
                    # item = self.detail_parse(detail_selector)
                    list_page_selector = self.get_page_selector(list_url)
                    is_last_page = True
                    # print(list_page_selector)
                    # yield item
                    # print(list_page_selector.response.text)
                    # lists_url = list_page_selector.xpath('//div[@class="primary-box"]/@href').extract()
                    for list_url in list_page_selector.xpath('//div[@class="primary-box"]/@href').extract():
                        list_url = "https://www.zhipin.com" + list_url
                        print(list_url)
                        self.headers["cookie"] = "_uab_collina=159071905074371533234384; __zp__pub__=; lastCity=100010000; __c=1592189159; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1592113817,1592114026,1592114034,1592189159; __l=l=%2Fwww.zhipin.com%2Fjob_detail%2F%3Fquery%3D%25E8%25AF%25AD%25E9%259F%25B3%25E8%25AF%2586%25E5%2588%25AB%26city%3D100010000%26industry%3D%26position%3D&r=&friend_source=0&friend_source=0; __a=15264055.1590719051.1592113817.1592189159.201.6.23.92; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a={}; __zp_stoken__=8302aI2NkGiUDUnoHH3BdanV7YmsBdxp%2FZFwzb0B6YVxVan9GOj5mWW9oZGBWC1IePC49OwYGdzoYfjtAATNVQB4jK3BGeUdWex8RPjIONmgISVd2HUNvHhoafWMsOwkMfhd4RHsAdk1aTT4%3D".format(int(time.time()))
                        yield scrapy.Request(list_url, callback=self.parse_response, headers=self.headers)
            # next_url = list_page_selector("//").extract_first()
            # if next_url is None:
            #     is_last_page = True
            # else:
            #     list_url = next_url

    def get_page_selector(self, url):
        is_error = True
        while is_error:
            try:
                # time.sleep(10)
                ua = UserAgent()
                self.headers["User-Agent"] = ua.random
                requests.packages.urllib3.disable_warnings()
                # requests.adapters.DEFAULT_RETRIES = 5
                # s = requests.session()
                # # cookie = s.cookies
                # s.keep_alive = False
                # a = requests.Session()
                page = requests.get(url,  headers=self.headers, verify=False, timeout=5,)
                # print(headers["cookie"])
                # headers["cookie"] = requests.utils.dict_from_cookiejar(page.cookies) proxies=self.get_proxy()
                # print(len(page.headers))

                if len(page.headers) == 9:
                    page = page
                else:
                    self.headers["cookie"] = self.cookies(url)[0]
                    # print(headers["cookie"])
                    page = requests.get(url, headers=self.headers, verify=False, timeout=5, )
                # time.sleep(10)
                # print(url, 1)
                # print(page.text, 2)
                if page.status_code == 200:
                    is_error = False
                    # print("status_code == 200")
            except Exception as e:
                is_error = True
                # self.get_proxy(True)
        response = scrapy.utils.response
        response.text = page.text
        response.url = url
        response.status = 200
        response_selector = Selector(response)
        return response_selector


    def get_proxy(self, force_change=False):
        if self.thisip is None or force_change:
            self.thisip = requests.get("http://dynamic.goubanjia.com/dynamic/get/6b1634d90b1994d851fe9493c4b49ac1.html?sep=3").content.decode("utf-8").strip()
            # print(self.thisip)
        proxy = {"https": "https://" + self.thisip,
                 "http": "http://" + self.thisip
        }
        print(proxy)
        return proxy

    def detail_parse(self, detail_selector):
        # 详情页面数据提取
        # 返回一个Item对象
        item = "items 对象"
        return item


    def cookies(self, url):
        b = True
        while b:
            driver = webdriver.Chrome("F:\wode\kgc\python数据爬取\chromedriver.exe")
            driver.get(url)
            a = driver.get_cookies()
            time.sleep(10)
            driver.close()
            driver.quit()
            a = re.findall("8302+[a-z A-Z 0-9]*[%]*3D", str(a))
            if a != []:
                cookie = "_uab_collina=159071905074371533234384; __zp__pub__=; sid=sem; toUrl=/; JSESSIONID=""; __c=1592113817; __g=sem; __l=l=%2Fwww.zhipin.com%2Fuser%2Fsem7.html%3Fsid%3Dsem%26qudao%3Dbdpc_baidu-%25E5%258D%258E%25E5%2593%2581%25E5%258D%259A%25E7%259D%25BF02A18KA0679%26plan%3D%25E8%25A1%258C%25E4%25B8%259A%25E5%25AE%259A%25E6%258A%2595-%25E5%2593%2581%25E7%2589%258C%26unit%3Dboss%25E7%259B%25B4%25E8%2581%2598%26keyword%3Dwww.zhipin.com%2Fc101210100%26bd_vid%3D10642220335188829613&r=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.Kf0000K5cNxA6dzipXA58wnSPeKs0YyiITM-cTvyyoJgtWN5ShqoxbLcQD6bfK1m1CHbEPNXUDxJC0NCyk6aSS3rMd9X7gaS82n8h38os1kDfh1S71VaguC8uq7OVJ54Ayq9S7ZUQB8yNsQ82UFzKzmfzm48sK_DXmyP9YmhQBMrDFv8SxcHGMHg_tAiFVGVT2xZlNP--TjSn_pyQG6i9po38Z3v.7D_NR2Ar5Od663rj6t8AGSPticnDpuCcYlxZMLWknwGYqxu68uTkxIW94UvTyj59tqvZut_r11sSXejE33I-XZ1LmIMzseOU9tOZjESyZdSVhHvde5OKeUrMkLqTI7hFWj4en5Vose59sSxu9qIhZxeT5M8sSL1seOU9tSMj_q8Zx813x5I9LtTrzEj4SrZuEse59l3cMYAQLwk3x5kseOgjlqhZ1vmI-XZx_lqJIZ0lp4W63rjz3pM3Lkc69o_ozNvNvy2pMpRt85R_nYQAHG_3tN0.U1Yz0ZDqmhq1TsKspynqn0KY5gILIzRzwgGCpgKGUBRzwyPEUiRzwhnknjDznH0knj00pyYqnWcd0ATqTZn10ZNG5yF9pywd0ZKGujYkrfKWpyfqPHT0UgfqnH0krNtknjDLg1DsPjwxn1msnfKopHYs0ZFY5Hf4nfK-pyfqn1D4nj-xnHfdPNt1nHmLn-tznHDkPNt1nH0vrNt1nW0YPNt1nj6zndtzPWndn0KBpHYkPH9xnW0Yg1ckPsKVm1Yknj0kg1D3PHfzPjRLnjKxnH0kg100TgKGujYs0Z7Wpyfqn0KzuLw9u1Ys0A7B5HKxn0K-ThTqn0KsTjYknHndPWTYP1nd0A4vTjYsQW0snj0snj0s0AdYTjYs0AwbUL0qn0KzpWYs0Aw-IWdsmsKhIjYs0ZKC5H00ULnqn0KBI1Ykn0K8IjYs0ZPl5fK9TdqGuAnqTZnVuyPJ0A-bm1dribGH0ZwdT1YkP1bdnWfLnH0YPjTvPjRYPHfzP6Kzug7Y5HDdrHcknHn3nH0kPW60Tv-b5yuhuADkuhR1nj0srym4mHc0mLPV5RfdnWR3n1KjnH6vn1NDfYc0mynqnfKYIgfqnfKsUWYs0Z7VIjYs0Z7VT1Ys0Aw-I7qWTADqn0KlIjYs0AdWgvuzUvYqn7tsg1DsPjuxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1KxPjDLn1bsnNts0ZK9I7qhUA7M5H00uAPGujYs0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqn0KhmLNY5H00pgPWUjYs0ZGsUZN15H00mywhUA7M5H60UAuW5H00uAPWujY0mhwGujdKwWc4wjR3rRfYfWuKnW0sfbmdPHTLwHDkPWf1rHmvf6KEm1Yk0AFY5H00Uv7YI1Ys0AqY5HD0ULFsIjYzc10WnH0WnBnzPjcvrHcsnin1nW0sc1nznj08nj0snj0sc1DWnBnsczYWna3snj0snj0Wni3snj0snj00TNqv5H08rj-xna3sn7tsQW0sg108PHIxna3zP7tsQWnz0AF1gLKzUvwGujYs0APzm1YYnjn3n0%26ck%3D4959.14.87.282.302.446.261.285%26shh%3Dwww.baidu.com%26sht%3Dbaiduhome_pg%26us%3D2.0.1.0.1.300.0%26wd%3Dboss%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26inputT%3D3066%26bc%3D110101&g=%2Fwww.zhipin.com%2Fuser%2Fsem7.html%3Fsid%3Dsem%26qudao%3Dbdpc_baidu-%25E5%258D%258E%25E5%2593%2581%25E5%258D%259A%25E7%259D%25BF02A18KA0679%26plan%3D%25E8%25A1%258C%25E4%25B8%259A%25E5%25AE%259A%25E6%258A%2595-%25E5%2593%2581%25E7%2589%258C%26unit%3Dboss%25E7%259B%25B4%25E8%2581%2598%26keyword%3Dwww.zhipin.com%2Fc101210100%26bd_vid%3D11323583472472588092&friend_source=0&friend_source=0; __zp__pub__=; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1591954250,1592113817,1592114026,1592114034; lastCity=100010000; __a=15264055.1590719051.1591954244.1592113817.131.5.22.22; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a={}; __zp_stoken__={}".format(int(time.time()-60), a[0]),
                return cookie
            else:
                continue

    def parse_response(self, response):
        """
        招聘名称、职位信息、薪资、经验要求、学历要求、公司名称、公司行业、公司人数、公司概况、公司融资阶段
        :param response:
        :return:
        """
        job_name = response.xpath('//div[@class="name"]/h1/text()').extract()
        xinzi = response.xpath('//div[@class="text"]/text()').extract()
        xixin = response.xpath('/h1/span[@class="salary"]/span/text()').extract()
        jinyan = response.xpath('//p/text()').extract()
        xueli = response.xpath('//p/text()').extract()
        gsname = response.xpath('//div[@class="info-primary"]/p/text()').extract()
        gshy = response.xpath('//div[@class="info-primary"]/p[@class="gray"]/text()').extract()
        gsrs = response.xpath('//div[@class="info-primary"]/p[@class="gray"]/text()').extract()
        gsgk = response.xpath('//p[@class="detail-text show-switch four-lines"]/text()').extract()
        gsxz = response.xpath('//div[@class="info-primary"]/p[@class="gray"]/text()').extract()
        print(job_name, xinzi, xixin, jinyan, xueli, gsname, gshy, gsrs, gsgk, gsxz)

# _uab_collina=159071905074371533234384; __zp__pub__=; lastCity=100010000; __c=1592189159; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1592113817,1592114026,1592114034,1592189159; __l=l=%2Fwww.zhipin.com%2Fjob_detail%2F%3Fquery%3D%25E8%25AF%25AD%25E9%259F%25B3%25E8%25AF%2586%25E5%2588%25AB%26city%3D100010000%26industry%3D%26position%3D&r=&friend_source=0&friend_source=0; __a=15264055.1590719051.1592113817.1592189159.199.6.21.90; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1592192928; __zp_stoken__=8302aI2NkGiUDHSYQDwEhanV7YmsBBFhjSB8zb0B6YUYPK19pOj5mWW9oWhNqTC4aPC49OwYgAkgTcWxAEkNNZy9XD3ZSGCgpGwYHJjIONmgISVMKWn8cIBoafWMsOwkMfhd4RHsAdk1aTT4%3D

