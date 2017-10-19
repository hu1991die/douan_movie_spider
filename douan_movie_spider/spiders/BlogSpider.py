# encoding: utf-8
'''
@author: feizi
@file: BlogSpider.py
@time: 2017/10/19 22:12
@Software: PyCharm
@desc:
'''

from scrapy.spiders import Spider

class BlogSpider(Spider):
    name = "hu1991die"
    start_urls = ['http://hu1991die.com/archives/']

    def parse(self, response):
        titles = response.xpath('//a[@class="archive-article-title"]/text()').extract()
        if titles:
            for title in titles:
                print(title.strip())