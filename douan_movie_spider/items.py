# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 电影实体类
class DouanMovieItem(scrapy.Item):
    # 排名
    rank = scrapy.Field()
    # 封面
    cover = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 评价人数
    comment_num = scrapy.Field()
    # 经典语录
    quote = scrapy.Field()
    # 上映年份
    years = scrapy.Field()
    # 上映地区
    region = scrapy.Field()
    # 电影类型
    types = scrapy.Field()
