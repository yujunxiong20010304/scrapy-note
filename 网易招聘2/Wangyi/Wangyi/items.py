# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WangyiItem(scrapy.Item):
    # define the fields for your item here like:
    Job_title = scrapy.Field()    # 职位名称
    Department = scrapy.Field()    # 所属部门
    Position_category = scrapy.Field()  # 职位类别
    Type_work = scrapy.Field()  # 工作类别
    Duty_station = scrapy.Field()  # 工作地点
    Number_recruits = scrapy.Field()  # 招聘人数
    Release_time = scrapy.Field()  # 发布时间
    link = scrapy.Field()         # 深入网址的连接
    Job_requirements = scrapy.Field()  # 岗位要求
    Job_description = scrapy.Field()    # 岗位描述

    pass
