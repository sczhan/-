# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank_detail = scrapy.Field()
    title_detail = scrapy.Field()
    score = scrapy.Field()
    abstract_detail = scrapy.Field()
    describe = scrapy.Field()