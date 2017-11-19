# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
from scrapy.exceptions import DropItem

from douan_movie_spider.items import DouanMovieItem

# 获取数据库连接
def getDbConn():
    conn = MySQLdb.Connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='123456',
        db='testdb',
        charset='utf8'
    )
    return conn

# 关闭数据库资源
def closeConn(cursor, conn):
    # 关闭游标
    if cursor:
        cursor.close()
    # 关闭数据库连接
    if conn:
        conn.close()


class DouanMovieSpiderPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['title'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['title'])
            if item.__class__ == DouanMovieItem:
                self.insert(item)
                return
        return item

    def insert(self, item):
        try:
            # 获取数据库连接
            conn = getDbConn()
            # 获取游标
            cursor = conn.cursor()
            # 插入数据库
            sql = "INSERT INTO db_movie(rank, cover, title, score, comment_num, quote, years, region, types)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            params = (item['rank'], item['cover'], item['title'], item['score'], item['comment_num'], item['quote'], item['years'], item['region'], item['types'])
            cursor.execute(sql, params)

            #事务提交
            conn.commit()
        except Exception, e:
            # 事务回滚
            conn.rollback()
            print 'except:', e.message
        finally:
            # 关闭游标和数据库连接
            closeConn(cursor, conn)



