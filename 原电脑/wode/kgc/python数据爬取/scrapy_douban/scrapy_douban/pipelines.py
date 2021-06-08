# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql, pymongo


class ScrapyDoubanPipeline(object):

    def open_spider(self, spider):
        self.conn = pymysql.connect(
        host="127.0.0.1", user="root", password="zhan", db='douban', port=3306
    )
        self.cursor = self.conn.cursor()


    def process_item(self, item, spider):
        print(item["describe"])
        sql = 'insert into douban_250(title, rank, score, abstract, `describe`) values ("%s", "%s", "%s", "%s", "%s");' % (
            item["title_detail"], item["rank_detail"], item["score"], item["abstract_detail"], item["describe"])
        # sql = "select * from douban_250"
        # sql = "insert into douban_250(title, rank, score, abstract, `describe`) values ("%s", "%s", "%s", "%s", "%s");"
        #
        # self.cursor.execute(sql%(
        #     item["title_detail"],
        #     item["rank_detail"],
        #     item["score"],
        #     item["abstract_detail"],
        #     item["describe"]
        # ))
        self.cursor.execute(sql)
        # print(self.cursor.fetchall())
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()



class ScrapyDoubanMongoPipeline(object):

    def open_spider(self, spider):
        self.conn = pymongo.MongoClient(host="localhost", port=27017)
        self.db = self.conn.douban
        # self.db = self.conn["douban"]
        self.movies = self.db.movies

    def process_item(self, item, spider):
        self.movies.insert(
            {
                "title": item["title_detail"],
                "rank": item["rank_detail"],
                'score':  item["score"],
                "abstract_detail": item["abstract_detail"],
                "describe": item["describe"]
            }
        )

        return item


    def close_spider(self, spider):
        self.conn.close()