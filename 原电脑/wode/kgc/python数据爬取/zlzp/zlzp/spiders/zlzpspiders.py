# -*- coding: utf-8 -*-
import scrapy, random, json


class ZlzpspidersSpider(scrapy.Spider):
    name = 'zlzpspiders'
    allowed_domains = ['zhaopin.com']
    start_urls = [
                  # "https://sou.zhaopin.com/?jl=530&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&kt=3",
                  "https://fe-api.zhaopin.com/c/i/sou?_v=0.89584345&x-zp-page-request-id=4ccebed3fcac452383150b84f1ef1d68-1591600393406-257269&x-zp-client-id=39b6cdc3-05be-4419-8ce6-76a61643b5c3&MmEwMD=5wdUnzxyAfqsnT56Gw9gyM2otX9Wb2d.7cvn6OHGp1Y9DiXpguQ7h5B1SF47rJUOOYOkDcq3rqQnebmPN_Mu5oBchR3fY02An_kXOlsQ9RrVSxLiBf5NCjKoYxgiCEcX0bbBVFdCTRxrZLxnLmA8OdnYRrUvuOVstvDFDdlL9bDapfbWeb51yT.EfG88a9NCJful2yQQMpjcz0X7RPs4e9N7toxmnhESCWD8jcImXqBs_cEu8gTprAZ5ycEP13WEJnPmKRv1iZgcrRFaKlpQUj5OAqX.Kk23ORPW9tzxHMERJBcwd5ZyTxN_w1VddS9W9oR9CA7G2ZAklUcZlblwmduxBC1Rcyla4WZfLkDoyiyK0Hd29jk0ouoYpGdOjJx0UEuqxjqTcAG4Rskw6.C3X3dkR",
        # # "https://sou.zhaopin.com/?jl=530&kw=%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98&kt=3",
                  # "https://fe-api.zhaopin.com/c/i/sou?_v=0.47266301&x-zp-page-request-id=f73194d670714c888dd00c0d1f44d6ab-1591596395411-789458&x-zp-client-id=39b6cdc3-05be-4419-8ce6-76a61643b5c3&MmEwMD=5.n0jMlFEUJajkuVg.NMfzL913NB5snE00jpBYckx93o8gOnGmpHsEPSN7CHR4Fq4OXG80J4RCpp2AErSWKAbSPfsG5nE6jEgxFaPT2EmBIkZ88XSYtF9R7iSb.SLd3Bq3sN3L7DVdmV9EQNepZAOgmj2Qu9OZPV571lDMu.5V7U_z1FEg.nRytujQ_GtEKxG42e_g6DBzQSuhd2oE4NKR5NRRyGN3aiQY7mWKe4crg8YkBep6QePCW6Q6Vu5QbS5HkjHhY3zuZ5SCeLy5AudIUBVvV5pa7vm5yBz49L54BzYqVmVqR4fzC0z.0Boqx.mTvwT3Dv19FOCqyOFIRiNyMs0kl06IK302zASigFCtWi3d4Md1G7M4n_hbmEd3.g47zwY4E7DiGxE9uuBeXMrp7yh",
                  # # "https://sou.zhaopin.com/?jl=530&kw=%E7%AE%97%E6%B3%95&kt=3",
                  # "https://fe-api.zhaopin.com/c/i/sou?_v=0.82522386&x-zp-page-request-id=f6bb6d71c35248b89fc283b8ca4ccc3f-1591596468217-282158&x-zp-client-id=39b6cdc3-05be-4419-8ce6-76a61643b5c3&MmEwMD=51QBWPjrXXO.W_wH81oqoVDd0fo03jQs1Jltx773BwCQgrJNDZdVTSWjHY3Vdc0MwFq4gJOGdHdtkNbFUTghqEW_TQCgN7bn7VHA5p7RcIV4EUGk4EsWI9Aojj7n.Na_a5kdvrZGL3.eRYiid0HBoHaJWFWSIMuTgO60QbYv0_9tfAxMJdLsFKapo.NRBJ51iS1kbpkx1EEQJGUUQMw_JeewD4_yc1NgMtylO05ZEuT67zTowIgRPZHMcLVkucZnlaApKeMDBamon7p.D6XCzLqRMzZ4I43OPuENFPK9eGAhgZjQxXuHUaWNlCsJKxdZsBVcAF1zZc0sDhSvE1hgr2BL7b3w0knuzaaPq2LRcWAaGuaSK8p7UgxmNfA2MuKj0ZWVLA_e0wrMNJV3Ho41uIsccPTIcMRB9wlQIRc5t.MLsPquS1j_1EMkVSCSuo2PooM.",
                  # # "https://sou.zhaopin.com/?jl=530&kw=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0&kt=3",
                  # "https://fe-api.zhaopin.com/c/i/sou?_v=0.71783063&x-zp-page-request-id=2abda7ebde69447bb759ef229b1b2b0a-1591596508394-313368&x-zp-client-id=39b6cdc3-05be-4419-8ce6-76a61643b5c3&MmEwMD=52fAsYU5SR8VsJGar2_d3O4q.K_howf7J_yTKMpvajhOvCaKRhc.jDSYAP2.GTx9czelv_8IGgcTQ8M2Ecm0IdSmjwxpfQWt1gp6q3p475aExZXLRu0I_tZGVuzaaEb.O6J_3490MJEXV.b8uDWF.0W8dkc3hvYq0oY7.xFx9Zuu2qpjWJQCTIb20mCRC8B61z7YmY35e8p2lP5irUebjlTEHPLaCtWOo0L.Ud7fRWdU6I5U2EFxMuOldtgYS8JDKjC1.1solA1iyqFZJJgJHxLN7wg44Pf2bboyyuVOmUEIb4W9TJ9n9tXhrD9KxGRt8u2_4IctwOLJziVnydIo0K.xdxFyBrsQyV2oQC3bMZT3nWtC66NHULSaSB.EJGUL5EsLsnnJkMGPronJEf5KGV_Y4",
                  # # "https://sou.zhaopin.com/?jl=530&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3",
                  # "https://fe-api.zhaopin.com/c/i/sou?_v=0.46340121&x-zp-page-request-id=f2c9447d74f945acaddfedceec365ec5-1591596631192-832304&x-zp-client-id=39b6cdc3-05be-4419-8ce6-76a61643b5c3&MmEwMD=5HM5gdzAFu9_gvF8jHqpuxrXqZq276McbAkMeS.xMqSJWQtgnfgmr7h44EImhIutNoojWA9Sh1gM60fhOLdF0Yh.rnFGDZoSosX9IMrYVrgxQnYKi.nYZm52wvJUxLvatzfwG65SnMnbjQSp6hZ_E8FLyPZXivOOSyF0rFsnKm5X11.cC8G2Lq7VvwDJaKNoFEux.4HHR3lhaVnlR88ZzYfIScjMWlJSX_gLTC2qCU9lsn_svbQ7EVS0O.NlJRijFEyvWWHeJ_OziNz.s4hcnE0K8nY_w_BXiO05_tIRmbOw82UhvyOqwObELPb5DF_sSoXPWqnCUzrUP3gpguapHfbF9nii8nSLbHqx4CFk0RVaetqiK5soKo.ImP3WO72_OMgqXP95y7_KEJThRipdmnyBx8KpT0Qw.mWwPlWZHFUxos7ZHmA2KCq.N6CSruOYBRMO",
                  # # "https://sou.zhaopin.com/?jl=530&kw=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&kt=3"
                  # "https://fe-api.zhaopin.com/c/i/sou?_v=0.90130073&x-zp-page-request-id=42a2e8b34ec74dd8a519b25cd80cf5b2-1591596679479-984694&x-zp-client-id=39b6cdc3-05be-4419-8ce6-76a61643b5c3&MmEwMD=5S9pkr1dfJMYkR2SpSd5E65r4cdtUx9zwXZ0DHVbG5iP6PTUxIoj_10VqCGjafW21ygm6XM8a7o0Wt893KqTH.0l_7QDIr65ZnB0Yn7b6Kv.7UCVGI6TcIleSE76fQCr62maEw8sLAaSSA67i1gY8WhfADIlMuAsIkTwCJpHoyZnRnojsuNoL_7ye9iQnSJip2n5Hhm0q7svIRONex.ASUV.dpahYSwiUsoAA4pXIuPgc1vXXSQPXm4g1CiL5SieYJrhggqb.9s6W3x0T9HiqetV4u0MGKstsTZaFOZM8xXPlSEao13cvagI5ita6hKJ0RazSIfZWbNiC7I7TFndDTyGk1a6ULzJaMGtf5_rnqgKPgX_N1HL562wHYmFSbfJROuxMVYQUfUQXQg5ARd892Mfz"
    ]

    def start_requests(self):
        guanjianci = ['数据分析', '数据挖掘', '算法', '机器学习', '深度学习',  '人工智能']
        for url in self.start_urls:
            data = {
                "pageSize": "90",
                'cityId': "530",
                'workExperience': "-1",
                'companyType': "-1",
                'employmentType': "-1",
                'jobWelfareTag': "-1",
                'kt': "3",
                'kw': '数据分析',
            }
            yield scrapy.Request(url=url, callback=self.parse, body=json.dumps(data))

    def parse(self, response):
        """
        ①岗位搜索关键词：数据分析、数据挖掘、算法、机器学习机器学习、深度学习、人工智能
        ②爬取每个搜索关键词的列表首页的招聘信息，进入每个招聘信息的详情页，从详情页面提取以下信息并保存到Redis数据库中（招聘名称、职位信息、薪资、职位福利、经验要求、学历要求、公司名称、公司行业、公司性质、公司人数、公司概况）
        :param response:
        :return:
        """
        urls = response.xpath('//div[@id="listContent"]/div/div/a/@href')
        # response.body.decode(response.encoding)
        bs = str(response.body, encoding="utf8", errors="replace")
        print(bs)
        print(len(urls), urls)