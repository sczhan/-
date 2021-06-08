# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql, pymongo

class QcwyPipeline(object):
    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host="127.0.0.1", user="root", password="zhan", db='qcwy', port=3306
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):

        sql = 'insert into qcwy(job_name, xinxi, xinzi, fuli, jinyan, xueli, gsname, hangye, xingzhi, renshu, ' \
              'gaikuang) values ("%s", "%s", "%s", "%s", "%s","%s", "%s", "%s", "%s", "%s","%s");' % (item["job_name"],
                                                                                                      item["xinxi"],
                                                                                                    item["xinzi"],
                                                                                                    item["fuli"],
                                                                                                    item["jinyan"],
                                                                                                    item["xueli"],
                                                                                                    item["gsname"],
                                                                                                    item["hangye"],
                                                                                                    item["xingzhi"],
                                                                                                    item["renshu"],
                                                                                                    item["gaikuang"])
        self.cursor.execute(sql)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()




class QcwyMongoPipeline(object):

    def open_spider(self, spider):
        self.conn = pymongo.MongoClient(host="localhost", port=27017)
        self.db = self.conn.qcwy
        # self.db = self.conn["qcwy"]
        self.movies = self.db.qcwy

    def process_item(self, item, spider):
        self.movies.insert(
            {
                'job_name': item["job_name"],
                'xinxi': item["xinxi"],
                'xinzi': item["xinzi"],
                'fuli':  item["fuli"],
                'jinyan': item["jinyan"],
                'xueli':  item["xueli"],
                'gsname': item["gsname"],
                'hangye': item["hangye"],
                'xingzhi': item["xingzhi"],
                'renshu': item["renshu"],
                'gaikuang': item["gaikuang"],
            }
        )

        return item


    def close_spider(self, spider):
        self.conn.close()