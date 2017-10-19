# encoding: utf-8
'''
@author: feizi
@file: DoubanMovieTop250Spider.py
@time: 2017/10/19 22:26
@Software: PyCharm
@desc:
'''

from scrapy import Request
from scrapy.spiders import Spider
from douan_movie_spider.items import DouanMovieItem

class DoubanMovieTop250Spider(Spider):
    name = 'douban_movie_top250'

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3013.3 Safari/537.36'
    }

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url, headers=self.headers)

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
            comment_num = movie.xpath('.//div[@class="star"]/span/text()').re(r'(\d+)人评价')[0]
            # 经典语录
            quote = movie.xpath('.//p[@class="quote"]/span[@class="inq"]/text()').extract_first()

            print(rank, cover, title, score, comment_num, quote)
            item['rank'] = rank
            item['cover'] = cover
            item['title'] = title
            item['score'] = score
            item['comment_num'] = comment_num
            item['quote'] = quote
            yield item

        # 获取下一页url
        next_url = response.xpath('//span[@class="next"]/a/@href').extract_first()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url
            yield Request(next_url, headers=self.headers)
