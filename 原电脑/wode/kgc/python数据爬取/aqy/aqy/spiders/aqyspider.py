# -*- coding: utf-8 -*-
import scrapy, json
import time
"""
fiddler抓包的原理就是通过代理
"""

class AqyspiderSpider(scrapy.Spider):
    name = 'aqyspider'
    # allowed_domains = ['example.com']
    start_urls = ["https://cards.iqiyi.com/views_search/3.0/search?card_v=3.0&scrn_res=1080,1920&data_type=2&label_request_type=6&intent_result_num=0&need_onebox=1&play_mode=2&keyword=%E6%B5%B7%E8%B4%BC%E7%8E%8B&source=history&qr=0&need_qc=0&label_request_type=6&mode=1&s_sr=1&from_rpage=qy_home.0&from_block=search_bar_home&origin=0&s_token=&app_k=456ddd1ff52a6089c7e3f806d609520d&app_v=11.5.5&app_gv=&app_t=0&platform_id=10&dev_os=5.1.1&dev_ua=MI+9&net_sts=1&qyid=5680056330f607fb714c61c806c1f7831106&imei=f4921deb98f3951684a682df8d3ff265&aid=c70b5130ffb1b9ef&mac=84:EF:18:7A:96:F8&scrn_scale=2&lang=zh_CN&app_lm=cn&oaid=&psp_uid=&psp_sub_uid=&psp_cki=&psp_status=1&secure_v=1&secure_p=GPhone&cupid_id=863254664129623&cupid_v=3.46.009&core=1&api_v=11.2&profile=%7B%22group%22%3A%221%2C2%22%2C%22counter%22%3A1%2C%22hy_id%22%3A%22%22%2C%22recall_firstdate%22%3A%22-1%22%2C%22first_time%22%3A%2220200604%22%7D&unlog_sub=0&province_id=19007&service_filter=&youth_model=0&no_rec=0&xas=1&bi_params=%7B%22old_user_refresh_opt%22%3A%2210%22%2C%22viptab%22%3A%22cid_order_list_1%22%2C%22vipService%22%3A%22new%22%2C%22bi_recommend_reason%22%3A%22recreason%22%2C%22people_id%22%3A%220%22%2C%22vertical_order%22%3A%22colomn%22%2C%22paperplane%22%3A%22yes%22%2C%22ad_focus_time%22%3A%225%22%2C%22recommend%22%3A%221%22%2C%22ct%22%3A%2220200605%22%2C%22qyhome%22%3A%22newui%22%2C%22tag_data_source%22%3A%22bi%22%2C%22wdym_hd%22%3A%220%22%2C%22smallvideo%22%3A%221%22%2C%22wallet_ui%22%3A%22ui_new%22%2C%22order%22%3A%22huati%2Cbaoxiang%2Cdati%2Cwenda%22%2C%22baike_p2v%22%3A%22bucket_a%22%2C%22ad_third%22%3A%22yes%22%2C%22cnxh_card_new%22%3A%221%22%2C%22is_poster%22%3A%22operation%22%2C%22design%22%3A%221%22%7D&layout_v=67.90&device_type=0&cupid_uid=863254664129623&gps=%2C&bdgps=&net_level=3&req_times=0&req_sn=1591291988694"]
    listm = 0
    ps = '&app_k=456ddd1ff52a6089c7e3f806d609520d&app_v=11.5.5&app_gv=&app_t=0&platform_id=10&dev_os=5.1.1&dev_ua=MI+9&net_sts=1&qyid=5680056330f607fb714c61c806c1f7831106&imei=f4921deb98f3951684a682df8d3ff265&aid=c70b5130ffb1b9ef&mac=84:EF:18:7A:96:F8&scrn_scale=2&lang=zh_CN&app_lm=cn&oaid=&psp_uid=&psp_sub_uid=&psp_cki=&psp_status=1&secure_v=1&secure_p=GPhone&cupid_id=863254664129623&cupid_v=3.46.009&core=1&api_v=11.2&profile=%7B%22group%22%3A%221%2C2%22%2C%22counter%22%3A1%2C%22hy_id%22%3A%22%22%2C%22recall_firstdate%22%3A%22-1%22%2C%22first_time%22%3A%2220200604%22%7D&unlog_sub=0&province_id=19007&service_filter=&youth_model=0&no_rec=0&xas=1&bi_params=%7B%22old_user_refresh_opt%22%3A%2210%22%2C%22viptab%22%3A%22cid_order_list_1%22%2C%22vipService%22%3A%22new%22%2C%22bi_recommend_reason%22%3A%22recreason%22%2C%22people_id%22%3A%220%22%2C%22vertical_order%22%3A%22colomn%22%2C%22paperplane%22%3A%22yes%22%2C%22ad_focus_time%22%3A%225%22%2C%22recommend%22%3A%221%22%2C%22ct%22%3A%2220200605%22%2C%22qyhome%22%3A%22newui%22%2C%22tag_data_source%22%3A%22bi%22%2C%22wdym_hd%22%3A%220%22%2C%22smallvideo%22%3A%221%22%2C%22wallet_ui%22%3A%22ui_new%22%2C%22order%22%3A%22huati%2Cbaoxiang%2Cdati%2Cwenda%22%2C%22baike_p2v%22%3A%22bucket_a%22%2C%22ad_third%22%3A%22yes%22%2C%22cnxh_card_new%22%3A%221%22%2C%22is_poster%22%3A%22operation%22%2C%22design%22%3A%221%22%7D&layout_v=67.90&device_type=0&cupid_uid=863254664129623&gps=%2C&bdgps=&net_level=3&req_times=0&req_sn='
    # pr = "https://cards.iqiyi.com/views_search/3.0/search?prev_card_index=31&keyword=%E6%B5%B7%E8%B4%BC%E7%8E%8B&origin=0&from_docid=&s_sr=1&page_st=&user_first_time=20200604&pg_num="
    headers = {
        't': '484640881',
        'sign': 'b72c22de11ff62df03156c74b24f4ad3',
        # 'X-B3-TraceId': '331ee510dbad74d001728064cad6004b',
        'X-B3-Sampled': '0',
        # 'qyid':'863254664129623_c70b5130ffb1b9ef_0',
        'User-Agent': 'iqiyi/com.qiyi.video/11.5.5/NetLib-okhttp/3.12.10.2',
        'Connection': 'Keep-Alive',
        # 'X-B3-SpanId': '01728064cad6004b',
        'Host': 'cards.iqiyi.com',
        'Accept-Encoding': 'gzip'
    }

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], headers=self.headers, callback=self.parse)

    def parse(self, response):
        self.listm += 1
        jrs = json.loads(response.body)
        # print(response.body)
        next_url = str(jrs["base"]["next_url"]).replace("海贼王", "%E6%B5%B7%E8%B4%BC%E7%8E%8B")
        bases = jrs["cards"]
        # print(next_url)
        for base in bases:
            try:
                base = base["blocks"][1]["metas"][0]["text"]
                print(base)
            except KeyError as e:
                pass

        ti = int(time.time() * 100)
        if self.listm < 5:
            url = next_url + self.ps + str(ti)
            print(url)
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)


