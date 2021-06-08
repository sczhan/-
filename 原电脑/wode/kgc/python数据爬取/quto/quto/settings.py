# -*- coding: utf-8 -*-

# Scrapy settings for quto project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
BOT_NAME = 'quto'

SPIDER_MODULES = ['quto.spiders']
NEWSPIDER_MODULE = 'quto.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'quto (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'quto.middlewares.QutoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'quto.middlewares.QutoDownloaderMiddleware': 123,
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 543,
    "quto.middlewares.UserAgentMiddleware": 300,
}

IPPools = [
    {"ipaddr": "117.141.114.57:8080"},
    {"ipaddr": '223.241.4.14:4216'},
    {"ipaddr": '183.250.255.86:6300'},
    {"ipaddr": "114.98.27.122:4216"},
    {"ipaddr": "218.14.142.156:4216"},
    {"ipaddr": "59.41.131.171:4216}"},
]
# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'quto.pipelines.QutoPipeline': 300,
}

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
DEFAULT_COOKIE = {
    "_uab_collina": "159071905074371533234384;",
    "__zp__pub__":";",
    "__c=1591155281; __g":'-;',
    "lastCity":"100010000;",
    " __l:=l=%252Fjob_detail%252F%253Fquery%253D%2525E5%25259B%2525BE%2525E5%252583%25258F%2525E8%2525AF%252586%2525E5%252588%2525AB%2526city%253D100010000%2526industry%253D%2526position%253D&r=&friend_source=0&friend_source=0; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1590719051,1590974367,1591155303; __zp_stoken__=e01eaWC5ffgsVPhIdLXMjHnI0VzVyaSoeDToMAyk2OGF7XjgXVXpEXFkRJh1ELi4WLXshQH97JQYZYQdnS2coWyRXI2koDREbK25XfgEtWxEXHENxXTkTPx9QG0AAMQkMb0JkPyRbUGRROnQ%3D; __a=15264055.1590719051.1590974367.1591155281.81.3.14.81;":" Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1591157592",
},