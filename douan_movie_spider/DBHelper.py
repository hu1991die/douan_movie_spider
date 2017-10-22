# encoding: utf-8
'''
@author: feizi
@file: DBHelper.py
@time: 2017/10/22 16:51
@Software: PyCharm
@desc:
'''

import pymysql
#导入seetings配置
from scrapy.utils.project import get_project_settings

class DBHelper():
    def __init__(self):
        # 获取settings配置，设置需要的信息
        self.settings=get_project_settings()

        self.host=self.settings['HOST']
        self.port=self.settings['PORT']
        self.user=self.settings['USER']
        self.password=self.settings['PASSWORD']
        self.db=self.settings['DB_NAME']

    # 连接到Mysql,不是链接到具体的数据库
    def connectMysql(self):
        # 初始化打开数据库连接
        conn = pymysql.Connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.password,
            # db=self.db,不指定数据库名
            charset='utf8' # 要指定编码，否则中文可能乱码
        )
        return conn

    def connectDatabase(self):
        # 初始化打开数据库连接
        conn = pymysql.Connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.password,
            db=self.db,
            charset='utf8'  # 要指定编码，否则中文可能乱码
        )
        return conn

    # 创建数据库
    def createDb(self):
        # 连接数据库
        conn = self.connectMysql()

        sql = "CREATE database IF NOT EXISTS " + self.db
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        conn.close()

    # 创建数据表
    def createTable(self, sql):
        conn = self.connectDatabase()

        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        conn.close()

    # 插入数据
    '''注意这里params要加*,因为传递过来的是元组，*表示参数个数不定'''
    def insert(self, sql, *params):
        conn = self.connectDatabase()

        cursor = conn.cursor()
        cursor.execute(sql, params)
        # 事务commit
        self.conn.commit()
        cursor.close()
        conn.close()


    # 更新数据
    def update(self, sql, *params):
        conn = self.connectDatabase()

        cursor = conn.cursor()
        cursor.execute(sql, params)
        # 事务commit
        self.conn.commit()
        cursor.close()
        conn.close()


    # 删除数据
    def delete(self, sql, *params):
        conn = self.connectDatabase()

        cursor = conn.cursor()
        cursor.execute(sql, params)
        # 事务commit
        self.conn.commit()
        cursor.close()
        conn.close()


'''测试DBHelper的类'''
class TestDBHelper():
    def __init__(self):
        self.dbHelper=DBHelper()

    # 测试创建数据库（settings配置文件中的MYSQL_DBNAME,直接修改settings配置文件即可）
    def testCreateDb(self):
        self.dbHelper.createDb()

    # 测试创建表
    def testCreateTable(self):
        sql = "CREATE TABLE testtable(id INT PRIMARY KEY AUTO_ increment, name VARCHAR(50), url VARCHAR(200))"

        self.dbHelper.createTable(sql)

    # 测试插入
    def testInsert(self):
        sql = "insert into testtable(name,url) values(%s,%s)"
        params = ("test", "test")
        #  *表示拆分元组，调用insert（*params）会重组成元组
        self.dbHelper.insert(sql, *params)

    # 测试更新
    def testUpdate(self):
        sql = "update testtable set name=%s,url=%s where id=%s"
        params = ("update", "update", "1")
        self.dbHelper.update(sql, *params)

    # 测试删除
    def testDelete(self):
        sql = "delete from testtable where id=%s"
        params = ("1")
        self.dbHelper.delete(sql, *params)

if __name__=="__main__":
    testDBHelper=TestDBHelper()
    testDBHelper.testCreateDb()  #执行测试创建数据库
    # testDBHelper.testCreateTable()     #执行测试创建表
    #testDBHelper.testInsert()          #执行测试插入数据
    #testDBHelper.testUpdate()          #执行测试更新数据
    #testDBHelper.testDelete()          #执行测试删除数据
