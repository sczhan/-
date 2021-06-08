# -*- coding: utf-8 -*-
import scrapy, json


class XueqiuspiderSpider(scrapy.Spider):
    name = 'xueqiuspider'
    # allowed_domains = ['example.com']
    start_urls = ['https://api.xueqiu.com/v4/statuses/home_timeline.json?_t=1XIAOMIa454fd1e443ecf2baae0e1b09e43323e.1474862103.1591271577451.1591271660227&_s=947142&count=10&source=all&x=0.154&filter_retweet_text=1&max_id=150803181 ']
    headers = {
        "Cookie": "xq_a_token=ff971eb2e7f816f8b525ac715f5a63e23d946600;xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjE0NzQ4NjIxMDMsImlzcyI6InVjIiwiZXhwIjoxNTkzODYxMzEzLCJjdG0iOjE1OTEyNjk1NTExOTQsImNpZCI6Ikp0WGJhTW43ZVAifQ.Xobi7SA2eCor0XVAlTZvMHjXY1Dunbne4nqlL5XZLVBzGLGtjO7q_MMmofUqIq7lf4xm5UT-lIYDGB-A5P2motEOEMuOe3KqvxZteZ8tafu9yhIyLZF6sIvhLzOWb4-uk4-TjlKDKDPhk2hRGa3sxbBfZc0iC-fRPLOqiGJzvUToE0hyCkhNMwlgtzLuRMVc7HBoabL2_uIwGnbZSF-2df-UI3vcygS_BHVYuk_rkX8suNE9UPKT1sLHNx7T3xbz2B4ZzV1MkP6OfffZuFg_yuxE5XYIe4jp1e0_JzQfKmFYL_uiNwvDXgYcLU7tBEpXs_voSM741wI4HE9dGYrAYQ;u=1474862103;session_id=;xid=0",
        "X-Device-Model-Name": "Xiaomi_MI_9",
        "X-Device-OS": "Android 5.1.1",
        "User-Agent": "Xueqiu Android 12.11.1",
        "Accept-Encoding": "gzip",
        "Accept-Language": "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
        "Host": "api.xueqiu.com",
        "Connection": "Keep-Alive"
    }
    pre_url = "https://api.xueqiu.com/v4/statuses/home_timeline.json?_t=1XIAOMIa454fd1e443ecf2baae0e1b09e43323e.1474862103.1591271577451.1591271660227&_s=947142&count=10&source=all&x=0.154&filter_retweet_text=1&max_id="
    limit = 0
    def start_requests(self):

        for i in self.start_urls:
            yield scrapy.Request(i, headers=self.headers, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.body.decode())
        next_max_id = data['next_max_id']
        print(data, next_max_id)
        self.limit += 1
        for i in data['home_timeline']:
            # sub_item = json.loads(i['description'])
            # title = sub_item['description']
            title = i['description']
            print(title)
        if self.limit < 3:
            yield scrapy.Request(self.pre_url + str(next_max_id), headers=self.headers, callback=self.parse)
