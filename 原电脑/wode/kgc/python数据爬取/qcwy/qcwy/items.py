# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QcwyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = scrapy.Field()
    xinxi = scrapy.Field()
    xinzi = scrapy.Field()
    fuli = scrapy.Field()
    jinyan = scrapy.Field()
    xueli = scrapy.Field()
    gsname = scrapy.Field()
    hangye = scrapy.Field()
    xingzhi = scrapy.Field()
    renshu = scrapy.Field()
    gaikuang = scrapy.Field()
