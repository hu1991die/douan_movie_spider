# encoding: utf-8
'''
@author: feizi
@file: test.py
@time: 2017/11/19 17:32
@Software: PyCharm
@desc:
'''
import re
from lxml import etree

str = '''
<p class="">
                            导演: 万籁鸣 Laiming Wan / 唐澄 Cheng  Tang&nbsp;&nbsp;&nbsp;主演: 邱岳峰 Yuefeng Qiu /...<br>
                            1961 / 1964 / 1978 / 2004&nbsp;/&nbsp;中国大陆&nbsp;/&nbsp;动画 奇幻
                        </p>
'''

def run():
    briefList = etree.HTML(str, ).xpath('.//p/text()')
    if briefList:
        # 以'/'进行分割
        briefs = re.split(r'/', briefList[1])
        # 上映年份
        for brief in briefs:
            if hasNumber(brief):
                years = ''
                years = years + re.compile(ur'(\d+)').findall(brief)[0] + ','
                print years.join(';')

def hasNumber(str):
    return bool(re.search('\d+', str))


if __name__ == '__main__':
    run()