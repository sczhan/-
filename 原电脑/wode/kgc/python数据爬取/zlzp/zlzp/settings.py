# -*- coding: utf-8 -*-
import random
# Scrapy settings for zlzp project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zlzp'

SPIDER_MODULES = ['zlzp.spiders']
NEWSPIDER_MODULE = 'zlzp.spiders'


USER_AGENT = [
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
    ]
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zlzp (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 20
DOWNLOAD_TIMEOUT = 10
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# 'Accept-Language': 'en',
"cookie": "https://fe-api.zhaopin.com/c/i/sou?_v=0.14688645&x-zp-page-request-id=6daf289383384f298f93b3e35b3e2c72-1591632517394-913042&x-zp-client-id=39b6cdc3-05be-4419-8ce6-76a61643b5c3&MmEwMD=5lRiV0BGCgbtV73XDlcfIck876cYqZRntMr.p_Ny6hueGUEE8j_TzvxhUkwTvVS_mWmFGMbrvR_.MdO4HOej38xMzy8V18MRF9n7kNoPGiVfMDwRMu444BpA05kvf4XhS9VWo2m1OC8NJVpboZ2myHta.yrtYVfAthKKkPB0RFKjd7k35ywC.m168a95OQ3KtBb7bMUtA7o_GOjfrA2Qu0XxTY4r_mdnmJdxoaG3cDhnqPvn04V2OLv7ev408_aXIlpijdRLSlYD7htCs5nSEbVBTfnWZf1fuSimimByOFK9ndNGnNGGzJvkdKgwEWfYjUWDiZW6kzRzNTnNZKZNyQ.Ykoodf5FgYkTbal.GllDmAoEONpZuCagJKjtk17fOE6cWEZvlQ3Y2Ufv7Gf1xuW9sf",
    "user-agent": random.choice(USER_AGENT),
'date': 'Mon, 08 Jun 2020 16:08:38 GMT',

# ":authority": "sou.zhaopin.com",
# ":path": "/?jl=530&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&kt=3",
# ":scheme": "https",
# "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
# "accept-language": "zh-CN,zh;q=0.9",
# "cache-control": "max-age=0",
# "referer": "https://www.zhaopin.com/",
# "sec-fetch-dest": "document",
# "sec-fetch-mode": "navigate",
# "sec-fetch-site": "same-origin",
"sec-fetch-user": "?1",
"upgrade-insecure-requests": "1",
"origin": "https://sou.zhaopin.com",
"referer": "https://sou.zhaopin.com/?jl=530&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&kt=3",
"sec-fetch-dest": "empty",
"sec-fetch-mode":"cors",
"sec-fetch-site": "same-site",
":authority": "fe-api.zhaopin.com",
'x-zp-page-request-id': '6daf289383384f298f93b3e35b3e2c72-1591632517394-913042',
'x-zp-request-id': '887e79df79f44a41ba0e98ae33f169bd',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zlzp.middlewares.ZlzpSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zlzp.middlewares.ZlzpDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'zlzp.pipelines.ZlzpPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'