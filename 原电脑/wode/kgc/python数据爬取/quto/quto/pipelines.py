# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import time

class QutoPipeline(object):
    def __init__(self):
        self.start_time = 0
        self.end_time = 0

    def open_spider(self, spider):
        self.start_time = time.time()
        print(time.ctime())


    def process_item(self, item, spider):
        return item

    def close_spider(self, spider):
        self.end_time = time.time()
        print(time.ctime())
        print(self.end_time - self.start_time)
