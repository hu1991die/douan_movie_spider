# encoding: utf-8
'''
@author: feizi
@file: DoubanMovieTop250Spider.py
@time: 2017/10/19 22:26
@Software: PyCharm
@desc:
'''
import re

from scrapy import Request
from scrapy.spiders import Spider
from douan_movie_spider.items import DouanMovieItem

class DoubanMovieTop250Spider(Spider):
    name = 'douban_movie_top250'

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url)

    def parse(self, response):
        item = DouanMovieItem()
        movieList = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movieList:
            # 排名
            rank = movie.xpath('.//div[@class="pic"]/em/text()').extract_first()
            # 封面
            cover = movie.xpath('.//div[@class="pic"]/a/img/@src').extract_first()
            # 标题
            title = movie.xpath('.//div[@class="hd"]/a/span[1]/text()').extract_first()
            # 评分
            score = movie.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract_first()
            # 评价人数
            comment_num = movie.xpath('.//div[@class="star"]/span[4]/text()').re(ur'(\d+)')[0]
            # 经典语录
            quote = movie.xpath('.//p[@class="quote"]/span[@class="inq"]/text()').extract_first()
            # 上映年份,上映地区，电影分类
            briefList = movie.xpath('.//div[@class="bd"]/p/text()').extract()
            if briefList:
                # 以'/'进行分割
                briefs = re.split(r'/', briefList[1])
                # 电影分类
                types = re.compile(u'([\u4e00-\u9fa5].*)').findall(briefs[len(briefs) - 1])[0]
                # 上映地区
                region = re.compile(u'([\u4e00-\u9fa5]+)').findall(briefs[len(briefs) - 2])[0]
                if len(briefs) <= 3:
                    # 上映年份
                    years = re.compile(ur'(\d+)').findall(briefs[len(briefs) - 3])[0]
                else:
                    # 上映年份
                    years = ''
                    for brief in briefs:
                        if hasNumber(brief):
                            years = years + re.compile(ur'(\d+)').findall(brief)[0] + ","
                            print years

                if types:
                    # 替换空格为“,”
                    types = types.replace(" ", ",")

            print(rank, cover, title, score, comment_num, quote, years, region, types)
            item['rank'] = rank
            item['cover'] = cover
            item['title'] = title
            item['score'] = score
            item['comment_num'] = comment_num
            item['quote'] = quote
            item['years'] = years
            item['region'] = region
            item['types'] = types
            yield item

        # 获取下一页url
        next_url = response.xpath('//span[@class="next"]/a/@href').extract_first()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url
            yield Request(next_url)

def hasNumber(str):
    return bool(re.search('\d+', str))