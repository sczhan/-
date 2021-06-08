# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QcwySpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_url = scrapy.Field()
    record_data = scrapy.Field()
    job_tag = scrapy.Field()

    job_name = scrapy.Field()
    job_info = scrapy.Field()
    jon_salary = scrapy.Field()
    job_welfare = scrapy.Field()
    job_exp_require = scrapy.Field()
    job_edu_require = scrapy.Field()
    company_name = scrapy.Field()
    company_industry = scrapy.Field()
    company_people = scrapy.Field()
    company_location = scrapy.Field()
    company_overview = scrapy.Field()
    company_financing_stage = scrapy.Field()
    job_country = scrapy.Field()
