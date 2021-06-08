# -*- coding: utf-8 -*-
import scrapy, json


class JrttspiderSpider(scrapy.Spider):
    name = 'jrttspider'
    # allowed_domains = ['example.com']
    start_urls = ['https://is.snssdk.com/api/news/feed/v47/?refer=1&refresh_reason=1&count=20&min_behot_time=1591276570&last_refresh_sub_entrance_interval=1591276647&loc_mode=5&tt_from=pull&lac=4527&cid=28883&cp=52eed189f7467q1&plugin_enable=4&client_extra_params=%7B%22ad_download%22%3A%7B%22space_unoccupied%22%3A62408088%2C%22space_cleanable%22%3A0%7D%2C%22last_ad_position%22%3A-1%7D&last_ad_show_interval=-1&cached_item_num=0&iid=1239895030633623&device_id=2436163651778093&ac=wifi&mac_address=84%3AEF%3A18%3A7A%3A96%3AF8&channel=lite2_tengxun&aid=35&app_name=news_article_lite&version_code=749&version_name=7.4.9&device_platform=android&ab_version=668903%2C668904%2C1757572%2C668907%2C668905%2C668906%2C668908%2C928942&ab_client=a1%2Cc2%2Ce1%2Cf2%2Cg2%2Cf7&ab_group=z2&ab_feature=z1&abflag=3&ssmix=a&device_type=MI+9&device_brand=Android&language=zh&os_api=22&os_version=5.1.1&uuid=863254664129623&openudid=c70b5130ffb1b9ef&manifest_version_code=7490&resolution=1080*1920&dpi=320&update_version_code=74906&_rticket=1591276647678&plugin_state=34893623325&sa_enable=0&tma_jssdk_version=1.65.0.6&rom_version=22&cdid=d7349617-c18c-48ca-ab41-2b4b52a30e2f']
    headers = {
        'Host': 'is.snssdk.com',
        'Connection': 'keep-alive',
        'Cookie': 'install_id=1239895030633623; ttreq=1$ea98afb01682d3386d73dc1b5ce16692959932c8; odin_tt=f8efd99ae00a36d905f28a19027b25b6e5ccec2e295e912f91ab5385a0cf29390ea33006ff6124b0ff5facd42fadeb181db6c5e1d8db7702295f26a1bcb3c16d',
        'X-SS-REQ-TICKET': '1591276647690',
        'passport-sdk-version': '12',
        'sdk-version': '2',
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; MI 9 Build/NMF26X) NewsArticle/7.4.9 cronet/TTNetVersion:4df3ca9d 2019-11-25',
        'x-tt-trace-id': '00-7f7ab6880d8a7ad8d14362d31acb0023-7f7ab6880d8a7ad8-01',
        'Accept-Encoding': 'gzip, deflate',
        'X-Gorgon': '040480284005c8a69ace2bd1659bb83aa9a7c08f51382f51eef9',
        'X-Khronos': '1591276647',
    }

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], headers=self.headers, callback=self.parse)

    def parse(self, response):
        jrs = json.loads(response.body)
        for jr in jrs["data"]:
            sub = json.loads(jr["content"])
            title = sub["abstract"]
            print(title)