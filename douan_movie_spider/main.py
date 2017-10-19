# encoding: utf-8
'''
@author: feizi
@file: main.py
@time: 2017/10/19 22:09
@Software: PyCharm
@desc:
'''

from scrapy import cmdline

name = "douban_movie_top250"
cmd = "scrapy crawl {0} -o douban.csv".format(name)
cmdline.execute(cmd.split())