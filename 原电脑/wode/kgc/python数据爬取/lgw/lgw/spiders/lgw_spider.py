# -*- coding: utf-8 -*-
import scrapy
import requests
from urllib.parse import urlencode
import json, time
from scrapy.selector import Selector


class LgwSpiderSpider(scrapy.Spider):
    name = 'lgw_spider'
    # allowed_domains = ['example.com']1307e660255740ada6dae383362da5fa
    # start_urls = ['http://example.com/']
    pre_datail_url = "https://www.lagou.com/jobs/{}.html"
    fake_start_url = "http://example.com/"
    json_request_url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
    start_url_tags = ["机器学习"]

    def start_requests(self):
        yield scrapy.Request(self.fake_start_url, callback=self.parse)

    def parse(self, response):
        url_start = "https://www.lagou.com/jobs/list_%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0?labelWords=&fromSearch=true&suginput="

        for keyword in range(0, len(self.start_url_tags)):
            for page_num in range(1, 2):
                parm = {"first": "false", "kd": self.start_url_tags[keyword], "pn": str(page_num)}
                data = urlencode(parm)
                headers = {
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    'Referer': 'https://www.lagou.com/jobs/list_%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0?labelWords=&fromSearch=true&suginput=',
                    # "origin": "https://www.lagou.com",
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                    # "x-requested-with": "XMLHttpRequest",
                }
                s = requests.Session()
                s.get(url_start, headers=headers, timeout=3)  # 请求首页获取cookies
                cookie = s.cookies  # 为此次获取的cookies
                headers["content-length"] = str(len(data))
                headers["origin"] = "https://www.lagou.com"
                headers["x-requested-with"] = "XMLHttpRequest"
                headers["cookie"] = "user_trace_token=20200408170451-29a87a1a-2ca8-4d57-9eb9-4d1f0347208d; LGUID=20200408170451-b5c104a1-2e8d-4658-857a-d57c3b9ce74a; _ga=GA1.2.404826130.1586336693; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22171592c18c531d-072a631f34a5b3-6701b35-1327104-171592c18c6346%22%2C%22%24device_id%22%3A%22171592c18c531d-072a631f34a5b3-6701b35-1327104-171592c18c6346%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; RECOMMEND_TIP=true; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAABEIABCI3DA8B41D6302A195C1441364308EF3AD; WEBTJ-ID=20200614210126-172b2eba339368-0d540fb10511b9-d373666-1327104-172b2eba33a384; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1591928278,1591928499,1591928502,1592139687; LGSID=20200614210124-f5691899-d33c-477b-8133-1f493b7c24bd; _gid=GA1.2.728047838.1592139687; TG-TRACK-CODE=search_code; X_HTTP_TOKEN=01dd9aa456f606ad5416412951e021a7f77e9b9a86; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1592146148; LGRID=20200614224909-7842f827-eb29-44d0-9e82-9027bbaf47a4; SEARCH_ID=7ebe49e0d878471aa25eb57ce8058fbf"
                # headers["cookie"] = "XMLHttpRequest"
                response = s.post(self.json_request_url, data=data, headers=headers, timeout=3, verify=False,)
                # response = s.post(self.json_request_url, data=data, headers=headers, cookies=cookie)  # 获取此次文本
                # print(response)
                time.sleep(5)
                # response = requests.post(self.json_request_url, data=data, headers=headers)
                # response = scrapy.utils.response
                # response.text = page.text
                # response.url = url_start
                # response.status = 200
                # response_selector = Selector(response)
                print(response.text)
                self.parse_json(response.text)
                # for result in self.parse_json(response.text):
                #
                #     yield result



    def parse_json(self, response_json_str):
        print(1)
        json_object = json.loads(response_json_str)
        jobs_list = json_object["content"]["positionResult"]["result"]
        print(jobs_list)
        for job in jobs_list:
            positionId = job["publisherId"]
            try:
                print(positionId["positionName"])
            except Exception as e:
                print(e)
            detail_url = self.pre_datail_url.format(positionId)
            # self.parse_detail(detail_url)
            print(detail_url)
            # yield self.parse_detail(detail_url)
        # print(json_object)

    def parse_detail(self, detail_url):
        #需要使用代理ip
        # 使用 return 返回 item
        pass

# user_trace_token=20200408170451-29a87a1a-2ca8-4d57-9eb9-4d1f0347208d; LGUID=20200408170451-b5c104a1-2e8d-4658-857a-d57c3b9ce74a; _ga=GA1.2.404826130.1586336693; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22171592c18c531d-072a631f34a5b3-6701b35-1327104-171592c18c6346%22%2C%22%24device_id%22%3A%22171592c18c531d-072a631f34a5b3-6701b35-1327104-171592c18c6346%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; RECOMMEND_TIP=true; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAABEIABCI3DA8B41D6302A195C1441364308EF3AD; WEBTJ-ID=20200614210126-172b2eba339368-0d540fb10511b9-d373666-1327104-172b2eba33a384; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1591928278,1591928499,1591928502,1592139687; LGSID=20200614210124-f5691899-d33c-477b-8133-1f493b7c24bd; _gid=GA1.2.728047838.1592139687; TG-TRACK-CODE=index_hotjob; _gat=1; X_HTTP_TOKEN=01dd9aa456f606ad6824412951e021a7f77e9b9a86; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1592144289; LGRID=20200614221806-7b1c94ec-beab-4fa0-94f1-091847ae13cf; SEARCH_ID=9cef4f5c71c34906b0646675a547f3b1
# user_trace_token=20200408170451-29a87a1a-2ca8-4d57-9eb9-4d1f0347208d; LGUID=20200408170451-b5c104a1-2e8d-4658-857a-d57c3b9ce74a; _ga=GA1.2.404826130.1586336693; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22171592c18c531d-072a631f34a5b3-6701b35-1327104-171592c18c6346%22%2C%22%24device_id%22%3A%22171592c18c531d-072a631f34a5b3-6701b35-1327104-171592c18c6346%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; RECOMMEND_TIP=true; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAABEIABCI3DA8B41D6302A195C1441364308EF3AD; WEBTJ-ID=20200614210126-172b2eba339368-0d540fb10511b9-d373666-1327104-172b2eba33a384; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1591928278,1591928499,1591928502,1592139687; LGSID=20200614210124-f5691899-d33c-477b-8133-1f493b7c24bd; _gid=GA1.2.728047838.1592139687; TG-TRACK-CODE=index_hotjob; _gat=1; X_HTTP_TOKEN=01dd9aa456f606ad6824412951e021a7f77e9b9a86; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1592144289; LGRID=20200614221806-7b1c94ec-beab-4fa0-94f1-091847ae13cf  SEARCH_ID=e8e8f047c1d1456eacb348fc57a19c61;
# user_trace_token=20200408170451-29a87a1a-2ca8-4d57-9eb9-4d1f0347208d; LGUID=20200408170451-b5c104a1-2e8d-4658-857a-d57c3b9ce74a; _ga=GA1.2.404826130.1586336693; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22171592c18c531d-072a631f34a5b3-6701b35-1327104-171592c18c6346%22%2C%22%24device_id%22%3A%22171592c18c531d-072a631f34a5b3-6701b35-1327104-171592c18c6346%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; RECOMMEND_TIP=true; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAABEIABCI3DA8B41D6302A195C1441364308EF3AD; WEBTJ-ID=20200614210126-172b2eba339368-0d540fb10511b9-d373666-1327104-172b2eba33a384; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1591928278,1591928499,1591928502,1592139687; LGSID=20200614210124-f5691899-d33c-477b-8133-1f493b7c24bd; _gid=GA1.2.728047838.1592139687; TG-TRACK-CODE=index_hotjob; _gat=1; X_HTTP_TOKEN=01dd9aa456f606ad6824412951e021a7f77e9b9a86; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1592144289; LGRID=20200614221806-7b1c94ec-beab-4fa0-94f1-091847ae13cf; SEARCH_ID=9cef4f5c71c34906b0646675a547f3b1
# user_trace_token=20200408170451-29a87a1a-2ca8-4d57-9eb9-4d1f0347208d; LGUID=20200408170451-b5c104a1-2e8d-4658-857a-d57c3b9ce74a; _ga=GA1.2.404826130.1586336693; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22171592c18c531d-072a631f34a5b3-6701b35-1327104-171592c18c6346%22%2C%22%24device_id%22%3A%22171592c18c531d-072a631f34a5b3-6701b35-1327104-171592c18c6346%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; RECOMMEND_TIP=true; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAABEIABCI3DA8B41D6302A195C1441364308EF3AD; WEBTJ-ID=20200614210126-172b2eba339368-0d540fb10511b9-d373666-1327104-172b2eba33a384; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1591928278,1591928499,1591928502,1592139687; LGSID=20200614210124-f5691899-d33c-477b-8133-1f493b7c24bd; _gid=GA1.2.728047838.1592139687; TG-TRACK-CODE=index_hotjob; _gat=1; SEARCH_ID=e8e8f047c1d1456eacb348fc57a19c61; X_HTTP_TOKEN=01dd9aa456f606ad6824412951e021a7f77e9b9a86; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1592144289; LGRID=20200614221806-7b1c94ec-beab-4fa0-94f1-091847ae13cf
# Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6 = 时间